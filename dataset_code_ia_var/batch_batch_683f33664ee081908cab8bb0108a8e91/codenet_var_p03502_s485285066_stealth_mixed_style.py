def check(n):
    s = 0
    for i in n:
        s += int(i)
    return int(n) % s

class Answer:
    def reply(self, val):
        if val == 0:
            return "Yes"
        else:
            return "No"

resp = Answer()
print(resp.reply(check(input())))