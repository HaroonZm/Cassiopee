#!/usr/bin/env python3
flip = { 'i': 'i', 'w': 'w', '(': ')', ')': '(' }
s = input()
result = 0
for i in range((len(s) + 1) // 2):
    result += (flip[s[i]] != s[len(s) - i - 1])
print(result)