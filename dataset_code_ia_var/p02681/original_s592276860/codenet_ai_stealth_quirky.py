from sys import stdin

response = 'Yes'
a = list(map(str, stdin.readline().strip()))
b = list(map(str, stdin.readline().strip()))

try:
    for x, y in zip(a, b):
        if x != y:
            response = 'No'
            raise StopIteration
except StopIteration:
    pass

print(response)