from typing import List

if __name__ == "__main__":
    num_query = int(input())
    vector: List[int] = []
    for _ in range(num_query):
        op, *value = map(lambda x: int(x), input().split())
        if (0 == op):
            vector.append(value[0])
        elif (1 == op):
            print(f"{vector[value[0]]}")
        elif (2 == op):
            vector.pop()
        else:
            pass