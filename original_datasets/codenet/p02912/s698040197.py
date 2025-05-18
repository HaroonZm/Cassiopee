#優先度付きキュー
import heapq

N, M = map(int, input().split())

#heapqは最小値しか取り出せないので全ての要素に-1をかける
A = list(map(lambda x: int(x)*(-1), input().split()))
# print(A)

#リストを優先度付きキューに入れる
heapq.heapify(A)

for _ in range(M):
    num = heapq.heappop(A)
    # print(num >> 1)
    heapq.heappush(A, (-num)//2*(-1))
print(sum(A)*(-1))