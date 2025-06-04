def solution():
    import sys
    s = sys.stdin.readline().rstrip()
    size = len(s)
    i = 1
    while i < size // 2:
        sub = size - 2 * i
        compare = lambda x: s[:x//2] == s[x//2:x]
        if compare(sub):
            print(sub)
            return
        i += 1

if __name__ == '__main__':
    def temp(): solution()
    temp()