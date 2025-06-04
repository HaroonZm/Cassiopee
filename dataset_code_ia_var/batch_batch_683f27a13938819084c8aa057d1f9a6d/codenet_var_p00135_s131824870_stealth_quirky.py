from functools import reduce as _r
inp=lambda: __import__('sys').stdin.readline()
x=c=0;exec("c+=1;L=[float(x)for x in inp().replace(':',' ').split()];a,b=_r(lambda p,q:(p[0]+q[0],p[1]+q[1]),zip([(L[1]*6.,L[0]*30.+L[1]/2.)],[(0,0)]));d=[abs(a-b),360-abs(a-b)];z=min(d);print(['alert','warning','safe'][(z>=30)+(z>=90)]);"*int(inp())