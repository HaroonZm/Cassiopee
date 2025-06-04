def read_dimensions():
    return map(int, input().split())

def create_empty_field(size):
    return [[] for _ in range(size)]

def read_row():
    return list(map(int, input().split()))

def fill_field_row(field, x, i, w):
    for j in range(w):
        set_field(field, x[j], i, j)

def set_field(field, num, i, j):
    field[num-1] = [i, j]

def fill_field(h, w, field):
    for i in range(h):
        x = read_row()
        fill_field_row(field, x, i, w)

def init_dis(size):
    return [10**20] * size

def set_dis_zero(dis, d):
    for i in range(d):
        dis[i] = 0

def compute_index(i, d):
    return i - d

def pos(field, idx):
    return field[idx]

def update_dis_value(dis, i, d, field):
    prev = compute_index(i, d)
    dis[i] = dis[prev] + abs(pos(field, i)[0] - pos(field, prev)[0]) + abs(pos(field, i)[1] - pos(field, prev)[1])

def fill_dis_field(dis, h, w, d, field):
    for i in range(h * w):
        if i >= d:
            update_dis_value(dis, i, d, field)

def read_query():
    return map(int, input().split())

def process_query(dis, l, r):
    print(dis[r-1] - dis[l-1])

def process_queries(q, dis):
    for _ in range(q):
        l, r = read_query()
        process_query(dis, l, r)

def main():
    h, w, d = read_dimensions()
    field = create_empty_field(h*w)
    fill_field(h, w, field)
    dis = init_dis(h*w)
    set_dis_zero(dis, d)
    fill_dis_field(dis, h, w, d, field)
    q = int(input())
    process_queries(q, dis)

main()