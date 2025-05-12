#92

li = [int(input().rstrip()) for x in range(4)]

print(min(li[0]+li[2], li[0]+li[3], li[1]+li[2], li[1]+li[3]))