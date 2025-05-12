n = input()
n = int(n)
string = input()
numbers = string.split(' ')
numbers.reverse()
for _ in range(n):
    print(numbers[_], end='')
    if _ != n - 1:
        print(' ', end='')
print()