s = input()
words = ["dream", "dreamer", "erase", "eraser"]

def f():
    t = s
    while 1:
        original = len(t)
        for idx, w in enumerate(words[::-1]):
            if t.endswith(w):
                t = t[:-len(w)]
                break
        else:
            if len(t)==0:
                return "YES"
            return "NO"
        if original==len(t):
            return "NO"

class Dummy:
    def run(self): return f()

x = Dummy()
print(x.run())