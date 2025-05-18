# 整数の入力
s = input()

words = ["dream", "dreamer", "erase", "eraser"]

def check():
    tmp = s
    while(True):
      current_len = len(tmp)
      for w in words:
        if tmp.endswith(w):
          tmp = tmp[:-len(w)]
      if len(tmp) == 0:
          return "YES"

      if current_len == len(tmp):
          return "NO"

print(check())