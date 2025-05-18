#binary_search
from bisect import bisect_left
from bisect import bisect_right
#input
N = int(input())
A = sorted(list(map(int, input().split()))) 
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    ab = bisect_left(A,B[i])
    bc = N-bisect_right(C,B[i])
    #print(ab, end='  ')
    #print(bc)
    ans += ab*bc
print(ans)

'''
A ●  ○  ○  ○  ○  ○ << ab
    ^ bisec_left(A,B[i])

B ○  ○  #  ○  ○  ○  << # = B[i]

C ○  ○  ○  ●  ●  ●  << bc
          ^ bisec_right(C,B[i])

ab * bc が i のときの組み合わせの数になる
'''