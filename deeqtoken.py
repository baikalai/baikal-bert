import sys
import unicodedata
import deeqnlpy

## Using docker(server on localhost)
# docker run -d -p 5659:5656 baikalai/deeq-nlp:v1.5.0
#__host = "localhost"
#__port = 5659
#_tagger = deeqnlpy.Tagger(host=__host, port=__port)

_tagger = deeqnlpy.Tagger()


# 앞에서부터 제일 긴 토큰을 찾는다
def _long_token_for(t, vocab, unk):
    if t in vocab:
        return t, ''
    # 한 글자인 경우 찾고 바로 나가도록
    if len(t) == 1:
        n = 1
    else:
        n = -1
    while True:
        w = t[:n]
        if w == '':
            break
        if w in vocab:
            return w, t[len(t)+n:]
        n -= 1
    return unk, ''


# 뒤에서부터 제일 긴 토큰을 찾는다
def _long_token_rev(t, vocab, unk):
    if t in vocab:
        return t, ''
    n = 1
    while True:
        if len(t) > 1:
            w = t[n:]
        else:
            w = t
            n = 0
        if w == '':
            break
        if w in vocab:
            return w, t[:n]
        n += 1
    return unk, ''


# unk를 잘라서 토큰으로 바꿈
def _unk2tokens(t, vocab, unk):
    k1 = []
    t1 = t
    while True:
        out, rem = _long_token_for(t1, vocab, unk)
        k1.append(out)
        if rem == '':
            break
        t1 = rem
    # while True:
    #     out, rem = self._long_token_rev(t2)
    #     k2.append(out)
    #     if rem == '':
    #         k2.reverse()
    #         break
    #     t2 = rem
    # if len(k1) < len(k2):
    #     return k1
    return k1


def _tokenize(res, word=False, newline=False, tags=False):
    tos = []
    for tok in res:
        if word:
            tos.append('_'+tok)
        else:
            tos.append(tok)
    if newline:
        tos.append('\n')
    return tos


def _clean(text):
    # delete: control-chars(^A,^B,^J) or unknown unicode-chars
    text = ''.join(list(c for c in text if c=='\n' or unicodedata.category(c)[:1]!='C'))
    # replace: space & grave accent
    return text.replace('\u00a0', ' ').replace("`", "'")


def analyze(text, word=False, clean=True, newline=False, tags=False):
    if clean:
        text = _clean(text)
    res = _tagger.morphs(text)
    return _tokenize(res, word, newline, tags)


def do_tokenize(text, vocab, unk, word=False, resolve=True, clean=True):
    out = []
    tokens = analyze(text, word=word, clean=clean, newline=False)
    for tk in tokens:
        if tk in vocab or tk == '\n':
            out.append(tk)
        elif resolve:
            rt = _unk2tokens(tk, vocab, unk)
            if rt is None or len(rt) == 0:
                out.append(unk)
            else:
                out.extend(rt)
        else:
            out.append(unk)
    return out


_break = '\u2581'

def word_break(vocab):
    return _break+'/' in vocab


_mask_tok = "[MASK]"

def tokenize(text, vocab, unk="[UNK]", word=False, resolve=True, clean=True):
    mask = text.find(_mask_tok)
    out = []
    if mask == -1:
        out = do_tokenize(text, vocab, unk, word, resolve, clean)
    else:
        out = do_tokenize(text[:mask], vocab, unk, word, resolve, clean)
        out.append(_mask_tok)
        out.extend(do_tokenize(text[mask+6:], vocab, unk, word, resolve, clean))
    return out


def batch(reader, vocab, unk, step=250, word=False):
    tokens = [[]]
    tags = [[]]
    para = []
    lines = reader.readlines()
    lmax = len(lines)
    loops = lmax//step + 1
    # spch = ord('\n')
    for li in range(loops):
        begin = li*step
        next_end = (li+1)*step
        end = min(lmax, next_end)
        para = [[] if l=='\n' else [''] for l in lines[begin:end]]
        text = '\n'.join(lines[begin:end])
        # clear spaces & special characters
        #text = repeat_reduce(text, 3)
        res = tokenize(text, vocab, unk, word=word, resolve=True, clean=True)
        for tok in res:
            if tok == '\n':
                tags.append([])
            else:
                tags[-1].append(tok)
        ntag = 0
        for pa in para:
            if ntag >= len(tags):
                break
            if len(pa) == 1:
                tokens[-1].append(tags[ntag])
                ntag += 1
            else:
                tokens.append([])
        # print(tokens[-1])
        # input()
    return tokens
