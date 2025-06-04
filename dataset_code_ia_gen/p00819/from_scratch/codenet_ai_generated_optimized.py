def main():
    import sys
    input=sys.stdin.readline

    def inv_J(s): return s[-1]+s[:-1]
    def inv_C(s): return s[1:]+s[0]
    def inv_E(s):
        l=len(s)
        mid=l//2
        if l%2==0:
            return s[mid:]+s[:mid]
        else:
            return s[mid+1:]+s[mid]+s[:mid]
    def inv_A(s): return s[::-1]
    def inv_P(s):
        res=[]
        for c in s:
            if c.isdigit():
                res.append('9' if c=='0' else str(int(c)-1))
            else:
                res.append(c)
        return ''.join(res)
    def inv_M(s):
        res=[]
        for c in s:
            if c.isdigit():
                res.append('0' if c=='9' else str(int(c)+1))
            else:
                res.append(c)
        return ''.join(res)

    inv_map={'J':inv_J,'C':inv_C,'E':inv_E,'A':inv_A,'P':inv_P,'M':inv_M}
    n=int(input())
    for _ in range(n):
        order=input().strip()
        msg=input().rstrip('\n')
        for ch in reversed(order):
            msg=inv_map[ch](msg)
        print(msg)
main()