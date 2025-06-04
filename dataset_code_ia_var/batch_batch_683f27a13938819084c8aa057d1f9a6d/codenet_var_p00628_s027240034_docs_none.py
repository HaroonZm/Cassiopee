while True:
   s = input()
   if s == "END OF INPUT": break
   s += " "
   c = 0
   for i in range(len(s)):
      if s[i] == ' ':
         print(c, end = "")
         c = 0
         continue
      c += 1
   print("")