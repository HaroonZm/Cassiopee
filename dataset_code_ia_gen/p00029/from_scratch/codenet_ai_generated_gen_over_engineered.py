class WordFrequencyAnalyzer:
    def __init__(self, text):
        self.text = text
    
    def tokenize(self):
        return self.text.split()
    
    def calculate_frequencies(self, words):
        frequency_map = {}
        for word in words:
            frequency_map[word] = frequency_map.get(word, 0) + 1
        return frequency_map
    
    def get_most_frequent_word(self, frequency_map):
        most_freq_word = None
        highest_freq = -1
        for word, freq in frequency_map.items():
            if freq > highest_freq:
                highest_freq = freq
                most_freq_word = word
        return most_freq_word

class WordLengthAnalyzer:
    def __init__(self, words):
        self.words = words
    
    def get_longest_word(self):
        longest_word = None
        max_length = -1
        for word in self.words:
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word
        return longest_word

class TextAnalyzerFacade:
    def __init__(self, text):
        self.text = text
    
    def analyze(self):
        freq_analyzer = WordFrequencyAnalyzer(self.text)
        words = freq_analyzer.tokenize()
        
        freq_map = freq_analyzer.calculate_frequencies(words)
        most_frequent_word = freq_analyzer.get_most_frequent_word(freq_map)
        
        length_analyzer = WordLengthAnalyzer(words)
        longest_word = length_analyzer.get_longest_word()
        
        return most_frequent_word, longest_word

def main():
    text = input().strip()
    analyzer = TextAnalyzerFacade(text)
    most_frequent_word, longest_word = analyzer.analyze()
    print(most_frequent_word, longest_word)

if __name__ == '__main__':
    main()