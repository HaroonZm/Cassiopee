def counting_sort(a, b, k):
    c = [0 for _ in range(k)]
    
    for i in range(len(a)):
        c[a[i]] += 1 # 要素の数を数えた配列
    

    for i in range(1, k):
        c[i] += c[i-1] # 積み重ねたもの
    

    for i in range(len(a))[::1]:
        b[c[a[i]] -1] = a[i]
        c[a[i]] -= 1
    
    return b

def main():
    n = int(input())
    A = list(map(int, input().split()))

    B = [0 for _ in range(len(A))]

    b = counting_sort(A, B, max(A)+1)

    print(" ".join(map(str, b)))

if __name__ == "__main__":
    main()