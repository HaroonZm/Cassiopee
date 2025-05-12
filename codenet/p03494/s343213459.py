_ = input()
a_list = list(map(int, input().split()))

can_devide = sum([a%2 for a in a_list])==0
count = 0
while can_devide:
    count += 1
    for i, a in enumerate(a_list):
        a_list[i] = a//2
        
    can_devide = sum([a%2 for a in a_list])==0

print(count)