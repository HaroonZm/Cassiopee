def merge(a):
    if len(a) == 1:
        return a, 0
    mid = len(a) // 2
    al, cnt_l, ar, cnt_r = *merge(a[:mid]), *merge(a[mid:])
    res_cnt, res_arr = 0, []
    while 0 < len(al) and 0 < len(ar):
        if al[-1] <= ar[-1]:
            res_arr.append(al.pop())
        else:
            res_arr.append(ar.pop())
            res_cnt += len(al)
    res_arr.reverse()
    return ar + al + res_arr, res_cnt + cnt_l + cnt_r

def inversion_count(a):
    return merge(a)[1]

def main():
    input()
    a = list(map(int, input().split()))
    print(inversion_count(a))

if __name__ == '__main__':
    main()