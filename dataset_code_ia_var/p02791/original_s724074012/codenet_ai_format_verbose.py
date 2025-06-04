from sys import stdin

def main():

    number_of_prices_input = input()
    price_list = [int(price_string) for price_string in stdin.readline().rstrip().split()]

    current_minimum_price = price_list[0]
    num_prices_at_or_below_min = 0

    for price in price_list:

        if price <= current_minimum_price:

            num_prices_at_or_below_min += 1
            current_minimum_price = price

        else:

            pass

    print(num_prices_at_or_below_min)

if __name__ == "__main__":

    main()