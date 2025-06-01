a = int(input())
b = list(map(int,input().split()))
cave = []
for i in range(a):
    cat = b[i]
    if cat > 0:
        if cat in cave:
            print(i+1)
            break
        else:
            cave.append(cat)
    else:
        if -(cat) in cave:
            if -(cat) == cave[-1]:
                cave.remove(-(cat))
            else:
                print(i+1)
                break
        else:
            print(i+1)
            break
    if i + 1 == a:
        print("OK")