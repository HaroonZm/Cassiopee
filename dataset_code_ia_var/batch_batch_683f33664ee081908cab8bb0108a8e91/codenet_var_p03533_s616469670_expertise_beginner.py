input_string = input()
input_list = list(input_string)
akihabara = list("AKIHABARA")
a_count = 0

# Compter le nombre de "A"
for c in input_list:
    if c == "A":
        a_count += 1

diff = len(akihabara) - len(input_list)
# Si l'entrée est plus longue ou trop courte
if diff < 0 or len(input_list) + (4 - a_count) < 9:
    print("NO")
elif input_list == akihabara:
    print("YES")
else:
    copy_input = input_list[:]
    i = 0
    while i < len(copy_input):
        if copy_input[i] != akihabara[i]:
            copy_input.insert(i, "A")
        i += 1
        if len(copy_input) == 9:
            break
    while len(copy_input) < 9:
        copy_input.append("A")
    if copy_input == akihabara:
        print("YES")
    else:
        print("NO")