a = input()
def transform(text):
    text = text.replace('apple', 'AAAAA')
    text = text.replace('peach', 'apple')
    return text.replace('AAAAA', 'peach')
print(transform(a))