all = input()
while True:
  try:
    str = raw_input()
    if str == '=':
      print all
      break
    num = input()
    if str == '+':
      all += num
    elif str == '-':
      all -= num
    elif str == '*':
      all = all * num
    elif str == '/':
      all = all / num
  except EOFError:
    break