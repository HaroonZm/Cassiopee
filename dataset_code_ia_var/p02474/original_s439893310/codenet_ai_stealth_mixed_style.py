def f(): r=input();return eval(r.replace(' ','*'))
class X: pass
def main():
   x = X()
   while 1:
      res=[f()]
      for r in res:
         print(r)
      break
main()