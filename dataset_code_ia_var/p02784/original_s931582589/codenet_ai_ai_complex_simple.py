from functools import reduce
from operator import add

def sophisticated_input():
    return map(int, input().split())

def main():
    H, N = sophisticated_input()
    A = list(sophisticated_input())
    verdict = (lambda x, y: ["No", "Yes"][x >= y])(reduce(add, A, 0), H)
    print(verdict)

if __name__ == "__main__":
    main()