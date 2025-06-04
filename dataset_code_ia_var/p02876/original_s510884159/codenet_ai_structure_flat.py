import heapq
import sys,random

input = sys.stdin.readline

N = int(input())
beam = [tuple(map(int, input().split())) for i in range(N)]
beam.sort(key=lambda x: x[1])
data = [min(0, beam[i][0] - beam[i][1]) for i in range(N)]
for i in range(N - 2, -1, -1):
    data[i] += data[i + 1]
cummin = [beam[i][1] for i in range(N)]
for i in range(N):
    if beam[i][0] - beam[i][1] > 0:
        cummin[i] = 10 ** 15
for i in range(N - 2, -1, -1):
    cummin[i] = min(cummin[i], cummin[i + 1])
ide_ele = 10 ** 15
def segfunc(x, y):
    return min(x, y)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def SegTree_build(init_val, segfunc, ide_ele):
    n = len(init_val)
    num = 1 << (n - 1).bit_length()
    tree = [ide_ele] * 2 * num
    for i in range(n):
        tree[num + i] = init_val[i]
    for i in range(num - 1, 0, -1):
        tree[i] = segfunc(tree[2 * i], tree[2 * i + 1])
    return tree, num

def SegTree_update(tree, num, segfunc, k, x):
    k += num
    tree[k] = x
    while k > 1:
        tree[k >> 1] = segfunc(tree[k], tree[k ^ 1])
        k >>= 1

def SegTree_query(tree, num, segfunc, ide_ele, l, r):
    res = ide_ele
    l += num
    r += num
    while l < r:
        if l & 1:
            res = segfunc(res, tree[l])
            l += 1
        if r & 1:
            res = segfunc(res, tree[r - 1])
        l >>= 1
        r >>= 1
    return res

start = 0
end = N
while end - start > 1:
    m = (end + start) // 2
    if m == 0:
        if data[0] <= 0:
            start = m
        else:
            end = m
        continue
    que = []
    cnt = 0
    S = 0
    ok = False
    for i in range(N - 1):
        if cnt == m:
            test = -que[0]
            if beam[i][0] < test:
                heapq.heappop(que)
                heapq.heappush(que, -beam[i][0])
                S += beam[i][0] - test
        else:
            heapq.heappush(que, -beam[i][0])
            S += beam[i][0]
            cnt += 1
        if cnt == m:
            test2 = S + data[i + 1]
            if test2 <= 0:
                ok = True
                break
    if ok:
        start = m
    else:
        end = m

if data[0] > 0:
    print(0, 1)
    sys.exit()

m = start
ans = [0, 1]
que = []
cnt = 0
S = 0
if m != 0:
    for i in range(N - 1):
        if cnt == m:
            test = -que[0]
            if beam[i][0] < test:
                heapq.heappop(que)
                heapq.heappush(que, -beam[i][0])
                S += beam[i][0] - test
        else:
            heapq.heappush(que, -beam[i][0])
            S += beam[i][0]
            cnt += 1
        if cnt == m:
            test2 = S + data[i + 1]
            B = cummin[i + 1]
            if test2 <= 0:
                t = abs(test2)
                if B * ans[0] < ans[1] * t:
                    ans = [t, B]
    start_arr = [-1] * N
    end_arr = [-1] * N
    que = []
    trash = []
    cnt = 0
    S = 0
    data1 = [ide_ele] * N
    data2 = [ide_ele] * N
    for i in range(N):
        if cnt == m:
            val, idx = que[0]
            val = -val
            if val > beam[i][0]:
                heapq.heappop(que)
                heapq.heappush(trash, val)
                end_arr[idx] = i - 1
                heapq.heappush(que, (-beam[i][0], i))
                start_arr[i] = i
                S += beam[i][0] - val
            else:
                heapq.heappush(trash, beam[i][0])
        else:
            heapq.heappush(que, (-beam[i][0], i))
            start_arr[i] = i
            S += beam[i][0]
            cnt += 1
        if cnt == m:
            if i != N - 1:
                data1[i] = S + data[i + 1]
                if trash:
                    data2[i] = S + data[i + 1] + trash[0]
                else:
                    data2[i] = S + data[i + 1]
            else:
                data1[i] = S
                data2[i] = S + (trash[0] if trash else 0)
    for i in range(N):
        if start_arr[i] != -1 and end_arr[i] == -1:
            end_arr[i] = N - 1
    tree1, num1 = SegTree_build(data1, segfunc, ide_ele)
    tree2, num2 = SegTree_build(data2, segfunc, ide_ele)
    for i in range(m):
        if end_arr[i] == m - 1:
            temp = SegTree_query(tree1, num1, segfunc, ide_ele, m, N)
            temp += beam[i][0] - beam[i][1]
            if temp <= 0:
                temp2 = abs(temp)
                B = beam[i][1]
                if B * ans[0] < ans[1] * temp2:
                    ans = [temp2, B]
        else:
            L, R = m, end_arr[i]
            temp = SegTree_query(tree2, num2, segfunc, ide_ele, L, R + 1) - beam[i][0]
            temp += beam[i][0] - beam[i][1]
            if temp <= 0:
                temp2 = abs(temp)
                B = beam[i][1]
                if B * ans[0] < ans[1] * temp2:
                    ans = [temp2, B]
            temp = SegTree_query(tree1, num1, segfunc, ide_ele, R + 1, N)
            temp += beam[i][0] - beam[i][1]
            if temp <= 0:
                temp2 = abs(temp)
                B = beam[i][1]
                if B * ans[0] < ans[1] * temp2:
                    ans = [temp2, B]
    for i in range(m, N):
        if beam[i][0] - beam[i][1] <= 0:
            if start_arr[i] == -1:
                temp = SegTree_query(tree1, num1, segfunc, ide_ele, i, N)
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp2 = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp2:
                        ans = [temp2, B]
            else:
                L = start_arr[i]
                R = end_arr[i]
                temp = SegTree_query(tree2, num2, segfunc, ide_ele, L, R + 1) - beam[i][0]
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp2 = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp2:
                        ans = [temp2, B]
                temp = SegTree_query(tree1, num1, segfunc, ide_ele, R + 1, N)
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp2 = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp2:
                        ans = [temp2, B]
        else:
            if start_arr[i] == -1:
                temp = SegTree_query(tree1, num1, segfunc, ide_ele, m - 1, N)
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp2 = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp2:
                        ans = [temp2, B]
            else:
                L = start_arr[i]
                R = end_arr[i]
                temp = SegTree_query(tree2, num2, segfunc, ide_ele, L, R + 1) - beam[i][0]
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp2 = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp2:
                        ans = [temp2, B]
                temp = min(SegTree_query(tree1, num1, segfunc, ide_ele, R + 1, N), SegTree_query(tree1, num1, segfunc, ide_ele, m - 1, L))
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp2 = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp2:
                        ans = [temp2, B]
else:
    for i in range(N):
        test = data[i]
        B = cummin[i]
        if test <= 0:
            t = abs(test)
            if B * ans[0] < ans[1] * t:
                ans = [t, B]
    M = min(data)
    for i in range(N):
        if beam[i][0] - beam[i][1] > 0:
            temp = M + beam[i][0] - beam[i][1]
            if temp <= 0:
                temp2 = abs(temp)
                B = beam[i][1]
                if B * ans[0] < ans[1] * temp2:
                    ans = [temp2, B]
p, q = ans
res = [q * m + p, N * q]
g = gcd(res[0], res[1])
print(res[0] // g, res[1] // g)