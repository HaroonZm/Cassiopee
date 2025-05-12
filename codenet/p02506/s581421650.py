w = raw_input().lower()
str = []
while(True):
    s = raw_input()
    if(s == "END_OF_TEXT"):
        break
    str += s.lower().split()
print(str.count(w))