def ReadInput():
  return input()

def Solve(x):
    return {'A':'T','C':'G',"T":'A','G':"C"}[x]

class Runner:
    def run(self):
        y = ReadInput()
        result = Solve(y)
        print(result)

if __name__ == "__main__":
    app = Runner()
    app.run()