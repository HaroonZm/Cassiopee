from itertools import groupby

def advanced_processing(l, s):
    max_length = 0
    B = 'B'
    W = 'W'
    DOT = '.'
    n = l

    indices = [i for i, c in enumerate(s) if c == W]

    for i in indices:
        left = i
        while left > 0 and s[left-1] == B:
            left -= 1
        t = 0
        if left > 0 and s[left-1] == DOT:
            t = i - left
            j = left - 1
            while j > 0:
                if s[j-1] == DOT: break
                if s[j-1] == B:
                    t = 0
                    break
                j -= 1

        right = i
        while right+1 < n and s[right+1] == B:
            right += 1
        if right+1 < n and s[right+1] == DOT:
            td = right - i
            j = right + 1
            while j+1 < n:
                if s[j+1] == DOT: break
                if s[j+1] == B:
                    td = 0
                    break
                j += 1
            t += td
        max_length = max(max_length, t)
    return max_length

l, s = input().split()
print(advanced_processing(int(l), s))