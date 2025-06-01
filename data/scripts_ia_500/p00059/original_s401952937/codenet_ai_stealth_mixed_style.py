def check_inclusion():
    while True:
        raw = input()
        if not raw:
            break
        try:
            data = list(map(float, raw.split()))
        except Exception:
            break
        ax, ay, bx, by, cx, cy, dx, dy = data

        def inner_check():
            return (ax <= dx and cx <= bx) and (ay <= dy and cy <= by)

        print('YES' if inner_check() else 'NO')

check_inclusion()