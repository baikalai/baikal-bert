# dbert

이 프로젝트는 huggingface에 등록되어있는 deeq/dbert, deeq/dbert5의 사용법을 설명하고 있습니다.

dbert 시리즈는 baikal.ai가 만들고 있는 pre-trained transformer 모델중 BERT를 기반으로한 모델입니다.

모델들은 같은 말뭉치를 사용해 학습하고 있고, 이름은 사용하는 토크나이저와 vocab의 차이에 따라 구분됩니다.

- dbert: BertTokenizer(Wordpiece)를 사용하므로 모든 BERT 모델을 사용하는 작업에 쉽게 적용할 수 있습니다.

- dbert5: deeqnlp 토크나이저와 그것으로 제작된 50000크기의 vocab을 사용합니다. 정확한 형태소 분석기 기반이므로 한국어 과제에 더 적합한 모델입니다.

# files

- example.py: huggingface의 transformers를 사용하여 deeq/dbert를 쉽게 실행할 수 있는 첫번째 예를 보여줍니다.

# todo

dbert5, dbert을 실제 사용할 수 있는 샘플 코드들을 추가할 예정입니다.
