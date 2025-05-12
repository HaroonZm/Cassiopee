class binary_tree():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def find_corres_bra(s,fr,to):
    count=0 
    x=-1
    for i in range(len(s)):
        if s[i]==fr:
            count += 1
        elif s[i]==to:
            if count==1:
                x=i
                break
            else:
                count-=1
    return x
    

def make_tree(s):
    if s=='':
        return None
    x0=0
    x1=find_corres_bra(s,'(',')')+1
    x2=x1+find_corres_bra(s[x1:],'[',']')+1
    tree=binary_tree(int(s[x1+1:x2-1]),make_tree(s[x0+1:x1-1]),make_tree(s[x2+1:-1]))
    return tree

def synthe_trees(t1,t2):
    tree=binary_tree(value=t1.value+t2.value)
    if t1.left!=None and t2.left !=None:
        tree.left=synthe_trees(t1.left,t2.left)
    if t1.right!=None and t2.right !=None:
        tree.right=synthe_trees(t1.right,t2.right)
    return tree

def tree_to_str(tree):
    if tree==None:
        return ''
    ans='('+ tree_to_str(tree.left)+')'+'['+str(tree.value)+']'+'('+ tree_to_str(tree.right)+')'
    return ans

t1=make_tree(input())
t2=make_tree(input())
tree=synthe_trees(t1,t2)
print(tree_to_str(tree))