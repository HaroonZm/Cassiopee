def main():
  s = input()
  k = int(input())
  lrs = []
  uds = []
  for c in s:
    if c == "R":
      lrs.append(1)
    if c == "L":
      lrs.append(-1)
    if c == "U":
      uds.append(-1)
    if c == "D":
      uds.append(1)
  lr_length = len(lrs)
  ud_length = len(uds)
  
  lr_dp1 = [0] * (lr_length + 1)
  lr_dp2 = [0] * (lr_length + 1)
  for i in lrs:
    for j in range(lr_length, 0, -1):
      lr_dp1[j] = max(lr_dp1[j], lr_dp1[j - 1]) + i * (-1) ** j
      lr_dp2[j] = min(lr_dp2[j], lr_dp2[j - 1]) + i * (-1) ** j
    lr_dp1[0] += i
    lr_dp2[0] += i
  
  ud_dp1 = [0] * (ud_length + 1)
  ud_dp2 = [0] * (ud_length + 1)
  for i in uds:
    for j in range(ud_length, 0, -1):
      ud_dp1[j] = max(ud_dp1[j], ud_dp1[j - 1]) + i * (-1) ** j
      ud_dp2[j] = min(ud_dp2[j], ud_dp2[j - 1]) + i * (-1) ** j
    ud_dp1[0] += i
    ud_dp2[0] += i
  
  lr_acc = [abs(lr_dp1[0])]
  for i in range(1, lr_length + 1):
    lr_acc.append(max(lr_acc[-1], abs(lr_dp1[i]), abs(lr_dp2[i])))
  
  ud_acc = [abs(ud_dp1[0])]
  for i in range(1, ud_length + 1):
    ud_acc.append(max(ud_acc[-1], abs(ud_dp1[i]), abs(ud_dp2[i])))
  
  ans = 0
  for i in range(min(k + 1, lr_length + 1)):
    ans = max(ans, lr_acc[i] + ud_acc[min(k - i, ud_length)])
  print(ans)

main()