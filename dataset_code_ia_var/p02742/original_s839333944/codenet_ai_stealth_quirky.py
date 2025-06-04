_ = lambda: (lambda a, b: [1, (a*b+1)//2][a>1<b])(*map(int, input().split()))
print(_())