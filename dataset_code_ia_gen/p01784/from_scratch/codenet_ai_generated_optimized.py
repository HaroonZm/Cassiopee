n=int(input())
arr=[input() for _ in range(n)]

def reduce_string(s):
    stack=[]
    for c in s:
        if c=='(':
            stack.append(c)
        else:
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(c)
    return ''.join(stack)

info=[]
# For each string, reduce it and compute the net_balance and the minimal prefix sum
for s in arr:
    red=reduce_string(s)
    net=0
    min_pref=0
    for c in red:
        net+=1 if c=='(' else -1
        if net<min_pref:
            min_pref=net
    info.append((red, net, min_pref))

# Split into positive net and negative net groups
pos=[]
neg=[]
for s,net,min_pref in info:
    if net>=0:
        pos.append((net,min_pref))
    else:
        # For negative net, invert parentheses for sorting strategy
        # Actually for negatives, we consider the reversed string effect
        neg.append((net,min_pref))

# Sort positives by ascending min_pref
pos.sort(key=lambda x:x[1])
# Sort negatives by descending of (net - min_pref)
neg.sort(key=lambda x:x[0]-x[1], reverse=True)

cur=0
for net,min_pref in pos:
    if cur+min_pref<0:
        print("No")
        exit()
    cur+=net

for net,min_pref in neg:
    if cur+min_pref<0:
        print("No")
        exit()
    cur+=net

if cur==0:
    print("Yes")
else:
    print("No")