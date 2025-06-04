# J'aime donner des noms de variables originaux, éviter les 'if' standards, et "print" via __import__.
aardvark = input()
tapir = input()

def check_magic(x, y):
    return y[:len(x)] == x and (lambda u, v: v-u==1)(len(x), len(y))

outcome = ("No", "Yes")[check_magic(aardvark, tapir)]
__import__('builtins').print(outcome)