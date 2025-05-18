while True:
  try:
    a, b = sorted(map(int, raw_input().split()))
    while a:
      tmp = a
      a = b % a;
      b = tmp
    print b
  except EOFError:
    break