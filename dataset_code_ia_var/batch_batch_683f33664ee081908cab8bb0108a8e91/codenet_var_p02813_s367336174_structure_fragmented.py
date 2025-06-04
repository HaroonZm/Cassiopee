import math

def read_input():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    return n, p, q

def precompute_factorials(n):
    facts = [1] * (n+1)
    for i in range(1, n+1):
        facts[i] = facts[i-1] * i
    return facts

def decrement_n_for_lessers(seq, cur_val, up_to_index):
    count = 0
    for j in range(up_to_index):
        if seq[j] < cur_val:
            count += 1
    return count

def term_for_position(val, lessers, remaining, facts):
    return (val - 1 - lessers) * facts[remaining]

def sequence_order(n, seq, facts):
    total = 0
    for i in range(n):
        val = seq[i]
        lessers = decrement_n_for_lessers(seq, val, i)
        remaining = n - (i + 1)
        total += term_for_position(val, lessers, remaining, facts)
    return total

def compute_difference(n, p, q):
    facts = precompute_factorials(n)
    ord_p = sequence_order(n, p, facts)
    ord_q = sequence_order(n, q, facts)
    return abs(ord_p - ord_q)

def main():
    n, p, q = read_input()
    diff = compute_difference(n, p, q)
    print(diff)

main()