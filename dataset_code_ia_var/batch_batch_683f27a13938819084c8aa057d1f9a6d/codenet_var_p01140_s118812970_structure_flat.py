while 1:
    n, m = map(int, raw_input().split(" "))
    if n == 0 and m == 0:
        break
    Lon = []
    Lat = []
    for i in range(1000 * n + 1):
        Lon.append(0)
    for i in range(1000 * m + 1):
        Lat.append(0)
    Lon_sum = []
    Lat_sum = []
    for i in range(n):
        Lon_sum.append(0)
    for i in range(m):
        Lat_sum.append(0)
    i = 0
    while i < n:
        h = int(raw_input())
        j = 0
        while j <= i:
            Lon_sum[j] += h
            Lon[Lon_sum[j]] += 1
            j += 1
        i += 1
    i = 0
    while i < m:
        w = int(raw_input())
        j = 0
        while j <= i:
            Lat_sum[j] += w
            Lat[Lat_sum[j]] += 1
            j += 1
        i += 1
    if Lon_sum and Lat_sum:
        max_width = Lon_sum[0]
        if Lat_sum[0] < max_width:
            max_width = Lat_sum[0]
    else:
        max_width = 0
    result = 0
    i = 1
    while i <= max_width:
        result += Lon[i] * Lat[i]
        i += 1
    print result