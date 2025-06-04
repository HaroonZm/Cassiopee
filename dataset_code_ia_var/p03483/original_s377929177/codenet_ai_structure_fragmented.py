from collections import Counter

def read_input():
    return input()

def get_string_length(S):
    return len(S)

def count_characters(S):
    return Counter(S)

def check_palindrome_possible(apperance):
    flag = False
    odd_char = None
    for k, v in apperance.items():
        if v % 2 == 1:
            if flag:
                return (False, None)
            else:
                flag = True
                odd_char = k
    return (True, odd_char)

def collect_character_positions(S):
    place = {}
    for i, s in enumerate(S):
        if s not in place:
            place[s] = []
        place[s].append(i)
    return place

def create_empty_memo(N):
    return [-1] * N

def allocate_indices(S, N, apperance, place):
    memo = create_empty_memo(N)
    tmp = 0
    tmpApperance = {}
    for i in range(N):
        s = S[i]
        if s not in tmpApperance:
            tmpApperance[s] = 1
        else:
            tmpApperance[s] += 1
        if tmpApperance[s] <= apperance[s] // 2:
            memo[i] = tmp
            backIdx = place[s][-tmpApperance[s]]
            memo[backIdx] = N - tmp - 1
            tmp += 1
    return memo

def assign_middle_character(flag, memo, place, t, N):
    if flag:
        idx = N // 2
        memo[place[t][len(place[t]) // 2]] = idx

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i):
        return self._sum_internal(i)
    def add(self, i, x):
        self._add_internal(i, x)
    def _sum_internal(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def _add_internal(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def count_swaps(N, memo):
    bit = BIT(N)
    cnt = 0
    for i in range(N):
        m = memo[i] + 1
        bit.add(m, 1)
        cnt += bit.sum(N) - bit.sum(m)
    return cnt

def not_palindrome_output():
    print(-1)

def final_output(cnt):
    print(cnt)

def main():
    S = read_input()
    N = get_string_length(S)
    apperance = count_characters(S)
    palindrome_possible, odd_char = check_palindrome_possible(apperance)
    if not palindrome_possible:
        not_palindrome_output()
        return
    place = collect_character_positions(S)
    memo = allocate_indices(S, N, apperance, place)
    assign_middle_character(odd_char is not None, memo, place, odd_char, N)
    cnt = count_swaps(N, memo)
    final_output(cnt)

main()