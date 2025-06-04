user_input = input()
letters = set()
i = 0
while i < len(user_input):
    letters.add(user_input[i])
    i = i + 2

if len(letters) == 1:
    print("Yes")
else:
    print("No")