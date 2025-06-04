N = int(input())
A = {}
for s in input().split():
    n = int(s)
    if n in A:
        A[n] += 1
    else:
        A[n] = 1

def main():
    a_len = len(A)
    counts = A.values()
    even = [c for c in counts if c % 2 == 0]
    if len(even) % 2 == 0:
        ans = a_len
    else:
        ans = a_len - 1
    print(ans)

if __name__ == "__main__":
    main()