from BoW import *

# 벡터 연산에 효과적인 numpy 패키지 이용
import numpy as np

# Eucludean Distance 계산 함수
def euclidean_distance(A, B):
    # 1. (A-B)의 원소의 제곱 연산 이후, 모든 요소의 합을 구한다
    # 2. 양의 제곱근을 반환한다
    return np.sqrt(np.sum((A-B)**2))


docs = ["나는 아침보다 저녁이 더 좋다", "사과는 아침보다 저녁이 더 좋다", "사과는 점심 간식으로 좋다"]
docsV = []

for doc in docs:
    vocab, bow = bag_of_words(doc)
    docsV.append(np.array(bow))

## issue : BoW 로 벡터화 한 것의 길이를 맞춰보는 작업 해보기

""" array = 나는 / 아침보다 / 저녁이 / 더 / 좋다 / 사과는 / 점심 / 간식으로 """
doc1 = np.array([1, 1, 1, 1, 1, 0, 0, 0])
doc2 = np.array([0, 1, 1, 1, 1, 1, 0, 0])
doc3 = np.array([0, 0, 0, 0, 1, 1, 1, 1])

print(f"1. docs1-docs2 E.D. : {euclidean_distance(doc1, doc2)}")
print(f"1. docs2-docs3 E.D. : {euclidean_distance(doc2, doc3)}")
print(f"1. docs3-docs1 E.D. : {euclidean_distance(doc3, doc1)}")