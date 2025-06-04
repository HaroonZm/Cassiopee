H,W=[*map(int, input().split())]
A=list(map(str.__add__,['']*H,[input()for _ in' '*H]))
[print(line,end='\n'+line+'\n') for line in A]