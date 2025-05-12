while True:
    n = str(input())
    if n[0] == '0':
        break
    print(sum(int(num) for num in n))