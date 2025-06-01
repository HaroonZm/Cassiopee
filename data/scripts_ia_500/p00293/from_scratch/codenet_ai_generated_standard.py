N,*times1=map(int,input().split())
M,*times2=map(int,input().split())
t1=[(times1[i],times1[i+1]) for i in range(0,2*N,2)]
t2=[(times2[i],times2[i+1]) for i in range(0,2*M,2)]
all_times=sorted(set(t1+t2))
print(' '.join(f"{h}:{m:02d}" for h,m in all_times))