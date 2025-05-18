from statistics import pstdev

while True:
    if input() == "0":
        break
    
    print(pstdev([int(i) for i in input().split()]))