def main():
    n = input()
    seq = [int(a) for a in input().split(" ")]
    q = int(input())
    for _ in range(q):
        b, e = map(int, input().split(" "))
        tmp = seq[b:e]
        tmp = tmp[::-1]
        seq[b:e] = tmp[:]
    print(*seq)
main()