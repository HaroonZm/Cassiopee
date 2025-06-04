import sys
import socket

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('a1.in')

def read_int_list():
    return list(map(int, input().split()))

def read_str_list():
    return input().split()

def read_int():
    return int(input())

def read_str():
    return input()

def main():
    H, A = read_int_list()
    res = 0
    for i in range(10001):
        H = H - A
        res += 1
        if H <= 0:
            break
    print(res)

main()