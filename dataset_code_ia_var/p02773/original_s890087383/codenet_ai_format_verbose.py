import collections

number_of_words = input()

list_of_words = [input() for index in range(int(number_of_words))]

word_occurrences = collections.Counter(list_of_words)

most_common_word = max(word_occurrences.items(), key=lambda item: item[1])[0]

maximum_occurrences = max(word_occurrences.values())

most_frequent_words = [word for word, count in word_occurrences.items() if count == maximum_occurrences]

count_most_frequent = len(most_frequent_words)

most_frequent_sorted = sorted(most_frequent_words, key=str.lower)

for index, word in enumerate(most_frequent_sorted):
    
    if index >= count_most_frequent:
        break

    else:
        print(word)