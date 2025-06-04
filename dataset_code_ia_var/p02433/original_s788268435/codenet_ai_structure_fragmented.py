import collections

def create_cursor_list():
    return {'vector': create_deque(), 'cursor': 0}

def create_deque():
    return collections.deque()

def insert_element(cursor_list, x):
    append_left(cursor_list['vector'], x)
    return cursor_list

def append_left(deq, x):
    deq.appendleft(x)

def move_cursor(cursor_list, d):
    rotate_vector(cursor_list['vector'], -d)
    update_cursor(cursor_list, d)
    return cursor_list

def rotate_vector(deq, steps):
    deq.rotate(steps)

def update_cursor(cursor_list, d):
    cursor_list['cursor'] += d

def erase_element(cursor_list):
    popleft_vector(cursor_list['vector'])
    return cursor_list

def popleft_vector(deq):
    deq.popleft()

def parse_input():
    return int(input())

def parse_queue():
    return tuple(map(int, input().split(' ')))

def process_queries(num_queue, cursor_list):
    for _ in range(num_queue):
        queue = parse_queue()
        handle_queue(cursor_list, queue)

def handle_queue(cursor_list, queue):
    if queue[0] == 0:
        insert_element(cursor_list, queue[1])
    elif queue[0] == 1:
        move_cursor(cursor_list, queue[1])
    elif queue[0] == 2:
        erase_element(cursor_list)

def final_rotate(cursor_list):
    rotate_vector(cursor_list['vector'], cursor_list['cursor'])

def print_vector(cursor_list):
    for item in cursor_list['vector']:
        print(str(item))

def main():
    num_queue = parse_input()
    cursor_list = create_cursor_list()
    process_queries(num_queue, cursor_list)
    final_rotate(cursor_list)
    print_vector(cursor_list)

main()