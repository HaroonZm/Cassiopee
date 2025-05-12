import math
EPS=1e-10

#点类
class Point():

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __sub__(self,p):
        return Point(self.x - p.x, self.y - p.y);
    def __add__(self,p):
        return Point(self.x + p.x, self.y + p.y)
           
    def __mul__(self,a): #a: scalar
        return Point(self.x * a, self.y * a)
    def __truediv__(self,a): #a: scalar
        return Point(self.x / a, self.y / a)
   
    def __str__(self):
       return  str(self.x)+','+str(self.y)
    def __repr__(self):
        return  'Point('+str(self.x)+','+str(self.y)+')'
    
    def __lt__(self, other):    
        if self.y-other.y==0:
            return self.x<other.x
        else:
            return self.y<other.y
            
    def __eq__(self, other):    
        return abs(self.x-other.x)<EPS and  abs(self.y-other.y)<EPS

# 线段类
class Segment():
    def __init__(self,p1, p2):
        self.p1=p1
        self.p2=p2
    def __str__(self):
        return  'segment:('+str(self.p1)+';'+str(self.p2)+')'
    def __repr__(self):
        return  'segment:('+str(self.p1)+';'+str(self.p2)+')'

class Circle():
    def __init__(self,c, r):
        self.c=c
        self.r=r

    def __str__(self):
       return  'Circle:(center point: '+str(self.c)+'; radius: '+str(self.r)+')'
    def __repr__(self):
       return  'Circle:(center point: '+str(self.c)+'; radius: '+str(self.r)+')'
   
    
#定义多边形
class Polygon():
    def __init__(self,ps=[]):
        self.ps=ps
        self.size=len(ps)
  
    def __getitem__(self, i):#iter override 
        return self.ps[i]  
    def __setitem__(self,i,p): 
        self.ps[i]=p               
    def __iter__(self):     
        return self.ps  
    
    def addpoint(self,i,p):
        self.ps.insert(i,p)
        self.size+=1
    def delpoint(self,i):
        self.size-=1
        return self.ps.pop(i)
    def sortYX(self):
        self.ps.sort()
        #self.ps.sort(key=attrgetter('y','x'))
    def __str__(self):
       return  'Polygon:'+str(tuple(self.ps))
    def __repr__(self):
       return  'Polygon:'+str(tuple(self.ps))
        
    def __len__(self):
        return len(self.ps)
    def __eq__(self, other):  
         return self.ps==other.ps
    
    def draw(self):
      
       turtle.screensize(800,800,"black")
       #turtle.setup(width=0.9,height=0.9)
       turtle.title("Polygon convex hull")
       turtle.setworldcoordinates(-400,-400,400,400) 

       #print(turtle.screensize())
       #mywin = turtle.Screen()    
       #mywin.   
       t=turtle.Turtle() 
       #mywin=turtle.Screen()
       
       t.pencolor("red")
       for pt in self.ps:
           t.goto(pt.x,pt.y)
           t.dot(10,'white')
       
 

#***************************点、向量****************************

#向量的模的平方
def norm(p):  
    return p.x * p.x + p.y * p.y

#向量P的长度
def length(p):
    return math.sqrt(p.x * p.x + p.y * p.y)

# 向量的(点)内积, dot(a,b)=|a|*|b|*cos(a,b) (从a,到b的角)
# =============================================================================
# r=dot(a,b),得到矢量a和b的点积，如果两个矢量都非零矢量  
# r<0：两矢量夹角为钝角； 
# r=0：两矢量夹角为直角； 
# r>0：两矢量夹角为锐角  
# =============================================================================
def dot(a, b) :
    return a.x * b.x + a.y * b.y

# =============================================================================
# # 向量的（叉）外积 cross(a,b)=|a||b|*sin(a,b) (从a,到b的角)由a,b构成的平行四边的面积
# r=cross(a,b),得到向量a和向量b的叉积  
# r>0：b在矢量a的逆时针方向；  
# r=0：a,b 平行共线；  
# r<0：b在向量a的顺时针方向 
# =============================================================================
def cross( a, b) :
    return a.x * b.y - a.y * b.x

# 点p在线段s上的投影
def project(s, p):
    base = s.p2 - s.p1
    r = dot(p - s.p1, base) / norm(base)
    return s.p1 + base * r 

# 点a到点b的距离
def getDistance(a, b) :
    return length(a - b)

# 线段l和点p的距离
def getDistanceLP(l, p) :
    return abs( cross(l.p2 - l.p1, p - l.p1) / length(l.p2 - l.p1) )

#getDistanceLP(s3, p7)
    
#线段s与点p的距离
def getDistanceSP(s, p) :
    if (dot(s.p2 - s.p1, p - s.p1) < 0.0):
        return length(p - s.p1)
    if (dot(s.p1 - s.p2, p - s.p2) < 0.0):
        return length(p - s.p2)
    return getDistanceLP(s, p)

#print(getDistanceLP(s3, Point(5,5)))
#print(getDistanceSP(s3, Point(5,5)))

#*************************线段********************************/
# 线段s1，s2是否正交 <==> 内积为0
def isOrthogonalSG(s1, s2) :
    return abs(dot(s1.p2 - s1.p1, s2.p2 - s2.p1))<EPS

# 线段s1，s2是否平行 <==> 叉积为0
def isParallelLN(s1,s2) :
    return abs(cross(s1.p2 - s1.p1, s2.p2 - s2.p1))<0

# 逆时针方向ccw（Counter-Clockwise）
COUNTER_CLOCKWISE = 1;
CLOCKWISE = -1;
ONLINE_BACK = -2;
ONLINE_FRONT = 2;
ON_SEGMENT = 0;

def ccw(p0, p1, p2) :
    a = p1 - p0
    b = p2 - p0
    if (cross(a, b) > EPS):
        return COUNTER_CLOCKWISE
    if (cross(a, b) < -EPS):
        return CLOCKWISE
    if (dot(a, b) < -EPS):
        return ONLINE_BACK
    if (norm(a) < norm(b)):
        return ONLINE_FRONT
    
    return ON_SEGMENT;

def toleft(p0,p1,p2):
    a = p1 - p0
    b = p2 - p0  
    tmp=cross(a,b)
    if tmp > EPS:
        return 1
    elif abs(tmp)<EPS and norm(a)<=norm(b):
        return 2  #共线，p2在p0p1的右延长线上
    elif abs(tmp)<EPS and norm(a)>norm(b):
        return -2  #共线，p2在p0p1的left延长线上    
    else:
        return -1

#以线段s为对称轴与点p成线对称的点
def reflect(s, p) :
    return p + (project(s, p) - p) * 2.0

#判断线段s1和s2是否相交
def intersectSG(s1, s2) :
    return intersectP4(s1.p1, s1.p2, s2.p1, s2.p2)

# 线段s1和线段s2的距离
def getDistanceSG(s1, s2) :
    # 相交
    if (intersectSG(s1, s2)):
        return 0.0
    return min(getDistanceSP(s1, s2.p1), getDistanceSP(s1, s2.p2),\
        getDistanceSP(s2, s1.p1), getDistanceSP(s2, s1.p2))

# 判断线段p1p2和线段p3p4是否相交
def intersectP4(p1, p2, p3, p4) :
    return ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and \
            ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0

q=int(input())
for i in range(0,q):
    s= [int(x) for x in input().split()]
    p0=Point(s[0],s[1])
    p1=Point(s[2],s[3])
    p2=Point(s[4],s[5])
    p3=Point(s[6],s[7])
    
    
    if p0==p2 or p0==p3 or p1==p2 or p1==p3:
        print(1)

    elif cross(p1-p0,p2-p0)*cross(p1-p0,p3-p0)<0 and \
           cross(p3-p2,p0-p2)*cross(p3-p2,p1-p2)<0:
       print(1)
    
    elif cross(p1-p0,p2-p0)==0 and dot (p1-p0,p2-p0)>0 and \
            length(p2-p0)<length(p1-p0):
        print(1)
                
    elif cross(p1-p0,p3-p0)==0 and dot (p1-p0,p3-p0)>0 and \
            length(p3-p0)<length(p3-p0):
        print(1)

    elif cross(p3-p2,p0-p2)==0 and dot (p3-p2,p0-p2)>0 and \
            length(p0-p2)<length(p3-p2):
        print(1)
                
    elif cross(p3-p2,p1-p2)==0 and dot (p3-p2,p1-p2)>0 and \
            length(p1-p2)<length(p3-p2):
        print(1)

    else:
       print(0)