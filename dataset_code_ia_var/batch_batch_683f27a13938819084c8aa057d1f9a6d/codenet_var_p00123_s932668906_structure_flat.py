import bisect
m500 = [35.5, 37.5, 40, 43, 50, 55, 70]
m1000 = [71, 77, 83, 89, 105, 116, 148]
rank = ["AAA", "AA", "A", "B", "C", "D", "E", "NA"]
while True:
    try:
        s = input()
    except:
        break
    if not s:
        break
    parts = s.split()
    n = float(parts[0])
    m = float(parts[1])
    idx1 = bisect.bisect_left(m500, n + 0.001)
    idx2 = bisect.bisect_left(m1000, m + 0.001)
    idx = max(idx1, idx2)
    print(rank[idx])