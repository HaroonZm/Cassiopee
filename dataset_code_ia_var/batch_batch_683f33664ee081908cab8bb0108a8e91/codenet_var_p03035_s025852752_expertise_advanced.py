from sys import stdin

def calculate_fee(age: int, fee: int) -> int:
    return fee if age >= 13 else (fee // 2 if age >= 6 else 0)

if __name__ == "__main__":
    age, fee = map(int, stdin.readline().split())
    print(calculate_fee(age, fee))