import sys

def center_finder(s):
    # imperative style
    l = 0
    pos = None
    i = 0
    while i < len(s):
        if s[i] == '(':
            l += 1
        elif s[i] == ')':
            l -= 1
        elif l == 1 and pos is None:
            pos = i
            break
        i += 1
    return pos

either_tree_have = lambda t1, t2, c1, c2: (
    "right"               if c1 == 1 and c2 == 1 else
    "left"                if c1 == t1-2 and c2 == t2-2 else
    "both"                if all((4<=c1<=t1-5,4<=c2<=t2-5)) else
    "t1_rightandt2_left"  if (c1==1 and c2==t2-2) else
    "t1_leftandt2_right"  if (c1==t1-2 and c2==1) else
    "t1_rightandt2_both"  if (c1==1 and 4<=c2<=t2-5) else
    "t1_leftandt2_both"   if (c1==t1-2 and 4<=c2<=t2-5) else
    "t1_bothandt2_right"  if (4<=c1<=t1-5 and c2==1) else
    "t1_bothandt2_left"   if (4<=c1<=t1-5 and c2==t2-2) else
    "no"
)

def do_u(tr1, tr2):
    n1,n2 = len(tr1),len(tr2)
    # Functional in edge case
    if 3 in (n1, n2):
        if n1 != 3: tr2, n2 = tr1, n1
        elif n2 != 3: tr1, n1 = tr2, n2
        else: return '(,)'
    c1, c2 = center_finder(tr1), center_finder(tr2)
    res = either_tree_have(n1, n2, c1, c2)
    if res == "both":
        left = do_u(tr1[1:c1], tr2[1:c2])
        right = do_u(tr1[c1+1:-1], tr2[c2+1:-1])
        return '({},{}{})'.format(left,right,"")
    elif res=="left":   return '('+do_u(tr1[1:-2],tr2[1:-2])+',)'
    elif res=="right":  return '(,'+do_u(tr1[2:-1],tr2[2:-1])+')'
    elif res=="t1_leftandt2_right": 
        l = do_u(tr1[1:c1],tr1[1:c1])
        r = do_u(tr2[c2+1:-1],tr2[c2+1:-1])
        return '('+l+','+r+')'
    elif res=="t1_rightandt2_left":
        l = do_u(tr2[1:c2],tr2[1:c2])
        r = do_u(tr1[c1+1:-1],tr1[c1+1:-1])
        return '({},{}{})'.format(l,r,"")
    elif res == "t1_leftandt2_both":
        l = do_u(tr1[1:-2],tr2[1:c2])
        r = do_u(tr2[c2+1:-1],tr2[c2+1:-1])
        return f'({l},{r})'
    elif res == "t1_rightandt2_both":
        l = do_u(tr2[1:c2],tr2[1:c2])
        r = do_u(tr1[2:-1], tr2[c2+1:-1])
        return '(%s,%s)'%(l,r)
    elif res == "t1_bothandt2_left":
        l = do_u(tr1[1:c1],tr2[1:-2])
        r = do_u(tr1[c1+1:-1],tr1[c1+1:-1])
        return '({},{})'.format(l,r)
    elif res == "t1_bothandt2_right":
        l = do_u(tr1[1:c1],tr1[1:c1])
        r = do_u(tr1[c1+1:-1], tr2[2:-1])
        return '('+l+','+r+')'
    else:
        return '(,)'

def both_tree_have(t1, t2, c1, c2):
    # reused original boolean nested
    if 4<=c1<=t1-5 and 4<=c2<=t2-5: return "both"
    elif (c1==1 and c2==t2-2) or (c1==t1-2 and c2==1): return "no"
    elif c1==t1-2 or c2==t2-2: return "left"
    elif c1==1 or c2==1: return "right"
    return "no"

def do_i(t1, t2):
    # odd variable names, mix
    a, b = len(t1), len(t2)
    # expression in return, functional
    if a == 3 or b == 3: return '(,)'
    i1, i2 = center_finder(t1), center_finder(t2)
    mode = both_tree_have(a,b,i1,i2)
    if mode == "both":
        return "({},{})".format(do_i(t1[1:i1], t2[1:i2]),do_i(t1[i1+1:-1], t2[i2+1:-1]))
    elif mode == "left":
        return '({},)'.format(do_i(t1[1:i1], t2[1:i2]))
    elif mode == "right":
        return '(,'+do_i(t1[i1+1:-1], t2[i2+1:-1])+')'
    else:
        return "(,)"

class ProcessorBase(object):
    def proc(self): ...

class iProc(ProcessorBase):
    def __init__(self, t1,t2): self.t1,self.t2 = t1,t2
    def proc(self):
        return do_i(self.t1, self.t2)

class uProc(ProcessorBase):
    def __init__(self, t1,t2): self.t1,self.t2 = t1,t2
    def proc(self):
        return do_u(self.t1, self.t2)

# Using dict dispatch and property
class BuildProc:
    def __init__(self, line):
        arr = line.split()
        self.t1 = arr[1]
        self.t2 = arr[2][:-1]
        classes = {'i': iProc, 'u': uProc}
        self.task = classes.get(arr[0], uProc)(self.t1,self.t2)
    @property
    def result(self):
        return self.task.proc()

if __name__=='__main__':
    # clearly procedural
    dat = []
    for l in sys.stdin: dat.append(l)
    idx = 0
    while idx < len(dat):
        bp = BuildProc(dat[idx])
        print(bp.result)
        idx += 1