import functools, itertools, operator

identity = lambda x: x

def overengineered_vowel_check():
    c = (lambda prompt="": functools.reduce(lambda acc, _: acc + _, itertools.islice(iter(lambda: input(prompt), None), 1), ""))()
    vowels = functools.reduce(operator.add, [["a", "i"], ["u", "e"], ["o"]])
    verdict = functools.reduce(
        lambda acc, v: acc or (c == v),
        vowels,
        False
    )
    print((lambda b: ['consonant', 'vowel'][b])(verdict))

overengineered_vowel_check()