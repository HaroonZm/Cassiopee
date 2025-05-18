n = int(input())
s,t = map(str,input().split())
final_str = str()
for i in range(n):
    final_str += (s[i]+t[i])
print(final_str)