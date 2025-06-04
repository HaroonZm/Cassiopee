def get_initial_end():
    return 0

def get_initial_ans():
    return [0]

def extend_ans_if_needed(ans, end):
    if end >= len(ans):
        ans.append(0)
    return ans

def set_ans_value(ans, end, x):
    ans[end] = x
    return ans

def increase_end(end):
    return end + 1

def pushBack(x, end, ans):
    ans = set_ans_value(ans, end, x)
    end = increase_end(end)
    ans = extend_ans_if_needed(ans, end)
    return end, ans

def parse_position(p):
    return int(p)

def print_ans_at_p(ans, p):
    print(ans[parse_position(p)])

def randomAccess(p, ans):
    print_ans_at_p(ans, p)

def decrease_end(end):
    return end - 1

def popBack(end):
    end = decrease_end(end)
    return end

def to_int(s):
    return int(s)

def get_query():
    return list(input().split())

def is_push(query):
    return query[0] == "0"

def is_random_access(query):
    return query[0] == "1"

def handle_push(query, end, ans):
    x = query[1]
    end, ans = pushBack(x, end, ans)
    return end, ans

def handle_random_access(query, ans):
    p = query[1]
    randomAccess(p, ans)

def handle_pop_back(end):
    end = popBack(end)
    return end

def process_query(query, end, ans):
    if is_push(query):
        end, ans = handle_push(query, end, ans)
    elif is_random_access(query):
        handle_random_access(query, ans)
    else:
        end = handle_pop_back(end)
    return end, ans

def main_loop(q, end, ans):
    for i in range(q):
        query = get_query()
        end, ans = process_query(query, end, ans)
    return end, ans

def main():
    end = get_initial_end()
    ans = get_initial_ans()
    q = to_int(input())
    main_loop(q, end, ans)

main()