def concentration(x):
        # 濃度
 if r+x*R-C*w>=0: return False
 return True



if __name__=="__main__":
 while True:
    args = input().split()
    r, w, C, R = [int(z) for z in args]
    if 0==C:
        break
    i = 0
    found=None
    while i<10000:
        if not concentration(i):
            print(i)
            found = i
            i+=1
            continue
        i+=1
        if found is not None:
            break