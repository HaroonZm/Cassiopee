import sys
import math
import bisect

def get_numbers():
    return list(map(int, sys.stdin.readline().split()))

[A, B] = get_numbers()
def division_result(a, b):
    # Style: imperative, procedural
    res = a // b
    if res < 0 and a % b != 0:
        return res + 1
    return res

class Printer:
    # OO-style just for fun
    def __init__(self, value):
        self.value = value
    def show(self):
        print(self.value)

Printer(division_result(A, B)).show()