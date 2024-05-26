# length_mapper.py

"""텍스트 한 줄을 단어 길이와 1의 쌍으로 변환"""
import sys

def tokenize_input():
    """표준 입력으로 들어오는 각 줄은 문자열 리스트로 분리"""
    for line in sys.stdin:
        yield line.split()
    
    # 표준 입력으로 각 줄을 읽고 각 단어별로 단어, 탭, 1 형태로 키-값쌍 만들기
    
    for line in tokenize_input():
        for word in line:
            print(str(len(word) + '\t1'))

# length_reducer.py
"""같은 단어 길이를 갖는 단어 수를 센다"""
import sys
from itertools import groupby
from operator import itemgetter

def tokenize_input():
    """표준 입력으로 들어오는 각 줄은 문자열 리스트로 분리"""
    for line in sys.stdin:
        yield line.split('\t')

# 단어 길이와 단어 수를 탭으로 분리한 키-값 쌍을 만든다
for word_length, group in groupby(tokenize_input(), itemgetter(0)):
    try:
        total = sum(int(count) for word_length, count in group)
        print(word_length + '\t' + str(total))
    except ValueError:
        pass # 단어 수가 정수가 아니면 해닽 단어 무시
