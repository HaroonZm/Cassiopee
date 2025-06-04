def get_N_M():
    return map(int, input().split())

def initialize_flag_list(size):
    return [False] * size

def read_event():
    return int(input())

def append_event(aft, e):
    aft.append(e)
    return aft

def mark_list_flag(lis, e):
    lis[e - 1] = True
    return lis

def reverse_list(lis):
    lis.reverse()
    return lis

def print_event(i):
    print(i)

def mark_end_flag(end, i):
    end[i - 1] = True
    return end

def is_event_end_false(end, i):
    return not end[i - 1]

def is_event_list_false(lis, i):
    return not lis[i]

def main():
    N, M = get_N_M()
    lis = initialize_flag_list(N)
    end = initialize_flag_list(N)
    aft = []
    for _ in range(M):
        e = read_event()
        aft = append_event(aft, e)
        lis = mark_list_flag(lis, e)
    aft = reverse_list(aft)
    for i in aft:
        if is_event_end_false(end, i):
            print_event(i)
            end = mark_end_flag(end, i)
    for i in range(N):
        if is_event_list_false(lis, i):
            print_event(i + 1)

main()