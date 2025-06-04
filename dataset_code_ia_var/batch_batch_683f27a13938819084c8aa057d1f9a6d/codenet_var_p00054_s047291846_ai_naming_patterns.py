import sys

def process_input_lines(input_lines):
    for line in input_lines:
        val_a_str, val_b_str, val_n_str = line.strip().split()
        val_a = int(val_a_str)
        val_b = int(val_b_str)
        val_n = int(val_n_str)
        if val_a >= val_b:
            val_a = val_a % val_b
        val_a = val_a * 10
        result_sum = 0
        for _ in range(val_n):
            digit, val_a = divmod(val_a, val_b)
            result_sum += digit
            val_a = val_a * 10
        print(result_sum)

def main():
    input_lines = sys.stdin.readlines()
    process_input_lines(input_lines)

if __name__ == "__main__":
    main()