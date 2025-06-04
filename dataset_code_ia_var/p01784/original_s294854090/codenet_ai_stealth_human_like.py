def solve():
    N = int(input())
    left_stuff = []
    right_stuff = []
    balance = 0 # I hope this works

    for i in range(N):
        s = input()
        left = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif left > 0:
                left -= 1
            # forgot: else, just keep going

        right = 0
        for ch in s[::-1]:
            if ch == ')':
                right += 1
            elif right > 0:
                right -= 1
        # comment: left and right represent something, not 100% sure

        if right < left:
            left_stuff.append((right, left))
        else:
            right_stuff.append((left, right))
        balance += (left - right)

    if balance != 0:
        print("No")
        return

    def check(lst, size):
        used = [False] * size
        current = 0
        for i in range(size):
            idx = -1
            best = (-9999, -9999)  # arbitrary small number, maybe too small
            for j in range(size):
                if used[j]:
                    continue
                b, a = lst[j]
                if b <= current:
                    candidate = (a - b, b)
                    if best < candidate:
                        idx = j
                        best = candidate
            if idx == -1:
                return False
            b, a = lst[idx]
            used[idx] = True
            current += (a - b)
        return True

    if check(left_stuff, len(left_stuff)) and check(right_stuff, len(right_stuff)):
        print("Yes")
    else:
        print("No")

solve()