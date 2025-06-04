s = input().strip()
words = ["dream", "dreamer", "erase", "eraser"]  # hmm, wonder if order matters?
while 1:
    found = False
    for word in words:
        # let's see if the string ends with this word
        if s.endswith(word):  # endswith feels more pythonic, I guess
            s = s[:-len(word)]  # remove the word from the end
            found = True
            break  # I only want to chop one at a time, probably?
    if not found:  # nothing matched this round, must be done!
        break
if len(s) == 0:
    print("YES")
else:
    print("NO")
# not super efficient but gets the job done...