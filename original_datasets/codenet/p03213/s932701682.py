def era(n):
    table = [0] * (n + 1)
    prime_list = []
    
    for i in range(2, n + 1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(2*i, n + 1, i):
                table[j] = 1
    
    return prime_list

def f(n):
    cnt = 0
    for i in data:
        if i[1] >= n-1:
            cnt += 1
    return cnt
 
N = int(input())
s = era(N)
data = []
 
for i in s:
    k = i
    c = 0
    while N // k >= 1:
        c += N // k
        k = k*i
 
    data.append([i,c])
 

print(f(75)+f(15)*(f(5)-1)+f(25)*(f(3)-1)+f(5)*(f(5)-1)*(f(3)-2)//2)