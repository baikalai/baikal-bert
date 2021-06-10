# coding: utf-8

from transformers import pipeline

# 토크나이저, 태스크가 모두 정의되어 있으므로 바로 실행 가능
nlp = pipeline("fill-mask", model="deeq/dbert")
result = nlp("대한민국은 민주[MASK]입니다")

for r in result:
    print(r)
