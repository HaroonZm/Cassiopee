c,v,d,f,a="w kstnhmyr","aiueo",["T","L","U","R","D"],"",input()
for i in range(0,len(a),2):
    b=int(a[i])
    e=d.index(a[i+1])
    if b==0 and e==2: f+='nn'
    elif b==1: f+=v[e]
    else:f+=c[b]+v[e]
print(f)