def delete_first_element(p):
    del p[0]

def current_element(p):
    return p[0]

def has_left_child(p):
    return current_element(p) != ','

def has_right_child(p):
    return current_element(p) != ')'

def assign_left_child(i):
    global sz
    if node[i][0] == 0:
        node[i][0] = sz
        sz_increment()

def assign_right_child(i):
    global sz
    if node[i][1] == 0:
        node[i][1] = sz
        sz_increment()

def sz_increment():
    global sz
    sz += 1

def increment_parsing_counter(i):
    node[i][2] += 1

def parse_left_subtree(p, i):
    assign_left_child(i)
    parse(p, node[i][0])

def parse_right_subtree(p, i):
    assign_right_child(i)
    parse(p, node[i][1])

def parse(p, i):
    increment_parsing_counter(i)
    delete_first_element(p)
    if has_left_child(p):
        parse_left_subtree(p, i)
    delete_first_element(p)
    if has_right_child(p):
        parse_right_subtree(p, i)
    delete_first_element(p)

def act(i, k):
    global ans
    if node[i][2] < k:
        return
    append_opening_paren()
    process_left_child(i, k)
    append_comma()
    process_right_child(i, k)
    append_closing_paren()

def append_opening_paren():
    global ans
    ans += '('

def append_comma():
    global ans
    ans += ','

def append_closing_paren():
    global ans
    ans += ')'

def process_left_child(i, k):
    if node[i][0] > 0:
        act(node[i][0], k)

def process_right_child(i, k):
    if node[i][1] > 0:
        act(node[i][1], k)

def initialize_node():
    return [[0 for _ in range(3)] for _ in range(210)]

while True:
    try:
        line = input()
        if not line:
            break
        op, a, b = line.split()
    except:
        break
    sz = 1
    node = initialize_node()
    parse(list(a), 0)
    parse(list(b), 0)
    ans = ''
    act(0, 2 if op == 'i' else 1)
    print(ans)