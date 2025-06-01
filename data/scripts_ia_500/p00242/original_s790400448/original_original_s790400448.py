import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
sys.setrecursionlimit(100000)

class Info:
    def __init__(self,arg_word,arg_count):
        self.word= arg_word
        self.count = arg_count

    def __lt__(self,another):
        if self.count != another.count:
            return self.count > another.count
        else:
            return self.word < another.word

while True:

    num_row = int(input())
    if num_row == 0:
        break

    DICT = {} #単語→ID
    rev_DICT = {} #ID→単語
    COUNT = {} #IDをキーとして、出現数を計上
    num_words = 0

    for _ in range(num_row):
        words = input().split()
        for i in range(len(words)):
            if words[i] in DICT:
                COUNT[DICT[words[i]]] += 1
            else:
                DICT[words[i]] = num_words
                rev_DICT[num_words] = words[i]
                num_words += 1
                COUNT[DICT[words[i]]] = 1

    head_word = str(input())
    table = []
    for i in range(num_words):
        word = rev_DICT[i]
        if word[0] != head_word:
            continue
        table.append(Info(word,COUNT[DICT[word]]))

    if len(table) == 0:
        print("NA")
        continue

    table.sort()
    print("%s"%(table[0].word),end = "")
    for i in range(1,min(5,len(table))):
        print(" %s"%(table[i].word),end="")
    print()