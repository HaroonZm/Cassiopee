# Your code here!

while True:
   s = input()
   if s == "END OF INPUT": break
   
   s += " " #文字列の文末にスペースを加える
   #print(s)
   
   c = 0
   for i in range(len(s)):
      #print(s[i])
      if s[i] == ' ':
         print(c, end = "")
         c = 0
         continue
      c += 1
   print("")