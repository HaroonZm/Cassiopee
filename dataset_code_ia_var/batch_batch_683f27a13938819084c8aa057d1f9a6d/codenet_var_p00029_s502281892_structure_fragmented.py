def read_input():
    return input()

def split_input(text):
    return text.split()

def init_dict():
    return {}

def increment_word_count(dic, word):
    try:
        dic[word] += 1
    except:
        dic[word] = 1

def count_words(word_list, dic):
    for word in word_list:
        increment_word_count(dic, word)

def longest_word(word_list):
    return max(word_list, key=len)

def most_frequent_word(dic):
    return max(dic.items(), key=lambda x: x[1])

def print_result(freq_word, long_word):
    print(freq_word, long_word)

def main():
    text = read_input()
    word_list = split_input(text)
    dic = init_dict()
    count_words(word_list, dic)
    long_word = longest_word(word_list)
    freq_word = most_frequent_word(dic)[0]
    print_result(freq_word, long_word)

main()