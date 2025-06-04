Characters = __import__('sys').stdin.read().strip()
Frequencies={chr(97+i):0 for i in range(26)}
for symbol in Characters: Frequencies[symbol]+=1
result=sum([1 for x in Frequencies.values() if x%2])
del Characters, symbol, x
def halver(n): return n//2
res=halver(result)
print(res)