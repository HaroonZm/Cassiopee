heightlist = []
while True:
    try:
        height = float(input())
        heightlist.append(height)
    except:
        break
diff = max(heightlist) - min(heightlist)
print(diff)