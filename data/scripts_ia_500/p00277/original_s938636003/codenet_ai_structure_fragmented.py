import sys
from heapq import heappush, heappop, heapreplace

def read_initial_parameters(file_input):
    return map(int, file_input.readline().split())

def initialize_priority_queue(N):
    return [[0, i, 0] for i in range(1, N + 1)]

def build_team_map(pq, N):
    return dict(zip(range(1, N + 1), pq))

def parse_line(line):
    return map(int, line.split())

def update_team_time(team, current_time, previous_time):
    team[2] += current_time - previous_time

def adjust_score_for_current_team(team, x):
    team[0] -= x

def replace_team_in_heap(pq, team, x):
    if x < 0:
        heapreplace(pq, team)

def duplicate_team_entry(team):
    return team[:]

def update_scored_team_and_push(pq, m, d, x):
    scored_team = duplicate_team_entry(m[d])
    scored_team[0] -= x
    heappush(pq, scored_team)
    m[d][2] = -1
    m[d] = scored_team

def pop_invalid_teams(pq):
    while pq[0][2] == -1:
        heappop(pq)

def update_final_team_time(pq, L, pre_t):
    pq[0][2] += L - pre_t

def find_answer_team(pq):
    return max(pq, key=lambda x: (x[2], -x[1]))

def print_answer(ans_team):
    print(ans_team[1])

def solve():
    file_input = sys.stdin
    N, R, L = read_initial_parameters(file_input)
    
    pq = initialize_priority_queue(N)
    m = build_team_map(pq, N)
    
    pre_t = 0
    for line in file_input:
        d, t, x = parse_line(line)
        
        team = pq[0]
        update_team_time(team, t, pre_t)
        pre_t = t
        
        if team[1] == d:
            adjust_score_for_current_team(team, x)
            replace_team_in_heap(pq, team, x)
        else:
            update_scored_team_and_push(pq, m, d, x)
        
        pop_invalid_teams(pq)
    
    update_final_team_time(pq, L, pre_t)
    ans_team = find_answer_team(pq)
    print_answer(ans_team)

solve()