import sys

def process():
    while True:
        try:
            line = input() if sys.version_info[0] > 2 else raw_input()
            n, k = (int(x) for x in line.strip().split())
            if n == 0 and k == 0:
                break

            if sys.version_info[0] > 2:
                fridge = list(map(int, input().split()))
            else:
                fridge = map(int, raw_input().split())

            status = False
            idx = 0
            while idx < n:
                if sys.version_info[0] > 2:
                    uses = [int(x) for x in input().split()]
                else:
                    uses = map(int, raw_input().split())
                for x in range(k):
                    fridge[x] = fridge[x] - uses[x]
                    if fridge[x] < 0:
                        status = True
                idx += 1
            if status: print("No") if sys.version_info[0] > 2 else sys.stdout.write("No\n")
            else: exec('print("Yes")' if sys.version_info[0] > 2 else 'print "Yes"')
        except EOFError:
            break

process()