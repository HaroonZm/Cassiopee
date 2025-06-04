import queue

def get_directions():
    return [0,1,0,-1], [1,0,-1,0]

def read_hw():
    return map(int, input().split())

def read_field(h):
    return [input() for _ in range(h)]

def create_distance_matrix(h, w, value):
    return [[value]*w for _ in range(h)]

def find_positions(field, h, w):
    positions = {
        '@': None,
        '$': [],
        '%': None,
    }
    for i, row in enumerate(field):
        for j in range(w):
            char = row[j]
            if char == '@':
                positions['@'] = (i, j)
            if char == '$':
                positions['$'].append((i,j))
            if char == '%':
                positions['%'] = (i, j)
    return positions

def initialize_queues_positions(field, h, w, pdist, sdist):
    pque = queue.Queue()
    sque = queue.Queue()
    pi, pj, gi, gj = None, None, None, None
    for i, row in enumerate(field):
        for j in range(w):
            if row[j] == '@':
                pque.put((i, j))
                pdist[i][j] = 0
                pi, pj = i, j
            if row[j] == '$':
                sque.put((i, j))
                sdist[i][j] = 0
            if row[j] == '%':
                gi, gj = i, j
    return pque, sque, pi, pj, gi, gj

def is_in_bounds(i, j, h, w):
    return 0 <= i < h and 0 <= j < w

def should_update_sdist(field, ni, nj, sdist, i, j):
    return field[ni][nj] != '#' and sdist[ni][nj] > sdist[i][j] + 1

def should_update_pdist(field, ni, nj, pdist, sdist, i, j):
    return field[ni][nj] != '#' and pdist[ni][nj] > pdist[i][j] + 1 and pdist[i][j]+1 < sdist[ni][nj]

def process_sdist_queue(sque, sdist, field, di, dj, h, w):
    def process_neighbor(i, j, k):
        ni = i + di[k]
        nj = j + dj[k]
        if is_in_bounds(ni, nj, h, w):
            if should_update_sdist(field, ni, nj, sdist, i, j):
                sdist[ni][nj] = sdist[i][j] + 1
                sque.put((ni, nj))
    while not sque.empty():
        i, j = sque.get()
        for k in range(4):
            process_neighbor(i, j, k)

def process_pdist_queue(pque, pdist, sdist, field, di, dj, h, w):
    def process_neighbor(i, j, k):
        ni = i + di[k]
        nj = j + dj[k]
        if is_in_bounds(ni, nj, h, w):
            if should_update_pdist(field, ni, nj, pdist, sdist, i, j):
                pdist[ni][nj] = pdist[i][j] + 1
                pque.put((ni, nj))
    while not pque.empty():
        i, j = pque.get()
        for k in range(4):
            process_neighbor(i, j, k)

def check_result(pdist, gi, gj):
    if pdist[gi][gj] < 1000:
        print("Yes")
    else:
        print("No")

def main():
    di, dj = get_directions()
    h, w = read_hw()
    field = read_field(h)
    pdist = create_distance_matrix(h, w, 1000)
    sdist = create_distance_matrix(h, w, 1000)
    pque, sque, pi, pj, gi, gj = initialize_queues_positions(field, h, w, pdist, sdist)
    process_sdist_queue(sque, sdist, field, di, dj, h, w)
    process_pdist_queue(pque, pdist, sdist, field, di, dj, h, w)
    check_result(pdist, gi, gj)

main()