# deeq-bert

- deeq-bert는 baikal.ai가 개발하고 있는 pre-trained BERT 모델입니다.
- 한국어 위키, 1990~2020 네이버 뉴스 등을 포함한 다양한 말뭉치를 정제하여 학습합니다.
- 모델은 huggingface에 deeq/dbert, deeq/dbert5로 등록되어 있어서 transformers 를 이용해 간편하게 사용할 수 있습니다.
- dbert는 BertTokenizer(wordpiece)를 그대로 사용하므로 BERT 모델을 사용하는 코드에서 쉽게 불러쓸 수 있습니다.
- dbert5는 deeqnlp 형태소 분석기를 사용한 DeeqTokenizer를 사용해서 만든 50000 크기의 vocab을 사용합니다.

# files

- example.py: huggingface의 transformers를 사용하여 deeq/dbert를 불러오는 단순한 예를 보여줍니다.

코드 한(?) 줄이면
```
from transformers import pipeline
nlp = pipeline("fill-mask", model="deeq/dbert")
result = nlp("대한민국은 민주[MASK]입니다")
```
이렇게 결과가 나옵니다.
```
{'sequence': '대한민국은 민주공화국 입니다', 'score': 0.9752267599105835, 'token': 16831, 'token_str': '##공화국'}
{'sequence': '대한민국은 민주국가 입니다', 'score': 0.01182450819760561, 'token': 5683, 'token_str': '##국가'}
{'sequence': '대한민국은 민주사회 입니다', 'score': 0.0010573873296380043, 'token': 2641, 'token_str': '##사회'}
{'sequence': '대한민국은 민주정부 입니다', 'score': 0.0009071531821973622, 'token': 2505, 'token_str': '##정부'}
{'sequence': '대한민국은 민주혁명 입니다', 'score': 0.0006644993554800749, 'token': 8764, 'token_str': '##혁명'}
```

# todo

dbert5 토크나이저 코드와 함께 몇가지 샘플 코드들을 추가할 예정입니다.
