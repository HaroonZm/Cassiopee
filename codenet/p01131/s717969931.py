keylist = [
   [],
   ['.', ',', '!', '?', ' '],
   ['a', 'b', 'c'],
   ['d', 'e', 'f'],
   ['g', 'h', 'i'],
   ['j', 'k', 'l'],
   ['m', 'n', 'o'],
   ['p', 'q', 'r', 's'],
   ['t', 'u', 'v'],
   ['w', 'x', 'y', 'z']
]
for i in range(int(input())):
   output = ''
   for item in input().split('0'):
      if item == '':
         continue
      output += keylist[int(item[0])][len(item) % len(keylist[int(item[0])]) - 1]
   print(output)