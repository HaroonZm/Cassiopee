s=int(input())
pattern=[]
for i in range(1,61):
    if i%15==0: pattern.append("FizzBuzz")
    elif i%3==0: pattern.append("Fizz")
    elif i%5==0: pattern.append("Buzz")
    else: pattern.append(str(i))
pattern_str="".join(pattern)
len_pattern=len(pattern_str)
res=[]
for i in range(s,s+20):
    pos=(i-1)%len_pattern
    res.append(pattern_str[pos])
print("".join(res))