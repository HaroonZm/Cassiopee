def HB(A,B):
    hits=0
    blows=0
    i=0
    while i<4:
        j=0
        while j<4:
            if A[i]==B[j]:
                hits+=(i==j)
                blows+=(i!=j)
            j+=1
        i+=1
    return hits,blows
def main():
    from sys import stdin
    inputs=[]
    while True:
        line=stdin.readline()
        if not line:
            break
        inputs.append(line.strip().split())
    idx=0
    while idx+1<len(inputs):
        A,B=inputs[idx],inputs[idx+1]
        H,Bw=HB(A,B)
        print(H, Bw)
        idx+=2
if __name__=="__main__":
    main()