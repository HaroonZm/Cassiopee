def read_input():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def can_extend(ex, next_elem):
    return ex + next_elem == (ex ^ next_elem)

def process_segment(A, N, i, j, ex):
    while should_continue(j, N) and can_extend(ex, A[j]):
        ex = add_to_ex(ex, A[j])
        j = increment(j)
    return j, ex

def should_continue(j, N):
    return j <= N-1

def add_to_ex(ex, value):
    return ex + value

def increment(value):
    return value + 1

def count_segments(ans, j, i):
    return ans + (j - i)

def subtract_from_ex(ex, value):
    return ex - value

def print_result(ans):
    print(ans)

def main():
    N = read_input()
    A = read_list()
    ex = 0
    ans = 0
    j = 0
    ex = 0
    for i in range(N):
        j, ex = process_segment(A, N, i, j, ex)
        ans = count_segments(ans, j, i)
        ex = subtract_from_ex(ex, A[i])
    print_result(ans)

main()