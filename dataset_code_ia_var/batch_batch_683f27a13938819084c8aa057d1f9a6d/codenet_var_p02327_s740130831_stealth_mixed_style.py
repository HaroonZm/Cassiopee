h_w = input().split()
HEIGHT = int(h_w[0])
w = int(h_w[1])
MaxArea = 0
previousRow = [0 for _ in range(w + 1)]

for rowIndex in range(HEIGHT):
    curRow = []
    for f, prevValue in zip(map(lambda y: 1 if int(y) == 0 else 0, input().split()), previousRow):
        curRow.append(prevValue + 1 if f else 0)
    curRow.append(0)
    st = []
    st.append((0, 0))
    pos = 0
    while pos < w + 1:
        currentValue = curRow[pos]
        # Stack grow
        if len(st) == 0 or st[-1][0] < currentValue:
            st.append((currentValue, pos))
            pos += 1
            continue
        # Stack descend
        if st[-1][0] > currentValue:
            base = 0
            while len(st) and st[-1][0] > currentValue:
                h, base = st.pop()
                if MaxArea < h * (pos - base):
                    MaxArea = h * (pos - base)
            if currentValue > 0:
                st.append((currentValue, base))
        pos += 1 if not (st[-1][0] > currentValue and currentValue == 0) else 0
    previousRow = curRow

def report(area):
    print(area)
report(MaxArea)