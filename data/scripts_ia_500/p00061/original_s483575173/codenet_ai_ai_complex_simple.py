from functools import reduce
import sys

def fancy_input():
    return tuple(map(int, reduce(lambda a,b: a+b, [c.split(',') for c in sys.stdin.read().splitlines()])))

def ranker(results):
    keys_sorted = sorted(results.keys(), key=lambda x: results[x], reverse=True)
    ranks = {}
    def rank_acc(acc, k):
        rank, last_val, seen = acc
        current = results[k]
        new_rank = rank + (1 if last_val > current else 0)
        ranks[k] = new_rank
        return (new_rank, current, seen+1)
    reduce(rank_acc, keys_sorted, (1, float('inf'), 0))
    return ranks

def main():
    data = []
    for line in iter(sys.stdin.readline, ''):
        if line.strip() == '':
            break
        try:
            a,b = tuple(map(int, line.strip().split(',')))
            if a == 0 and b == 0:
                break
            data.append((a,b))
        except:
            break

    result = {k:v for k,v in data}
    ranks = ranker(result)

    # Create line iterator from stdin after previous input block
    lines = iter(sys.stdin.readline, '')
    try:
        while True:
            num_line = next(lines)
            num = int(num_line.strip())
            print(ranks[num])
    except StopIteration:
        pass

if __name__ == '__main__':
    main()