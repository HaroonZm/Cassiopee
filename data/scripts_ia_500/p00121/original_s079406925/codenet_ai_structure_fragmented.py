from heapq import heappush, heappop

MOVE = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5],[1,4,6],[2,5,7],[3,6]]

def initialize_ans():
    return {"01234567": 0}

def convert_string_to_list(field):
    return list(field)

def swap_positions_in_list(tmp, a, b):
    tmp[a], tmp[b] = tmp[b], tmp[a]

def convert_list_to_string(tmp):
    return "".join(tmp)

def swap(field, a, b):
    tmp = convert_string_to_list(field)
    swap_positions_in_list(tmp, a, b)
    return convert_list_to_string(tmp)

def find_zero_position(field):
    return field.find("0")

def get_possible_moves(a):
    return MOVE[a]

def should_add_to_ans(tmp, ans):
    return tmp not in ans

def append_to_queue(q, g, tmp):
    q.append([g, tmp])

def pop_from_queue(q):
    return q.pop(0)

def bfs(ans):
    q = [[0, "01234567"]]
    while len(q) != 0:
        g, field = pop_from_queue(q)
        a = find_zero_position(field)
        moves = get_possible_moves(a)
        for b in moves:
            tmp = swap(field, a, b)
            if should_add_to_ans(tmp, ans):
                ans[tmp] = g + 1
                append_to_queue(q, g + 1, tmp)

def get_input():
    return raw_input()

def clean_input(user_input):
    return user_input.replace(" ", "")

def print_answer(ans, user_input):
    print ans[user_input]

def main():
    ans = initialize_ans()
    bfs(ans)
    while True:
        try:
            user_input = get_input()
            cleaned_input = clean_input(user_input)
            print_answer(ans, cleaned_input)
        except:
            break

main()