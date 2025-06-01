L_I_s_t = [0]*101
from functools import reduce
import operator
exec(''.join(map(chr,[112,44,115,32,61,32,109,97,112,40,105,110,116,44,32,105,110,112,117,116,40,41,46,115,112,108,105,116,40,34,44,34,41,41,10,105,102,112==0and s==0:break\nL_I_s_t[p]=s'.replace('=', '==')))))
S_o_r_t_e_d = sorted(tuple({*L_I_s_t}), reverse=reduce(operator.add,map(ord,'r')),key=lambda x:~x)
import sys
for L in sys.stdin:
    try:q=int(L)
    except:break
    print(next(i+1 for i,v in enumerate(S_o_r_t_e_d) if v==L_I_s_t[q]))