from sys import stdin

def to_alpha(n: int) -> str:
    chars = []
    while n:
        n -= 1
        chars.append(chr(97 + n % 26))
        n //= 26
    return ''.join(reversed(chars))

print(to_alpha(int(stdin.readline())))