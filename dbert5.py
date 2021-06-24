# coding: utf-8

from transformers import BertForMaskedLM, FillMaskPipeline
from tokenization_dq import DeeqTokenizer

# model과 tokenizer를 읽어옵니다
model = BertForMaskedLM.from_pretrained("deeq/dbert5")
tokenizer = DeeqTokenizer("vocab-deeq.txt")

# pipeline을 생성하고
nlp = FillMaskPipeline(model, tokenizer)

# task를 실행
text = "서울은 한국의 [MASK]입니다."
result = nlp(text)

for r in result:
    print(r)
