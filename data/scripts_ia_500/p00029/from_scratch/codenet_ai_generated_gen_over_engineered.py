class TextProcessor:
    def __init__(self, text: str):
        self.text = text
        self.words = []
        self.frequency_map = {}

    def preprocess(self):
        self.words = self.text.split()

    def analyze_frequencies(self):
        for word in self.words:
            self.frequency_map[word] = self.frequency_map.get(word, 0) + 1

    def get_most_frequent_word(self):
        max_freq = -1
        most_freq_word = None
        for word, freq in self.frequency_map.items():
            if freq > max_freq:
                max_freq = freq
                most_freq_word = word
        return most_freq_word

    def get_longest_word(self):
        max_length = -1
        longest_word = None
        for word in self.words:
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word
        return longest_word


class TextAnalysisFacade:
    def __init__(self, text: str):
        self.processor = TextProcessor(text)
    
    def run(self):
        self.processor.preprocess()
        self.processor.analyze_frequencies()
        most_freq = self.processor.get_most_frequent_word()
        longest = self.processor.get_longest_word()
        return most_freq, longest

def input_text():
    return input()

def output_result(most_freq_word: str, longest_word: str):
    print(most_freq_word, longest_word)

def main():
    text = input_text()
    analysis = TextAnalysisFacade(text)
    most_freq_word, longest_word = analysis.run()
    output_result(most_freq_word, longest_word)

if __name__ == "__main__":
    main()