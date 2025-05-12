class Node:
    def __init__(self):
        self.left=[0]
        self.right=[0]
    def createleft(self,inp,A):
        cnt=0
        for cn in range(len(inp)):
            c=inp[cn]
            if c=='(':
                cnt+=1
            elif c==')':
                cnt-=1
            elif cnt==0:
                self.left=[A[int(c)-1]]
            elif c==' ' and cnt==1:
                leftnode=Node()
                inpl=inp[1:cn]
                inpr=inp[cn+1:len(inp)-1]
                leftnode.createleft(inpl,A)
                leftnode.createright(inpr,A)
                self.left=leftnode
        
    def createright(self,inp,A):
        cnt=0
        for cn in range(len(inp)):
            c=inp[cn]
            if c=='(':
                cnt+=1
            elif c==')':
                cnt-=1
            elif cnt==0:
                self.right=[A[int(c)-1]]
            elif c==' ' and cnt==1:
            	rightnode=Node()
                inpl=inp[1:cn]
                inpr=inp[cn+1:len(inp)-1]
                rightnode.createleft(inpl,A)
                rightnode.createright(inpr,A)
                self.right=rightnode
    def possible(self):
        lp=self.left
        rp=self.right
        if isinstance(self.left,Node):
            lp=self.left.possible()
        if  isinstance(self.right,Node):
            rp=self.right.possible()
        return [l & r for l in lp for r in rp]+[l | r for l in lp for r in rp]+[l ^ r for l in lp for r in rp]
 
 
 
while(1):
    inp=raw_input()
    if inp=='END': break
    n=int(raw_input())
    A=[]
    for i in range(n):
        bn=int(''.join(raw_input().split()),2)
        A.append(bn)
    cnt=0
    root=Node()
    #create tree
    cnt=0
    for cn in range(len(inp)):
        c=inp[cn]
        if c=='(':
            cnt+=1
        elif c==')':
            cnt-=1
        elif c==' ' and cnt==1:
            inpl=inp[1:cn]
            inpr=inp[cn+1:len(inp)-1]
            root.createleft(inpl,A)
            root.createright(inpr,A)
    #count
    poss=root.possible()
    ans=poss.count(15)
    print ans