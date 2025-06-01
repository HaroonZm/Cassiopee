s=input()
tmp = s.replace('peach', 'X')
def swap_apple_peach(text):
    return text.replace('apple', 'peach')
res = swap_apple_peach(tmp)
print(res.replace('X', 'apple'))