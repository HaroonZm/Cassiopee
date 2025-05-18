#!/usr/bin/env python

N = int(input())
U = [input() for i in range(0,N)]
M = int(input())
door = False
for i in range(M):
    T = input()
    if T in U:
        if door == True:
            print("Closed by " + T)
            door = False
        else:
            print("Opened by " + T)
            door = True
    else:
        print("Unknown " + T)