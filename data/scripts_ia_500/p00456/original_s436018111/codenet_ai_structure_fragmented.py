def read_ten_numbers():
    numbers = []
    for _ in range(10):
        num = int(input())
        numbers.append(num)
    return numbers

def sort_numbers(numbers):
    numbers.sort()
    return numbers

def get_top_three_sum(numbers):
    return numbers[9] + numbers[8] + numbers[7]

def main():
    dataW = read_ten_numbers()
    dataW = sort_numbers(dataW)
    pointW = get_top_three_sum(dataW)
    
    dataK = read_ten_numbers()
    dataK = sort_numbers(dataK)
    pointK = get_top_three_sum(dataK)
    
    print(pointW, pointK)

main()