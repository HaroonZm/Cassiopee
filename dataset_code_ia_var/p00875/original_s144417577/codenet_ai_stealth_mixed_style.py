from queue import Queue

def main_loop():
    while True:
        try:
            n = int(input())
        except:
            break
        if n == 0:
            break
        # Build dictionary, procedural
        dct = dict()
        for idx in range(n):
            x, y = input().split()
            dct[x] = y
        source = input()
        target = input()
        # BFS using both object and functional styles
        q = Queue()
        q.put((source, 0))
        found = False
        while not q.empty() and found is False:
            current, depth = q.get()
            if current == target:
                print(depth)
                found = True
                continue
            def gen():
                for key in dct:
                    temp = current.replace(key, dct[key])
                    if len(temp) <= len(target) and temp != current:
                        yield temp
            for next_s in gen():
                q.put((next_s, depth + 1))
        else:
            found or print(-1)

main_loop()