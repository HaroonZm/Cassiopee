n,c= [int(i) for i in input().split()]
t_tk_r=0
t_md_r=0
g_tk_r=0
g_md_r=0
t_tk_m=0
t_md_m=0
g_tk_m=0
g_md_m=0
t_tk=[]
t_md=[]
g_tk=[]
g_md=[]
a=[]
d1=0

for i in range(n):
  a.append([int(i) for i in input().split()])

for d0,v0 in a:
  t_tk_r += v0-(d0-d1)
  t_md_r += v0-(d0-d1)*2
  t_tk_m = max(t_tk_m,t_tk_r)
  t_md_m = max(t_md_m,t_md_r)
  t_tk.append(t_tk_m)
  t_md.append(t_md_m)
  d1=d0
  
d1=0  
for d0,v0 in a[::-1]:
  g_tk_r += v0-((c-d0)-d1)
  g_md_r += v0-((c-d0)-d1)*2
  g_tk_m = max(g_tk_m,g_tk_r)
  g_md_m = max(g_md_m,g_md_r)
  g_tk.append(g_tk_m)
  g_md.append(g_md_m)
  d1=(c-d0) 
mx=max(max(t_tk),max(g_tk),0)

for i in range(n-1):
  mx=max(mx,t_tk[i]+g_md[n-2-i],t_md[i]+g_tk[n-i-2])
print(mx)