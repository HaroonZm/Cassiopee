class Dice:
    def __init__(self,l):
        self.f=l
        
    def __str__(self):
        l=self.f
        s=f'[U:{l[0]},S:{l[1]},E:{l[2]},W:{l[3]},N:{l[4]},D:{l[5]}]'
        return(s)
       
    def roll(self,c):
        if c=='N':
            ni=[1,5,2,3,0,4]
        elif c=='S':
            ni=[4,0,2,3,5,1]
        elif c=='E':
            ni=[3,1,0,5,4,2]
        elif c=='W':
            ni=[2,1,5,0,4,3]
        self.f=[self.f[j] for j in ni]
    
    def rotate(self,r):
        if r==+1:
            ni=[0,3,1,4,2,5]
        elif r==-1:
            ni=[0,2,4,1,3,5]
        self.f=[self.f[j] for j in ni]

    def patterns(self):
        fs=[]
        for i in range(6):
            if i%2==0:
                self.roll('N')
            else:
                self.roll('E')
            for j in range(4):
                self.rotate(+1)
                fs.append(self.f)
        return fs
        
    def lookEast(self,l):
        for f in self.patterns():
            if f[0]==l[0] and f[1]==l[1]:
                return f[2]
    
    def equals(self,d):
        for f in self.patterns():
            if f==d.f:
                return True
        return False

n=int(input())
d0=Dice(list(map(int,input().split())))
flag = True
for i in range(n-1):
    if d0.equals(Dice(list(map(int,input().split())))):
        flag=False
        break
print('Yes' if flag else 'No')