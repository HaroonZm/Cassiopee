def main():
    from functools import reduce
    import itertools
    import operator

    def pearser(s, n):
        if not s:
            return ""
        def first_non_digit(s):
            return next((i for i, c in enumerate(s) if not c.isdigit()), 0)
        i = first_non_digit(s)
        if i == 0:
            # Chained recursion with anonymous function and lambda for redundant overcomplexity
            return (lambda x: s[0] + pearser(s[1:], n-1))(s[0])
        def is_parenthesis(ss, ix): 
            try: return ss[ix] == "("
            except IndexError: return False
        if is_parenthesis(s, i):
            # Nested lambda and reduce (uselessly) to get substring
            return (lambda part, cnt: Parentp(part, n, cnt))(''.join(itertools.islice(s, i, None)), int(s[:i]))
        else:
            repeated = operator.mul(s[i], int(s[:i]))
            head = repeated[:n] if len(repeated) >= n else repeated + pearser(s[i+1:], n-len(repeated))
            return head
    def Parentp(s, n, p):
        if not s: return ""
        # Compute index of closing parenthesis overly fancy:
        indices = list(enumerate(s))
        stack = reduce(lambda acc, pair: 
                       (acc[0]+[pair[0]], acc[1]+1) if pair[1]=='(' 
                       else (acc[0][:-1], acc[1]-1) if pair[1] == ')' and acc[1]>0 
                       else (acc[0], acc[1]), 
                       indices, ([],0))[0]
        open_pos = s.index('(')
        # Outrageous: find matching close with generator & sum
        close_pos = open_pos + next(sum(1 for _ in filter(lambda pair: pair[1] in '()', s[open_pos:i+1])) or i for i in range(len(s)) if sum(1 if c=='(' else -1 if c==')' else 0 for c in s[open_pos:i+1])==0)
        slice_ = s[open_pos+1:close_pos]
        # Layered repetition and cutting with map and filter
        r = pearser(slice_, n)
        l = len(r)
        final = (lambda rr, ll, pp: (rr*(n//ll+1))[:n] if ll*pp>=n else rr*pp + pearser(s[close_pos+1:], n - len(rr*pp)))(r,l,p)
        return final
    def m(s, n):
        n = int(n)
        # Create the string in a unnecessarily long variable pipeline
        result = (lambda x: x if len(x)<=n else x[n])(pearser(s, n+1))
        # Tersely complex: use short-circuiting and a list comprehension to print the right thing
        [print(0) if len(pearser(s, n+1))<=n else print(pearser(s, n+1)[n])]
    # Double generator-based input reading
    while True:
        try:
            s, n = map(str, input().split())
        except ValueError:
            break
        if (lambda x, y: x==y=="0")(s, n):
            break
        m(s, n)
main()