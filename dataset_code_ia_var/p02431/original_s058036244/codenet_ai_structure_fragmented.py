from typing import List

def get_num_query() -> int:
    return int(input())

def get_operation() -> List[int]:
    return list(map(int, input().split()))

def process_insert(vector: List[int], value: int) -> None:
    vector.append(value)

def process_print(vector: List[int], index: int) -> None:
    print(f"{vector[index]}")

def process_pop(vector: List[int]) -> None:
    vector.pop()

def handle_operation(op: int, value: List[int], vector: List[int]) -> None:
    if op == 0:
        handle_insert_op(value, vector)
    elif op == 1:
        handle_print_op(value, vector)
    elif op == 2:
        handle_pop_op(vector)
    else:
        handle_unknown_op()

def handle_insert_op(value: List[int], vector: List[int]) -> None:
    insert_value(value, vector)

def insert_value(value: List[int], vector: List[int]) -> None:
    process_insert(vector, value[0])

def handle_print_op(value: List[int], vector: List[int]) -> None:
    print_value(value, vector)

def print_value(value: List[int], vector: List[int]) -> None:
    process_print(vector, value[0])

def handle_pop_op(vector: List[int]) -> None:
    pop_element(vector)

def pop_element(vector: List[int]) -> None:
    process_pop(vector)

def handle_unknown_op() -> None:
    pass

def process_queries(num_query: int, vector: List[int]) -> None:
    for _ in range(num_query):
        op, *value = get_operation()
        handle_operation(op, value, vector)

def main():
    num_query = get_num_query()
    vector: List[int] = []
    process_queries(num_query, vector)

if __name__ == "__main__":
    main()