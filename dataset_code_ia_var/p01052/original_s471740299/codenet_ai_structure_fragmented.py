import sys
import heapq

INF = float('inf')
MOD = 10 ** 9 + 7

def read_int():
    return int(sys.stdin.readline())

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_matrix(n):
    return [read_int_list() for _ in range(n)]

def get_matrix_columns_first_row(matrix):
    for col in zip(*matrix):
        return set(col)

def sort_matrix(matrix):
    matrix.sort()
    return matrix

def should_process_new_start(i, start):
    return (i+1) in start

def index_valid(index, n):
    return index < n

def can_push_to_heap(i, start, mat_row):
    return (i+1) in start and mat_row[0] == i+1

def push_to_heap(hq, element):
    heapq.heappush(hq, element)

def pop_from_heap(hq):
    return heapq.heappop(hq)

def heap_top_is_less(hq, i):
    return hq and hq[0] < i+1

def add_reward(ans, value):
    return ans + value

def main():
    n = read_int()
    matrix = read_matrix(n)
    start = get_matrix_columns_first_row(matrix)
    matrix = sort_matrix(matrix)
    ans = 0
    index = 0
    hq = []
    for i in range(31):
        if should_process_new_start(i, start):
            while index_valid(index, n) and can_push_to_heap(i, start, matrix[index]):
                push_to_heap(hq, matrix[index][1])
                index += 1

        while heap_top_is_less(hq, i):
            if hq:
                pop_from_heap(hq)
            else:
                break

        if hq:
            ans = add_reward(ans, 100)
            pop_from_heap(hq)
        else:
            ans = add_reward(ans, 50)
    print(ans)

main()