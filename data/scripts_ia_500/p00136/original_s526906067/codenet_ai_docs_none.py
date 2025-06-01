import os
import math

def main():
    lst = [0,0,0,0,0,0]
    for i in range(int(input())):
        temp = float(input())
        if temp < 165:
            lst[0] += 1
        elif temp < 170:
            lst[1] += 1
        elif temp < 175:
            lst[2] += 1
        elif temp < 180:
            lst[3] += 1
        elif temp < 185:
            lst[4] += 1
        else:
            lst[5] += 1
    for i in range(6):
        print(f"{i+1}:", end="")
        for j in range(lst[i]):
            print("*", end="")
        print()

main()