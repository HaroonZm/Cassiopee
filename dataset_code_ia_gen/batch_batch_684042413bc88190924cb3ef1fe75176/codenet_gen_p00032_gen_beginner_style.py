rectangle_count = 0
rhombus_count = 0

while True:
    try:
        line = input()
        if line.strip() == "":
            break
        parts = line.split(',')
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])

        # 長方形かどうかの判定
        # 長方形では隣り合う2辺a,bと対角線cの長さがピタゴラスの定理に従う： c^2 = a^2 + b^2
        if c*c == a*a + b*b:
            rectangle_count += 1
        # ひし形かどうかの判定
        # ひし形は4辺とも等しいので a == b
        elif a == b:
            rhombus_count += 1
        # それ以外は数えない

    except EOFError:
        break

print(rectangle_count)
print(rhombus_count)