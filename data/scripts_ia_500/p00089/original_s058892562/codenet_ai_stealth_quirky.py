import sys as S
input_data = list(map(lambda x: list(map(int, x.split(','))), S.stdin))
for idx in range(1, len(input_data)):
 length = len(input_data[idx])
 flag = length > len(input_data[idx-1])
 for pos in range(length):
  offset = pos - flag
  window = input_data[idx-1][(offset if pos>0 else 0):(offset+2)]
  input_data[idx][pos] += max(window)
print(*input_data[-1])