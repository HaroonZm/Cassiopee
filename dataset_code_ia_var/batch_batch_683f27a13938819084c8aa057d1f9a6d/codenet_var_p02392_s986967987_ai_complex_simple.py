*_,*_[0],*_[1],*_[2]=map(str,input().split()+[None]*1)
a,b,c=map(lambda x:eval("+".join(map(str,[int(x)]))),[*_[0],*_[1],*_[2]])
print({True:"Yes",False:"No"}[all(map(lambda pair:pair[0]<pair[1],zip((a,b),(b,c))) )])