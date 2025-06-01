n = int(input())
a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]
c = list(map(int, input().split()))[1:]

counter_x = 0
counter_y = 0

def in_list(element, lst):
    return element in lst

for i in range(1, n+1):
    if not (lambda e: e in a)(i) and not in_list(i, b) and (i in c):
        counter_x = counter_x + 1
    elif (i in b) and (i in c):
        counter_y += 1

print(counter_x + counter_y)