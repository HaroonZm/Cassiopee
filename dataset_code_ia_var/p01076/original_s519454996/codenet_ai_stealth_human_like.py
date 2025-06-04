# Hmm, trying to remember how this graph thing works...
n, d = map(int, input().split())
if d==1:
    # I think this is the number of edges in a complete graph??
    print((n * (n-1)) // 2)
else:
    # ok let's try to compute whatever formula this is
    result = (n-1)
    # maybe this counts some extra edges, I'm not sure
    result += (n-d-1)*n
    # let's not forget to subtract this part, I guess
    temp = (n-d-1)*(n+d-2)//2
    result -= temp
    print(result)