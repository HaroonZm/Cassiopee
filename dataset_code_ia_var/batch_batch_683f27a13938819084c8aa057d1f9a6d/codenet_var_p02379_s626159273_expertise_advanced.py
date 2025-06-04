from math import hypot

print(hypot(*map(lambda a, b: float(a) - float(b), *[input().split()[:2], input().split()[2:]]))
      if len((inp := input().split())) == 4 else hypot(*((float(inp[0])-float(inp[2])), (float(inp[1])-float(inp[3])))))