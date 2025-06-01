from __future__ import print_function
def main():
    while True:
        a_b = raw_input()
        if a_b == '0 0':
            return
        a,b = [int(x) for x in a_b.split()]
        tally = {}
        for _ in range(a):
            line = raw_input().split()
            for idx in range(b):
                if idx not in tally:
                    tally[idx] = 0
                tally[idx] += int(line[idx])
        sorted_items = sorted(tally.iteritems(), key=lambda (k,v): v, reverse=True)
        for key, _ in sorted_items:
            print(key+1,),
        print()
if __name__ == "__main__":
    main()