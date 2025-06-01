def gcd(a,b):
  return a if b==0 else gcd(b,a%b)

def read_numbers():
  return [*map(int,input().split())]

def mod_cycle_length(base, mod):
  val = base % mod
  count = 1
  while val != 1:
    val = val * base % mod
    count +=1
  return count

while True:
  data = read_numbers()
  if all(v==0 for v in data): break
  ix = mod_cycle_length(data[0], data[1])
  iy = mod_cycle_length(data[2], data[3])
  iz = mod_cycle_length(data[4], data[5])
  lcm_xy = (ix*iy)//gcd(ix,iy)
  print((lcm_xy*iz)//gcd(lcm_xy,iz))