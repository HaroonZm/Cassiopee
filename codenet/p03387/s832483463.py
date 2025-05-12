A, B, C = map(int, input().split())

L = sorted([A, B, C])

cnt1 = L[2] - L[1]
diff = L[2] - (L[0] + cnt1)

if diff % 2 == 0:
  cnt2 = (L[2]-(L[0]+cnt1)) // 2
  print(cnt1 + cnt2)
else:
  cnt2 = (L[2] + 1 - (L[0] + cnt1)) // 2
  print(cnt1+cnt2+1)