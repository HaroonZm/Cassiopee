n=input()
def sum_digits(s): return sum(int(c) for c in s)
class Resolver:
  def __init__(self, m):
    self.m = m
  def is_div_by_10(self):
    return int(self.m)%10==0
r = Resolver(n)
if r.is_div_by_10():
    print(10)
else:
    res = 0
    i = 0
    while i < len(n):
        res += int(n[i])
        i += 1
    print(res if res==sum_digits(n) else sum_digits(n))