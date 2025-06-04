S = input()

def count_diff(s):
    result = 0
    idx = 0
    while idx < len(s) - 1:
        if s[idx] != s[idx+1]:
            result = result + 1
        idx += 1
    return result

class Printer:
    @staticmethod
    def pr(r):
        print(r)

if S == "":
    Printer.pr(0)
else:
    x = count_diff(S)
    Printer.pr(x)