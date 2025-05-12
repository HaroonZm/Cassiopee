def is_solved(nums):
  keys = set(nums)
  for key in keys:
    if nums.count(key) >= 2:
      tmp = nums[:]
      tmp.remove(key)
      tmp.remove(key)
      for key in keys:
        key_count = tmp.count(key)
        if key_count == 4:
          if key + 1 in tmp and key + 2 in tmp:
            for _ in range(4): tmp.remove(key)
            tmp.remove(key + 1)
            tmp.remove(key + 2)
        elif key_count == 3:
          for _ in range(3): tmp.remove(key)

        elif tmp.count(key + 1) >= key_count and tmp.count(key + 2) >= key_count:
          for _ in range(key_count):
            tmp.remove(key)
            tmp.remove(key + 1)
            tmp.remove(key + 2)
      if tmp == []:
        return True
  return False

while True:
  try:
    puzzle = list(map(int, list(input())))
    ans = []
    for i in range(1, 10):
      if puzzle.count(i) <= 3 and is_solved(puzzle + [i]):
        ans.append(i)
    if ans:
      print(*ans)
    else:
      print(0)
  except EOFError:
    break