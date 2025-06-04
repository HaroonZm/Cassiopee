n, c = input().split()
n = int(n)
c = int(c)

t_tk_r = 0
t_md_r = 0
g_tk_r = 0
g_md_r = 0

t_tk_m = 0
t_md_m = 0
g_tk_m = 0
g_md_m = 0

t_tk = []
t_md = []
g_tk = []
g_md = []
a = []
d1 = 0

for i in range(n):
    values = input().split()
    d = int(values[0])
    v = int(values[1])
    a.append([d, v])

for i in range(n):
    d0 = a[i][0]
    v0 = a[i][1]
    t_tk_r = t_tk_r + v0 - (d0 - d1)
    t_md_r = t_md_r + v0 - (d0 - d1) * 2
    if t_tk_r > t_tk_m:
        t_tk_m = t_tk_r
    if t_md_r > t_md_m:
        t_md_m = t_md_r
    t_tk.append(t_tk_m)
    t_md.append(t_md_m)
    d1 = d0

d1 = 0

for i in range(n-1, -1, -1):
    d0 = a[i][0]
    v0 = a[i][1]
    g_tk_r = g_tk_r + v0 - ((c - d0) - d1)
    g_md_r = g_md_r + v0 - ((c - d0) - d1) * 2
    if g_tk_r > g_tk_m:
        g_tk_m = g_tk_r
    if g_md_r > g_md_m:
        g_md_m = g_md_r
    g_tk.append(g_tk_m)
    g_md.append(g_md_m)
    d1 = c - d0

mx = t_tk[0] if n > 0 else 0
for x in t_tk:
    if x > mx:
        mx = x
for x in g_tk:
    if x > mx:
        mx = x
if mx < 0:
    mx = 0

for i in range(n-1):
    val1 = t_tk[i] + g_md[n-2-i]
    val2 = t_md[i] + g_tk[n-i-2]
    if val1 > mx:
        mx = val1
    if val2 > mx:
        mx = val2

print(mx)