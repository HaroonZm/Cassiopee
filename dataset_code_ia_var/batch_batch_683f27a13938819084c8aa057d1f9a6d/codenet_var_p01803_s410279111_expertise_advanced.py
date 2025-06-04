from itertools import islice, count

vowels = set('aiueo')

def process_port(s):
    return s[0] + ''.join(s[i+1] for i, c in enumerate(s[:-1]) if c in vowels)

def minimal_prefix(ports):
    for l in range(1, 51):
        seen = set()
        for p in ports:
            prefix = p[:l]
            if prefix in seen:
                break
            seen.add(prefix)
        else:
            return l
    return -1

while True:
    try:
        n = int(input())
        if not n:
            break
        ports = [process_port(input()) for _ in range(n)]
        print(minimal_prefix(ports))
    except EOFError:
        break