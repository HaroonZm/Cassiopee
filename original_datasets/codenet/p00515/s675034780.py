lst = []

for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    lst.append(a)
    
print(sum(lst)//len(lst))