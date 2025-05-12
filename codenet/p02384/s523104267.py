class dice:
    def __init__(self, pip):
        self.pip = pip
        
    def move(self,dir):
        if str(dir) == "E":
            self.pip[0],self.pip[2],self.pip[3],self.pip[5] = self.pip[3],self.pip[0],self.pip[5],self.pip[2]
        elif str(dir) == "W":
            self.pip[0],self.pip[2],self.pip[3],self.pip[5] = self.pip[2],self.pip[5],self.pip[0],self.pip[3]
        elif str(dir) == "N":
            self.pip[0],self.pip[1],self.pip[4],self.pip[5] = self.pip[1],self.pip[5],self.pip[0],self.pip[4]
        elif str(dir) == "S":
            self.pip[0],self.pip[1],self.pip[4],self.pip[5] = self.pip[4],self.pip[0],self.pip[5],self.pip[1]

d = dice(list(map(int,input().split())))
n = int(input())

for i in range(n):
    
    top, front = map(int,input().split())
    
    for op in "EEENEEENEEESEEESEEENEEEN":
        if d.pip[0] == top and d.pip[1] == front:
            break
        d.move(op)    
    print(d.pip[2])