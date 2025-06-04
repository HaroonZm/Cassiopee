alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]
possible_alphas = [1,3,5,7,9,11,15,17,19,21,23,25]

def decode(alpha, beta, code):
    message = ""
    for ch in code:
        if ch != " ":
            index = alphabet.index(ch)
            for i in range(26):
                if (alpha * i + beta) % 26 == index:
                    decoded_char = alphabet[i]
                    break
            message += decoded_char
        else:
            message += " "
    return message

n = int(raw_input())
for _ in range(n):
    code = raw_input()
    found = False
    for alpha in possible_alphas:
        for beta in range(26):
            decoded = decode(alpha, beta, code)
            if "that" in decoded or "this" in decoded:
                found = True
                break
        if found:
            break
    print decoded