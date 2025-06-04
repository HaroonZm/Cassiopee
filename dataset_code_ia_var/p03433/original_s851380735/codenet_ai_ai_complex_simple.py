n = int(input())
a = int(input())
print(next((s for c, s in zip([n % 500 <= a], ('Yes', 'No')) if c), 'No'))