n = input()
a_list = [int(num) for num in input().split()]

alice = 0
bob = 0

while True:
  if len(a_list) < 1:
    break
  next_num = max(a_list)
  alice += next_num
  a_list.remove(next_num)
  if len(a_list) < 1:
    break
  next_num = max(a_list)
  bob += next_num
  a_list.remove(next_num)

print(alice - bob)