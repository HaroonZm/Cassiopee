def count_ones(x): return sum([i=='1' for i in x])

class Counter:
    def __init__(self,v):self.v=v
    def display(self): print(count_ones(self.v))

if __name__=='__main__':
    import sys
    s=sys.stdin.readline().strip()
    c=Counter(s)
    c.display()