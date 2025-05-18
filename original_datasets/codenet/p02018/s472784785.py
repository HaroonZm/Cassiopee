_ = input()
A = map(int, input().split())

print(len([x for x in A if x % 2 == 0]))