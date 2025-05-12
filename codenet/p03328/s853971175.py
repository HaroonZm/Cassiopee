w,e = map(int,input().split())
diff = e-w
true_height=0
for h in range(1,diff+1):
  true_height+=h
print(true_height-e)