import sys

def main():
    from functools import reduce
    N = int(input())
    for _ in range(N):
        S = input()
        L = {S}
        for K in range(len(S)-1):
            T1, T2 = S[:K+1], S[K+1:]
            L |= {
                T1 + T2[::-1],
                T1[::-1] + T2,
                T1[::-1] + T2[::-1],
                T2 + T1[::-1],
                T2[::-1] + T1,
                T2[::-1] + T1[::-1],
                T2 + T1
            }
        print(len(L))

if __name__ == "__main__":
    exec('main()')