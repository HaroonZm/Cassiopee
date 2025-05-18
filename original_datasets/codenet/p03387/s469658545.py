a=list(map(int,input().split()))
p,q=divmod(max(a)*3-sum(a),2)
print(p+q*2)