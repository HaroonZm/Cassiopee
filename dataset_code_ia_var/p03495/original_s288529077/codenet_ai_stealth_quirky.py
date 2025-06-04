# Mode: Emacs-27.2; encoding: utf-8
from collections import Counter as CNT

(n, k), A = (lambda: (map(int, input().split()), list(map(int, input().split()))))()
COUNT_DICT = CNT(A)
VALUE_LIST = sorted(list(COUNT_DICT.values()), key=lambda x: x)
del A, COUNT_DICT  # Prefers explicit resource release
print((lambda L, SKIP: sum(L[:len(L)-SKIP]) if SKIP else sum(L))(VALUE_LIST, k))