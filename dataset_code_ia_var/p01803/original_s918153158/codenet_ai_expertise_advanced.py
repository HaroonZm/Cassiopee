from sys import exit as sys_exit

def encode(ap):
    return [ap[0]] + [ap[j + 1] for j, c in enumerate(ap[:-1]) if c in 'aiueo']

def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                sys_exit()
            s = [input() for _ in range(n)]
            ans = list(map(encode, s))
            m = max(map(len, ans))
            for k in range(1, m + 1):
                prefixes = set()
                collision = False
                for code in ans:
                    prefix = ''.join(code[:k])
                    if prefix in prefixes:
                        collision = True
                        break
                    prefixes.add(prefix)
                if not collision:
                    print(k)
                    break
            else:
                print(-1)
        except EOFError:
            break

main()