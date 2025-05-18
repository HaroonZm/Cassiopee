N=int(input())
X=[0]*10001
for i in range(1,102):
  for j in range(1,102):
    for k in range(1,102):
      if i*i+j*j+k*k+i*j+j*k+k*i<10001:
        X[i*i+j*j+k*k+i*j+j*k+k*i]+=1
for i in range(N):
  print(X[i+1])