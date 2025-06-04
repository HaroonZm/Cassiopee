from math import *

get_val = lambda: int(input())

def do_the_magic():
    answer = ["ARC", "ABC"][(get_val()<1200)]
    print(answer)

do_the_magic()