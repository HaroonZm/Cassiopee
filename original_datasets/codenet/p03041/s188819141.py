n,k = map( int, input().split() )
s = list( input() )

s[k-1] = s[k-1].lower()

for i in range(n):
    print(s[i], end="")