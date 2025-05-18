import copy

shuffle_data = []
copy_data = []

while True:
  data = input()

  if data == "-":
    break

  copy_data.clear()

  for i in data:
    copy_data.append(i)
  
  Number = int(input())

  for i in range(Number):
    shuffle_data.clear()
    shuffle_number = int(input())

    for j in range(shuffle_number, len(data)):
      shuffle_data.append(copy_data[j])

    for j in range(0, shuffle_number):
      shuffle_data.append(copy_data[j])

    copy_data.clear()

    for j in shuffle_data:
      copy_data.append(j)

  for i in shuffle_data:
    print(i, end = "")

  print()