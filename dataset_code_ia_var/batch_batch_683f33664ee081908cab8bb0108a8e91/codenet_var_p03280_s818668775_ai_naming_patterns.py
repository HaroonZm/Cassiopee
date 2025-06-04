read_int = lambda: int(input())
read_ints = lambda: map(int, input().split())
read_strs = lambda: map(str, input().split())
read_str = lambda: str(input())
read_int_list = lambda: list(map(int, input().split()))
read_str_list = lambda: list(map(str, input().split()))

def main_process():
    int_a, int_b = read_ints()
    result = int_a * int_b - (int_a + int_b - 1)
    print(result)

if __name__ == '__main__':
    main_process()