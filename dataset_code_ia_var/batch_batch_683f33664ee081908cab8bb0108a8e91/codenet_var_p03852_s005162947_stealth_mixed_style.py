def check(char): return 'vowel' if char in ('a','i','u','e','o') else 'consonant'
class Printer:
    @staticmethod
    def pr(msg): print(msg)
for item in [input()]:
    if item.lower() in ['a','i','u','e','o']: 
        result = 'vowel'
    else:
        result = check(item)
    Printer.pr(result)