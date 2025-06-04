def myAnswer(S:str)-> str:
   dic = {"a":0,"b":0,"c":0}
   for s in S:
      dic[s]+= 1
   ans = sorted(dic.values(),reverse = True)
   return "NO" if(max(ans) - min(ans) >=2) else "YES"

def modelAnswer():
   return

def main():
   S = input()
   print(myAnswer(S))

if __name__ == '__main__':
   main()