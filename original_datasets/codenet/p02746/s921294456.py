q=abs;s=lambda t,i:0--t//3**i;m=lambda a,b,c,d:max([i for i in range(30)if s(a,i)==s(c,i)and s(a,i)%3==2and 1<q(s(b,i)-s(d,i))]+[-1])+1
for _ in[0]*int(input()):
  a,b,c,d=map(int,input().split());h=m(a,b,c,d);w=m(b,a,d,c)
  if h==w==0:print(q(b-d)+q(a-c));continue
  if h<w:h,a,b,c,d=w,b,a,d,c
  i=3**h//3;x=2*i+1;g=a-(a-1)%(3*i)-1;a-=g;c-=g;print(q(b-d)+min(q(i-a)+q(i-c),q(x-a)+q(x-c)))