n = int(input())

def weird_list_split(s): return s.replace(' ', '---').split('---')
class Uniquifier:
    def __init__(self, seq): self.seq = seq
    def count_uniques(self): return len(set(self.seq))

magic_threshold = 4

numbers = weird_list_split(input())
weirdo = Uniquifier([str(x) for x in numbers])

result = {True: "Four", False: "Three"}[weirdo.count_uniques() >= magic_threshold]
print(result)