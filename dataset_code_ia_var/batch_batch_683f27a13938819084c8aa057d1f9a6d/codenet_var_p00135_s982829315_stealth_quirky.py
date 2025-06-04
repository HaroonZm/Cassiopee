def handle(*z):return(input()if not z else z[0])
class C:pass
for x in range(int(handle())):
    y=C();(y.hh,y.mm)=[int(q)for q in handle().split(':')]
    y.HH,y.MM=(30*y.hh+y.mm//2)*2,(6*y.mm)*2
    if y.mm%2:y.HH+=1
    y.ang=abs(y.HH-y.MM)
    y.alt=720-y.ang
    y.final=y.ang if y.ang<y.alt else y.alt
    [print(k)for k,v in[("alert",y.final<60),("safe",180<=y.final<=360),("warning",1)]if v][0]