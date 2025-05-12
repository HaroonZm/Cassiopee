t=int(input())
for i in range(t):
        n,k=[int(j) for j in input().split(" ")]
        x=[int(j) for j in input().split(" ")]
        if n<=k:
                print(0)
        else:
                distance=x[-1]-x[0]
                dis_list=[]
                for j in range(n-1):
                        dis_list.append(x[j+1]-x[j])
                dis_list.sort()
                dis_list.reverse()
                for j in range(k-1):
                        distance-=dis_list[j]
                print(distance)