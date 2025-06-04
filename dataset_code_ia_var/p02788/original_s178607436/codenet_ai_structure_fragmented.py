import sys
from bisect import bisect_left

def get_input():
    return sys.stdin.read()

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 9)

def get_inf():
    return 1 << 60

def get_mod():
    return 1000000007

def parse_input_data(raw_data):
    data = list(map(int, raw_data.split()))
    N, D, A = data[0], data[1], data[2]
    XH = data[3:]
    return N, D, A, XH

def chunk_pairs(XH):
    length = len(XH)
    return [ (XH[i], XH[i+1]) for i in range(0, length, 2) ]

def ceil_division(h, A):
    return (h + A - 1) // A

def prepare_monster_list(XH_pairs, A, N):
    monster = [ None ] * N
    for i, (x, h) in enumerate(XH_pairs):
        monster[i] = (x, ceil_division(h, A))
    return monster

def sort_monsters(monster):
    monster.sort()
    return monster

def initialize_position_damage():
    return [], []

def initialize_indices():
    return 0, 0

def process_monsters(monster, D):
    pos, damage = initialize_position_damage()
    idx, cur_damage = initialize_indices()
    ans = 0
    for x, h in monster:
        idx, cur_damage = update_damage_index(pos, damage, idx, cur_damage, x)
        if needs_attack(h, cur_damage):
            attack_amt = h - cur_damage
            record_attack(pos, damage, x, D, attack_amt)
            ans, cur_damage = update_ans_cur_damage(ans, cur_damage, attack_amt)
    return ans

def update_damage_index(pos, damage, idx, cur_damage, x):
    while idx < len(pos) and pos[idx] < x:
        cur_damage -= damage[idx]
        idx += 1
    return idx, cur_damage

def needs_attack(h, cur_damage):
    return h > cur_damage

def record_attack(pos, damage, x, D, attack_amt):
    pos.append(x + 2 * D)
    damage.append(attack_amt)

def update_ans_cur_damage(ans, cur_damage, attack_amt):
    ans += attack_amt
    cur_damage += attack_amt
    return ans, cur_damage

def print_output(ans):
    print(ans)

def main():
    set_recursion_limit()
    INF = get_inf()
    MOD = get_mod()
    raw_data = get_input()
    N, D, A, XH = parse_input_data(raw_data)
    XH_pairs = chunk_pairs(XH)
    monster = prepare_monster_list(XH_pairs, A, N)
    monster = sort_monsters(monster)
    ans = process_monsters(monster, D)
    print_output(ans)

if __name__ == '__main__':
    main()