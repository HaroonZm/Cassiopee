from typing import List

if __name__ == "__main__":
    num_query = int(input())
    vector: List[int] = []
    for _ in range(num_query):
        op, *value = map(lambda x: int(x), input().split())
        if op == 0:
            vector.append(value[0])
        elif op == 1:
            print(f"{vector[value[0]]}")
        elif op == 2:
            vector.pop()
        else:
            pass