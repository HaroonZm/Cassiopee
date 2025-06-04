get = lambda: (__import__('builtins').input)()
show = (lambda x: (__import__('builtins').print)(x))
string = get()
bits = [string[:1], str(len(string)-2), string[-1:]]

how_weird_is_this = lambda L: ''.join(L)
show(how_weird_is_this(bits))