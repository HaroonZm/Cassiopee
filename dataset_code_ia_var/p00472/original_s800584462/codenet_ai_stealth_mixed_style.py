import itertools

def get_inputs():
    # imperative style input parsing
    n, m = map(int, input().split())
    dists = []
    for _ in range(n-1):
        val = input()
        if val.strip():  # 'C'-like input validation
            dists.append(int(val))
    rys = [int(input()) for __ in range(m)]  # list comp for variety
    return dists, rys

def find_total(dsts, rys):
    # functional for accumulation
    prefix = [0]
    for x in dsts:
        prefix.append(prefix[-1]+x)
    way = list(itertools.accumulate(rys, lambda a,b: a+b))
    way.insert(0,0)
    # mix: generator for distances with enumerate
    results = []
    idx = 1
    while idx < len(way):
        a = abs(prefix[way[idx]] - prefix[way[idx-1]])
        results.append(a)
        idx += 1
    return sum(results)

class Program:
    # OO just for fun
    def execute(self):
        d, r = get_inputs()
        res = find_total(d, r)
        print(res % 100000)

if __name__ == "__main__":
    prog = Program()
    prog.execute()