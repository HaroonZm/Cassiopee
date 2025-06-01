x=input()
def rot_n(s, n):
    answer = ''
    for letter in s:
        answer += chr(ord('A') + (ord(letter)-ord('A')-n) % 26)
    return answer
print(rot_n(x, 3))