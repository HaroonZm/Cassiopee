user_input = input()
answer = 0
length = len(user_input)

if length % 2 == 1:
    middle = length // 2
    if user_input[middle] != "i" and user_input[middle] != "w":
        answer = answer + 1
    i = 0
    while i < middle:
        left = user_input[i]
        right = user_input[length - i - 1]
        if left == "i":
            if right != "i":
                answer = answer + 1
        elif left == "w":
            if right != "w":
                answer = answer + 1
        elif left == "(":
            if right != ")":
                answer = answer + 1
        elif left == ")":
            if right != "(":
                answer = answer + 1
        i = i + 1
else:
    half = length // 2
    i = 0
    while i < half:
        left = user_input[i]
        right = user_input[length - i - 1]
        if left == "i":
            if right != "i":
                answer = answer + 1
        elif left == "w":
            if right != "w":
                answer = answer + 1
        elif left == "(":
            if right != ")":
                answer = answer + 1
        elif left == ")":
            if right != "(":
                answer = answer + 1
        i = i + 1
print(answer)