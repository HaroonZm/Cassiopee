W=input().lower()
counter=0
while True:
    line=input()
    if line=="END_OF_TEXT":
        break
    else:
        for i in line.lower().split():
            if W==i:
                counter=counter+1
print(counter)