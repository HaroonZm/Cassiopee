import sys

used = set()
max_turns = 50
turn = 0

def print_and_flush(word):
    print("?" + word)
    sys.stdout.flush()

def is_valid_word(word):
    if len(word) < 1 or len(word) > 10:
        return False
    for c in word:
        if c < 'a' or c > 'z':
            return False
    return True

def is_ai_word_valid(ai_word, last_word):
    # AI word length between 1 and 2
    if len(ai_word) < 1 or len(ai_word) > 2:
        return False
    if not ai_word.islower():
        return False
    if ai_word in used:
        return False
    if ai_word[0] != last_word[-1]:
        return False
    return True

# Start with a simple initial word
my_word = "a"
used.add(my_word)
print_and_flush(my_word)
turn += 1

last_word = my_word

while turn < max_turns:
    ai_word = input()
    if ai_word in used:
        # AI repeated a word
        print("!OUT")
        sys.stdout.flush()
        break
    if not is_ai_word_valid(ai_word, last_word):
        print("!OUT")
        sys.stdout.flush()
        break
    used.add(ai_word)
    last_word = ai_word

    # Find next word to say
    # next word must start with last char of ai_word
    start_char = ai_word[-1]
    # Try to find a single-char word not used starting with start_char
    # To force AI to fail quickly, use single char words
    found = False
    for c in "abcdefghijklmnopqrstuvwxyz":
        candidate = start_char + c  # two-letter word
        if candidate not in used and is_valid_word(candidate) and candidate[0] == start_char:
            my_word = candidate
            used.add(my_word)
            print_and_flush(my_word)
            turn += 1
            last_word = my_word
            found = True
            break
    if not found:
        # no word found, just print a word starting with start_char
        my_word = start_char
        if my_word in used:
            # no possible move, end here
            break
        used.add(my_word)
        print_and_flush(my_word)
        turn += 1
        last_word = my_word