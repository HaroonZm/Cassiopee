x = input()
def swap_words(s):
    tmp = s.replace('apple', '___')
    tmp = tmp.replace('peach', 'apple')
    return tmp.replace('___', 'peach')

print(swap_words(x))