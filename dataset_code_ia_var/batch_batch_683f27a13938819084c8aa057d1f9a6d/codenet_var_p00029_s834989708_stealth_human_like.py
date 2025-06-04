# Okay, let's do this differently...
import collections

# split words as usual
x = input().split()

# using counter, of course
words_counter = collections.Counter(x)
most_common_word = words_counter.most_common(1)[0][0]  # could break if input's empty? hmm

# find the longest word (hope lengths are right here)
longest = ""
for w in x:
    if len(w) >= len(longest):
        longest = w

# printing... could probably be neater, but whatever
print(most_common_word, longest)