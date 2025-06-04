def read_input():
    n, k, l = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, l, a

def can_take_this_value(current, X):
    return current <= X

def should_increment_cnt2(cnt2, k):
    return cnt2 == k - 1

def add_to_cnt1(cnt1, n, j):
    return cnt1 + (n - j)

def process_j_loop(n, k, X, A, i, r, cnt2, cnt1):
    for j in range(r, n):
        if should_increment_cnt2(cnt2, k) and can_take_this_value(A[j], X):
            r = j
            cnt1 = add_to_cnt1(cnt1, n, j)
            if can_take_this_value(A[i], X):
                cnt2 -= 1
            break
        elif can_take_this_value(A[j], X):
            cnt2 += 1
    else:
        return r, cnt1, cnt2, False
    return r, cnt1, cnt2, True

def is_ok(X, n, k, l, A):
    r = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        r, cnt1, cnt2, cont = process_j_loop(n, k, X, A, i, r, cnt2, cnt1)
        if not cont:
            break
    return cnt1 >= l

def bisearch(high, low, n, k, l, A):
    while high - low > 1:
        mid = (high + low) // 2
        if is_ok(mid, n, k, l, A):
            high = mid
        else:
            low = mid
    return high

def main():
    n, k, l, a = read_input()
    result = bisearch(200000, -1, n, k, l, a)
    print(result)

main()