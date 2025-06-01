def two(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return three(n)
    else:
        q = n // 2
        return two(q)

def three(n):
    if n == 1:
        return True
    if n % 3 != 0:
        return five(n)
    else:
        q = int(n / 3)
        return three(q)

def five(n):
    if n == 1:
        return True
    if n % 5 != 0:
        return False
    else:
        q = n / 5
        return two(int(q))

def main():
    while True:
        try:
            input_line = input()
        except EOFError:
            break
        if input_line == '0':
            break
        m, n = [int(x) for x in input_line.split()]
        count = 0
        for num in range(m, n + 1):
            if two(num) == True:
                count += 1
        else:
            print(count)

if __name__ == "__main__":
    main()