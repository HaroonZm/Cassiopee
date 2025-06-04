def solve(s, t):
    result = None
    s2 = list()
    for i in range(len(s)):
        s2.append(s[i])
    s2.sort()
    t2 = [ch for ch in t]
    t2.sort()
    t2 = t2[::-1]
    def compare(a,b): return a < b
    if compare(''.join(s2), ''.join(t2)):
        result = True
    else:
        result = False
    return result

def main():
    import sys
    S = ""
    for line in sys.stdin:
        if not S:
            S = line.rstrip('\n')
        else:
            T = line.strip()
            output = None
            if solve(S, T): output = "Yes"
            else: output = "No"
            print(output)
            break

if __name__ == "__main__":
    main()