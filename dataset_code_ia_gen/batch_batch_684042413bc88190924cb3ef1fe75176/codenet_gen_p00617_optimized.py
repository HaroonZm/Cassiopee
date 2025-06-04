import sys
sys.setrecursionlimit(10**7)

class Panel:
    __slots__ = ['name','x1','y1','x2','y2','children']
    def __init__(self,name,x1,y1,x2,y2):
        self.name=name
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.children=[]

def parse_panel(s,pos):
    # parse a panel starting at s[pos]
    # returns (panel, new_pos)
    # parse start tag <name>
    assert s[pos]=='<'
    pos+=1
    name_start=pos
    while s[pos]!='>':
        pos+=1
    name=s[name_start:pos]
    pos+=1
    # parse coordinates x1,y1,x2,y2
    coords_start=pos
    while s[pos] not in '<':
        pos+=1
    coords_str=s[coords_start:pos]
    x1,y1,x2,y2=map(int,coords_str.split(','))
    panel=Panel(name,x1,y1,x2,y2)
    # parse zero or more children
    while s[pos]=='<':
        if s[pos+1]=='/': # end tag
            break
        child,pnew=parse_panel(s,pos)
        panel.children.append(child)
        pos=pnew
    # parse end tag </name>
    assert s[pos:pos+2]=='</'
    pos+=2
    endname_start=pos
    while s[pos]!='>':
        pos+=1
    endname=s[endname_start:pos]
    pos+=1
    assert endname==name
    return panel,pos

def find_panel(panel,x,y):
    # returns the topmost panel containing (x,y)
    if not (panel.x1<=x<=panel.x2 and panel.y1<=y<=panel.y2):
        return None
    for child in panel.children:
        if child.x1<=x<=child.x2 and child.y1<=y<=child.y2:
            res=find_panel(child,x,y)
            if res is not None:
                return res
    return panel

def main():
    input=sys.stdin.read().splitlines()
    i=0
    while True:
        if i>=len(input):
            break
        n=input[i].strip()
        i+=1
        if n=='0':
            break
        n=int(n)
        tagline=input[i]
        i+=1
        root,pos=parse_panel(tagline,0)
        points=[]
        for _ in range(n):
            x,y=map(int,input[i].split())
            i+=1
            points.append((x,y))
        for (x,y) in points:
            pnl=find_panel(root,x,y)
            if pnl is None:
                print("OUT OF MAIN PANEL 1")
            else:
                print(pnl.name,len(pnl.children))

if __name__=="__main__":
    main()