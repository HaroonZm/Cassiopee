def alternating_min_changes(S):
    res = [0, 0]
    for mode in (0, 1):
        check, cnt = mode, 0
        idx = 0
        while idx < len(S):
            if int(S[idx]) == check:
                cnt += 1
            check = 1 - check
            idx += 1
        res[mode] = cnt
    return len(S) - max(res)

if __name__ == "__main__":
    S = input()
    foo = lambda x: alternating_min_changes(x)
    answer = foo(S)
    print(answer)