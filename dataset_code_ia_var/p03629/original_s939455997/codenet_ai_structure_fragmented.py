from collections import deque
from sys import exit

def read_input():
    return input()

def char_to_index_list(s):
    return [ord(c) - ord('a') for c in s]

def get_len(s):
    return len(s)

def initialize_pos_chars(length):
    return [length] * 26

def initialize_pos_nexts(length):
    return [[] for _ in range(length + 1)]

def build_pos_nexts(As, lenA):
    posChars = initialize_pos_chars(lenA)
    posNexts = initialize_pos_nexts(lenA)
    fill_reversed_pos_nexts(As, lenA, posChars, posNexts)
    posNexts[0] = posChars.copy()
    return posNexts

def fill_reversed_pos_nexts(As, lenA, posChars, posNexts):
    for i in reversed(range(lenA)):
        posNexts[i + 1] = posChars.copy()
        update_posChars(posChars, As[i], i)

def update_posChars(posChars, ch_idx, i):
    posChars[ch_idx] = i

def initialize_prevs(lenA):
    return [None] * lenA

def create_queue():
    return deque()

def enqueue_initial(Q):
    Q.append((0, -1))

def bfs(Q, posNexts, lenA, As, prevs):
    while not_empty(Q):
        lenAns, pos = dequeue(Q)
        handle_children(Q, posNexts, lenA, As, prevs, lenAns, pos)

def not_empty(Q):
    return bool(Q)

def dequeue(Q):
    return Q.popleft()

def handle_children(Q, posNexts, lenA, As, prevs, lenAns, pos):
    for ch in range(26):
        handle_single_child(Q, posNexts, lenA, As, prevs, lenAns, pos, ch)

def handle_single_child(Q, posNexts, lenA, As, prevs, lenAns, pos, ch):
    posNext = posNexts[pos + 1][ch]
    if is_end(posNext, lenA):
        process_answer_and_exit(As, ch, pos, prevs)
    if is_new_path(prevs, posNext):
        prevs[posNext] = pos
        Q.append((lenAns + 1, posNext))

def is_end(posNext, lenA):
    return posNext == lenA

def process_answer_and_exit(As, ch, pos, prevs):
    ans = [char_from_index(ch)]
    build_path(ans, As, pos, prevs)
    print_answer(ans)
    do_exit()

def char_from_index(ch):
    return chr(ord('a') + ch)

def build_path(ans, As, pos, prevs):
    while pos != -1:
        ans.append(char_from_index(As[pos]))
        pos = prevs[pos]

def print_answer(ans):
    print(''.join(reversed(ans)))

def do_exit():
    exit()

def is_new_path(prevs, posNext):
    return prevs[posNext] is None

def main():
    As = read_input()
    As = char_to_index_list(As)
    lenA = get_len(As)
    posNexts = build_pos_nexts(As, lenA)
    prevs = initialize_prevs(lenA)
    Q = create_queue()
    enqueue_initial(Q)
    bfs(Q, posNexts, lenA, As, prevs)

main()