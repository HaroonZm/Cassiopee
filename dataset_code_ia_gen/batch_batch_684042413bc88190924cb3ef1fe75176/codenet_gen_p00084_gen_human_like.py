import sys

text = sys.stdin.readline().strip()
for ch in ['.', ',']:
    text = text.replace(ch, ' ')
words = text.split()
result = [w for w in words if 3 <= len(w) <= 6]
print(' '.join(result))