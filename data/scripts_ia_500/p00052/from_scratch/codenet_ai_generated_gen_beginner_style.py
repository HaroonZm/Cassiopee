while True:
    n = int(input())
    if n == 0:
        break
    fact = 1
    for i in range(2, n+1):
        fact *= i
    fact_str = str(fact)
    count = 0
    for c in reversed(fact_str):
        if c == '0':
            count += 1
        else:
            break
    print(count)