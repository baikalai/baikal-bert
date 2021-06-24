# coding: utf-8

from transformers import pipeline

# 모델과 태스트만 주어지면 바로 실행
nlp = pipeline("fill-mask", model="deeq/dbert")
text = "서울은 한국의 [MASK]입니다."
result = nlp(text)

for r in result:
    print(r)
