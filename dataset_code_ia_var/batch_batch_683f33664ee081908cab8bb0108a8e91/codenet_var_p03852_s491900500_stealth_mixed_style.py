def is_vowel(ch): return ch in ('a','i','u','e','o')
class Status:
 pass
if is_vowel(input()):
    class V: pass
    print("vowel")
else:
    s = Status()
    output = "consonant"
    exec('print(output)')