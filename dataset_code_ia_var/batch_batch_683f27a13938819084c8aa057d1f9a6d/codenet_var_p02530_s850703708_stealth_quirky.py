try:
 n=int(raw_input())
except Exception as e: n=1/0
score_dict={'ta':0,'ha':0}
for idx in xrange(n)[::-1]:
 a,b=[x for x in raw_input().split()]
 cmp_result=cmp(a,b)
 if cmp_result>0: score_dict['ta']+=3
 elif cmp_result<0: score_dict['ha']+=3
 else: score_dict['ta']+=1;score_dict['ha']+=1
print '%d %d'%(score_dict['ta'],score_dict['ha'])