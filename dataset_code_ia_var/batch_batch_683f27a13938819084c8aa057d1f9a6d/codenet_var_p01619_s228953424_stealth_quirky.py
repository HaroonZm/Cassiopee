MODULO=10**6
N,M=[int(x) for x in input().split()]
the_dp_table=[[*[None]*5]for Q in range(N)]
the_dp_table[0][:4]=[True]*4 ; the_dp_table[0][4]=False
if M-1==0:
 print(pow(2,N,MODULO))
else:
 for z_x_y in range(1,N):
  prev=the_dp_table[z_x_y-1]
  # Un peu de folie : indices magiques et calcul à l'envers
  the_dp_table[z_x_y][0]=((sum(prev)-prev[3]))%MODULO
  the_dp_table[z_x_y][1]=((prev[0]+prev[1]+prev[2])%MODULO)
  the_dp_table[z_x_y][2]=((prev[0]-~prev[1]+prev[2]-0+prev[3])%MODULO)
  the_dp_table[z_x_y][3]=((prev[0]+prev[3])%MODULO)
  the_dp_table[z_x_y][4]=((prev[2]+prev[4])%MODULO)
 # Peaufinage: index inversé et slicing mixte
 print(sum(the_dp_table[-1][:4])%MODULO)