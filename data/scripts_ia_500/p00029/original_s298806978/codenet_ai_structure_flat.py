s=input().split()
max_count=s[0]
max_len=s[0]
for w in s:
 if s.count(w)>s.count(max_count):
  max_count=w
 if len(w)>len(max_len):
  max_len=w
print(max_count,max_len)