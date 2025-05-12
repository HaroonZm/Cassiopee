from collections import defaultdict

MOD = 1000000007
n = int(input())
s = input()
t = input()
dic = defaultdict(int)
dic[s[0]] = 1
for cs, ct in zip(s[1:n-1], t[1:n-1]):
    dic[cs] += dic[ct]
    dic[cs] %= MOD
print(dic[t[-1]])