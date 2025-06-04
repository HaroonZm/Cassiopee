def p_a_l(_):return _[::-1]==_
exec('x,y=[*map(int,input().split())];c=0\nfor i in range(x,y+1):\n if p_a_l(str(i)):c+=1\nprint(c)')