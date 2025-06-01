count_palindromes = 0
while True:
    try:
        user_input = input()
        if user_input == user_input[::-1]:
            count_palindromes += 1
    except:
        break
print(count_palindromes)