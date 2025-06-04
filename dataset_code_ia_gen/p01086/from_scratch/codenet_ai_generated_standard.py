def main():
    target = [5,7,5,7,7]
    while True:
        n = int(input())
        if n == 0:
            break
        words = [input() for _ in range(n)]
        lens = [len(w) for w in words]
        for start in range(n):
            idx = start
            valid = True
            for t in target:
                s = 0
                while idx < n and s < t:
                    s += lens[idx]
                    idx +=1
                if s != t:
                    valid = False
                    break
            if valid:
                print(start+1)
                break
if __name__ == "__main__":
    main()