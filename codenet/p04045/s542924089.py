def check(price, disabled_digits):
    price = int(price)
    disabled_digits = set(disabled_digits)
    while not set(str(price)).isdisjoint(disabled_digits):
        price += 1
    return price

def main():
    price, k = input().split()
    disabled_digits = input().split()
    print(check(price, disabled_digits))

if __name__ == '__main__':
    main()