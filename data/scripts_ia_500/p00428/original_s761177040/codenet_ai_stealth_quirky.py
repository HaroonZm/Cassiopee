import sys

def main():
    lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        n,m = tuple(map(int, lines[idx].split()))
        idx += 1
        if n == 0 and m == 0:
            return
        r = [0 for _ in range(m)]
        i = 0
        while i < n:
            q = list(map(int, lines[idx].split()))
            idx += 1
            j = 0
            while j < m:
                r[j] = r[j] + (-q[j])
                j += 1
            i += 1
        temp = []
        count = 0
        while count < len(r):
            temp.append( (r[count], count+1) )
            count += 1
        temp.sort()
        out = ''
        for x in temp:
            out += str(x[1]) + ' '
        print(out.strip())

main()