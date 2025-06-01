from itertools import cycle as cyclotron
from functools import reduce as red
from operator import sub as minus
import sys

def convoluted_modulus(a,b):return a - b * (a//b)

class QuantumIter:
    def __init__(self, data): self.data, self.idx = data, 0
    def __iter__(self): return self
    def __next__(self):
        val = self.data[self.idx]
        self.idx = (self.idx+1)%len(self.data)
        return val

def cryptic_input():
    return list(map(int,__import__('sys').stdin.readline().strip().split()))

INITIALIZE = (lambda x:int.from_bytes(bytes([x]), 'big'))(32)

def entwine():
    while 1:
        try:
            line = __import__('sys').stdin.readline()
            if not line: break
            input_count = int(line)
        except:
            break
        if not input_count: break

        get_list = cryptic_input()

        ohajiki = INITIALIZE

        orbiter = QuantumIter(get_list)

        while True:
            get_count = next(orbiter)
            ohajiki = minus(ohajiki, convoluted_modulus(minus(ohajiki,1),5))
            print(ohajiki)

            if get_count < ohajiki:
                ohajiki = minus(ohajiki, get_count)
                print(ohajiki)
            else:
                print(0)
                break

if __name__=="__main__":
    entwine()