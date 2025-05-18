from sys import stdin

def main():
    N = int(input())
    if N < 2:
        print('Hello World')
    else:
        A = int(input())
        B = int(input())
        print(A + B)

input = lambda: stdin.readline()
main()