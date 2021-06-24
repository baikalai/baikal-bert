# deeq-bert

- deeq-bert는 baikal.ai가 개발하고 있는 pre-trained BERT 모델입니다.
- 한국어 위키, 1990~2020 네이버 뉴스 등을 포함한 다양한 말뭉치를 정제하여 학습합니다.
- 모델은 huggingface에 deeq/dbert, deeq/dbert5로 공개되어있어 transformers 라이브러리로 간편하게 사용할 수 있습니다.
- dbert는 BertTokenizer(wordpiece)를 그대로 사용하므로 BERT 모델을 사용하는 코드에서 쉽게 불러쓸 수 있습니다.
- dbert**5**는 deeqnlp 형태소 분석기를 사용한 DeeqTokenizer와 **5**0000 크기의 vocab을 사용합니다.

# files

- dbert.py: huggingface의 transformers를 사용하여 deeq/dbert를 불러오는 단순한 예를 보여줍니다.
- dbert5.py: deeqnlp tokenizer로 만든 bert를 transformers로 사용하는 예시입니다.
- deeqtoken.py: deeqnlp로 tokenize 처리하는 코드입니다.
- tokenization_dq.py: tokenizers와 호환되게 만든 DeeqTokenizer 입니다.
- vocab-bert.txt: wordpiece로 만들어진 vocab(dbert)
- vocab-deeq.txt: 형태소 분석기(deeqnlp)로 만들어진 vocab(dbert5)

# sample runs

- dbert.py: 내장된 토크나이저를 사용하기때문에 한줄로 결과가 나옵니다.
```
nlp = pipeline("fill-mask", model="deeq/dbert")
result = nlp("서울은 한국의 [MASK]입니다.")
```
이렇게...
```
{'sequence': '서울은 한국의 수도 입니다.', 'score': 0.32904720306396484, 'token': 2443, 'token_str': '수도'}
{'sequence': '서울은 한국의 심장 입니다.', 'score': 0.06646282970905304, 'token': 9176, 'token_str': '심장'}
{'sequence': '서울은 한국의 땅 입니다.', 'score': 0.056068792939186096, 'token': 332, 'token_str': '땅'}
{'sequence': '서울은 한국의 도시 입니다.', 'score': 0.03166551515460014, 'token': 2679, 'token_str': '도시'}
{'sequence': '서울은 한국의 중심 입니다.', 'score': 0.02802455797791481, 'token': 2426, 'token_str': '중심'}
```

- dbert5.py: 자체 토크나이저를 사용한 pipeline을 생성해주면 됩니다.
```
model = BertForMaskedLM.from_pretrained("deeq/dbert5")
tokenizer = DeeqTokenizer("vocab-deeq.txt")
nlp = FillMaskPipeline(model, tokenizer)
result = nlp("서울은 한국의 [MASK]입니다.")
```
거의 비슷한 결과입니다. 토크나이징이 한글 형태소 구분으로 되어 있는 것을 알 수 있습니다.
```
{'sequence': '서울 은 한국 의 수도 이 ㅂ니다.', 'score': 0.4248102903366089, 'token': 22588, 'token_str': '수 도'}
{'sequence': '서울 은 한국 의 땅 이 ㅂ니다.', 'score': 0.0505908727645874, 'token': 647, 'token_str': '땅'}
{'sequence': '서울 은 한국 의 도시 이 ㅂ니다.', 'score': 0.0380173921585083, 'token': 22190, 'token_str': '도 시'}
{'sequence': '서울 은 한국 의 고향 이 ㅂ니다.', 'score': 0.030805835500359535, 'token': 24598, 'token_str': '고 향'}
{'sequence': '서울 은 한국 의 자랑 이 ㅂ니다.', 'score': 0.0296196099370718, 'token': 23795, 'token_str': '자 랑'}
```
