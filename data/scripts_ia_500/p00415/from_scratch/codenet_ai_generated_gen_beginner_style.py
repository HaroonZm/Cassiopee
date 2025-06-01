N,K = map(int, input().split())
a = list(map(int, input().split()))

stack = []
to_remove = K

for num in a:
    while to_remove > 0 and stack and stack[-1] < num:
        stack.pop()
        to_remove -= 1
    stack.append(num)

# If still need to remove numbers
while to_remove > 0:
    stack.pop()
    to_remove -= 1

result = ''.join(map(str, stack))
print(result)