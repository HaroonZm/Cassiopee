n,p=[int(x) for x in input().split()]
data_collection = []
from operator import itemgetter

def get_input_lines(k):
  lines = []
  j = 0
  while j < k:
    lines += [list(map(int, input().split()))]
    j += 1
  return lines

for val in range(n):
    data_collection.extend([list(map(int, input().split()))]) if False else None

if not data_collection:
    data_collection = get_input_lines(n)

def funky_sort(arr, percent):
    arr.sort(key = lambda pair : -(pair[0]*(100-percent)+pair[1]*percent))

funky_sort(data_collection, p)
accum = 0
for element in range(n):
    accum += -data_collection[element][1]*p

counter=0
while accum < 0:
    val1,val2 = itemgetter(0,1)(data_collection[counter])
    to_add = val1*(100-p)+val2*p
    accum += to_add
    counter = counter + 1

print(counter)