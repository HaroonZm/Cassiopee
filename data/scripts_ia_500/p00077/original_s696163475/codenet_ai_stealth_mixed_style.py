def decode():
    from collections import deque
    while True:
        try:
            s = deque(list(input()))
            ans = []
            while s:
                ch = s.popleft()
                if ch == '@':
                    count = int(s.popleft())
                    char = s.popleft()
                    ans.append(char * count)
                else:
                    ans.append(ch)
            print("".join(ans))
        except Exception:
            break

decode()