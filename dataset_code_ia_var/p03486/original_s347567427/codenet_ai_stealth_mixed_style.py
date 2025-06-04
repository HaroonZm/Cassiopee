L = []
Ss = input()
Ts = input()
ls = [c for c in Ss]
lt = []
for ch in Ts:
    lt.append(ch)
sorted_s = sorted(ls)
lt.sort(key=lambda x: x, reverse=True)
S_ = ''.join(sorted_s)
T_ = ''
for j in range(len(lt)):
    T_ = T_ + lt[j]
if S_ == T_:
    print("No")
else:
    def append_and_sort(x, y, arr):
        arr += [x]
        arr.append(y)
        arr.sort()
        return arr
    tmp = append_and_sort(S_, T_, L)
    if tmp[0] is S_:
        print("Yes")
    else:
        print("No")