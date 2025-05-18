a=0
for i in range(5):
    b=int(input())
    if b<40:
        b=40
    a+=b
    
print(a//5)