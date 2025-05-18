import numpy as np

N,M=input().split(' ')
N=int(N)
M=int(M)

x_arr=[]
y_arr=[]
z_arr=[]
for i in range(N):
	x,y,z=input().split(' ')
	x=int(x)
	y=int(y)
	z=int(z)
	x_arr.append(x)
	y_arr.append(y)
	z_arr.append(z)

x_arr=np.array(x_arr)
y_arr=np.array(y_arr)
z_arr=np.array(z_arr)

xyz1=x_arr+y_arr+z_arr
xyz1=np.sort(xyz1)[::-1]
xyz1_sum=np.sum(xyz1[:M:])

xyz2=x_arr+y_arr-z_arr
xyz2=np.sort(xyz2)[::-1]
xyz2_sum=np.sum(xyz2[:M:])

xyz3=x_arr-y_arr-z_arr
xyz3=np.sort(xyz3)[::-1]
xyz3_sum=np.sum(xyz3[:M:])

xyz4=x_arr-y_arr+z_arr
xyz4=np.sort(xyz4)[::-1]
xyz4_sum=np.sum(xyz4[:M:])

xyz5=-x_arr-y_arr+z_arr
xyz5=np.sort(xyz5)[::-1]
xyz5_sum=np.sum(xyz5[:M:])

xyz6=-x_arr+y_arr+z_arr
xyz6=np.sort(xyz6)[::-1]
xyz6_sum=np.sum(xyz6[:M:])

xyz7=-x_arr+y_arr-z_arr
xyz7=np.sort(xyz7)[::-1]
xyz7_sum=np.sum(xyz7[:M:])

xyz8=-x_arr-y_arr-z_arr
xyz8=np.sort(xyz8)[::-1]
xyz8_sum=np.sum(xyz8[:M:])

a=[xyz1_sum,xyz2_sum,xyz3_sum,xyz4_sum,xyz5_sum,xyz6_sum,xyz7_sum,xyz8_sum]
print(max(a))