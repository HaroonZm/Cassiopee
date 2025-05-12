"""
2つの集合から積集合を求める

input:
4
2 3 5 6
5
2 5 6 7 9
output:
2
5
6
"""

if __name__ == "__main__":
    input()
    A = set(map(int, input().split()))
    input()
    B = set(map(int, input().split()))
    I = A & B
    if I:
        print(*sorted(I), sep="\n")