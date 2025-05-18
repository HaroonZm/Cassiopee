def readinput():
    b=input()
    return b

def main(b):
    dic={'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    return dic[b]

if __name__=='__main__':
    b=readinput()
    ans=main(b)
    print(ans)