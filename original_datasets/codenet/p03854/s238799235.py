# C問題
S = input()
if "eraser" in S:
    S = S.replace("eraser", "")
if "erase" in S:
    S = S.replace("erase", "")
if "dreamer" in S:
    S = S.replace("dreamer", "")
if "dream" in S:
    S = S.replace("dream", "")
    
if len(S) == 0:
    print("YES")
else:
    print("NO")