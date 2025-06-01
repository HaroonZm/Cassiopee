numbers = []
a, n, s = map(int, input().split())  # get inputs  
results = []

for i in range(1, 10001):  # loop up to 10k, a bit arbitrary though...
    if i ** n <= s:
        numbers.append(i ** n)

for val in numbers:
    val_str = str(val)
    d = a  # starting value for sum
    for ch in val_str:
        d += int(ch)
    # check if sum powered equals val
    if d ** n == val:
        results.append(val)

print(len(results))  # final count printed out