def main():
    finished = False
    while not finished:
        try:
            l = raw_input().split() if 'raw_input' in globals() else input().split()
            n = int(l[0])
            k = int(l[1])
            if not n:
                finished = True
                continue
            data = [0]
            data.extend([int(x) for x in (input().split())])
            valid = 1
            for q in range(n):
                row = list(map(int, input().split()))
                idx = 1
                while idx <= k:
                    data[idx] -= row[idx-1]
                    if data[idx]<0:
                        valid = 0
                        break
                    idx += 1
                if not valid:
                    break
            res = "No"
            if valid: res = "Yes"
            print(res)
        except EOFError:
            break
main()