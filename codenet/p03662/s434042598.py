from networkx import*
(N,),*t=[s.split()for s in open(0)]
G=Graph()
G.add_edges_from(t)
s=shortest_path_length
x=s(G,'1')
y=s(G,N)
print('FSennunkeec'[sum(x[k]>y[k]for k in x)*2>=int(N)::2])