def split(x):
    assert isinstance(x, int)
    sx = str(x)
    l = len(sx)
    candidates = []
    for idx in range(1, l):
        candidates.append(int(sx[:idx]) * int(sx[idx:]))
    if len(candidates) == 0:
        return None
    else:
        return max(candidates)

def problem1():
    Q = input()
    answers = []
    for _ in range(int(Q)):
        N = int(input())
        x = N
        cnt = 0
        while True:
            next_x = split(x)
            if next_x is None:
                break
            elif x == next_x:
                cnt = -1
                break
            else:
                cnt += 1
                x = next_x
        answers.append(str(cnt))
    print('\n'.join(answers))

if __name__ == '__main__':
    problem1()