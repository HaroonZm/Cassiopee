n = input()
n = int(n)
string = input()
numbers = string.split(' ')
numbers = numbers[::-1]
_ = 0
while _ < n:
    print(numbers[_], end='')
    if _ != n - 1:
        print(' ', end='')
    _ += 1
print()