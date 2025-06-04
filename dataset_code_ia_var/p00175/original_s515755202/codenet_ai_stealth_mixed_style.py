def tr(o): l,s=[],str;exec('while o:c=o%4;l.append(s(c));o//=4','globals(),locals()');return"".join(l[::-1]) if l else "0"
i = 1
while True:
    data = input()
    try:
        k = int(data)
    except: continue
    if k==-1: 
        break
    if k>0:
        print(tr(k))
    else:
        print(0)