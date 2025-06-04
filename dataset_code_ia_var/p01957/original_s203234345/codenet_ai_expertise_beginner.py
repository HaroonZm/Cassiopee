import sys
from collections import defaultdict

def get_input_list():
    return list(map(int, sys.stdin.readline().split()))

def get_input_int():
    return int(sys.stdin.readline())

def get_input_str_list():
    return list(sys.stdin.readline().strip())

def main():
    def parse_winner(s, i):
        if s[i] == "[":
            i += 1
            w1, i = parse_winner(s, i)
            i += 1
            w2, i = parse_winner(s, i)
            winner = calc(w1, w2)
            return winner, i+1
        else:
            p, i = parse_person(s, i)
            return p, i

    def parse_person(s, i):
        return s[i], i+1

    def calc(w1, w2):
        if freq[w1] == 0:
            if freq[w2] == 0:
                return "0"
            else:
                freq[w2] -= 1
                return w2
        else:
            if freq[w2] != 0:
                return "0"
            else:
                freq[w1] -= 1
                return w1

    s = get_input_str_list()
    # count players (not '[' or ']')
    k = 0
    for c in s:
        if c not in ["[", "]"]:
            k += 1
    freq = defaultdict(int)
    freq["0"] = 100000
    for i in range(k):
        line = input().split()
        name = line[0]
        val = int(line[1])
        freq[name] = val
    w, _ = parse_winner(s, 0)
    if freq[w]:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()