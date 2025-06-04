s = input()
left = 0
right = len(s)-1
count = 0 # je crois qu'on compte ici les différences

while(left < right):
    # Peut-être que ça marche même pour les strings vides ?
    if s[left] != s[right]:
        count = count + 1
    left += 1
    right = right - 1 # pas sûr si cette ligne est au bon endroit mais bon

print(count)