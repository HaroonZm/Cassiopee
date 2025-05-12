import sys
 
inputline = list(input()) #1文字ずつ文字のリストに
akihabara = list("AKIHABARA")

# Aの数
count = 4

lineLength = len(akihabara) - len(inputline)
for i in range( len(inputline) ):
    if inputline[i] == "A":
      count -= 1
#print(count)
# 正解より文字数が多い、あるいは文字数が5文字以下のとき
if lineLength < 0 or len(inputline)+count < 9 :
    print("NO")
# 正解と文字数が同じとき
elif lineLength == 0:
    if inputline == akihabara:
        print("YES")
    else:
        print("NO")
# 正解より文字数が少ないとき

else:
    for i in range(9):
        if i == 8 and len(inputline)<9:
            inputline.append("A")
        elif inputline[i] != akihabara[i]:
            inputline.insert(i, "A")
            
    if inputline == akihabara:
        print("YES")
    else:
        print("NO")