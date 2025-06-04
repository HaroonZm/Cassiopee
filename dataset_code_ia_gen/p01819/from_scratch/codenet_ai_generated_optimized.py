n,m=map(int,input().split())
data=[input() for _ in range(m)]

# Convert data to a 2D boolean array: True if 'E', False if 'W'
E=[[c=='E' for c in row] for row in data]

# Precompute prefix sums of E's for each column across features
# errors if boundary is between i and i+1:
#   left side (1..i) should be all W's => count of E's in left is errors
#   right side (i+1..n) should be all E's => count of W's in right is errors
# So for each i in [0..n], error = sum of E's in [1..i] + sum of W's in [i+1..n]
# Implement prefix sums to retrieve these quickly

prefixE=[0]*(n+1)  # prefixE[i] = total number of E's in first i prefectures (all features)
for j in range(1,n+1):
    cntE=0
    for fi in range(m):
        if E[fi][j-1]:
            cntE+=1
    prefixE[j]=prefixE[j-1]+cntE

totalE=prefixE[n]

# Similarly, total W = total features * n - total E
total=m*n - totalE

# To compute errors for boundary i (0<=i<=n):
# errors = E in [1..i] + W in [i+1..n]
#      = prefixE[i] + (totalW - W in [1..i])
# W in [1..i] = m*i - prefixE[i]
errors_list=[0]*(n+1)
for i in range(n+1):
    W_in_left = m*i - prefixE[i]
    errors = prefixE[i] + (total - W_in_left)
    errors_list[i]=errors

min_error = min(errors_list)
opt_i = errors_list.index(min_error)

# Output boundary between opt_i and opt_i+1 (1-based)
print(opt_i if opt_i>0 else 0+1, opt_i+1+1 if opt_i<n else n+1)