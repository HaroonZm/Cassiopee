n = input()
s = input().strip().split(" ")
q = int(input().strip())
t = input().strip().split(" ")

count = 0
for i in t:
    if i in s:
        count += 1
print(count)