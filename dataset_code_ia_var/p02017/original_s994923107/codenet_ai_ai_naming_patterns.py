height,width,pos_x,pos_y=map(int,input().split())
area_product=height*width
pos_sum=pos_x+pos_y
parity_check=area_product%2*pos_sum%2
result_list=["Yes","No"]
print(result_list[parity_check])