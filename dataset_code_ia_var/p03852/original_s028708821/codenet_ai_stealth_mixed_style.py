c = input()

def is_vowel(ch):
    return ch in ('a', 'e', 'i', 'o', 'u')

class Printer:
    def __init__(self, value):
        self.value = value
    def show(self):
        if self.value:
            print("vowel")
        else:
            print("consonant")
        print()

res = is_vowel(c)
printer = Printer(res)
printer.show()