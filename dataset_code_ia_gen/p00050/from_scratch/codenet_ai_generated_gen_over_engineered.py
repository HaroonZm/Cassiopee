class FruitWordSwapper:
    def __init__(self, swap_map):
        self.swap_map = swap_map
        self._compile_patterns()
    
    def _compile_patterns(self):
        import re
        # Create a regex pattern to match any of the keys as whole words
        pattern_words = map(lambda w: r'\b' + w + r'\b', self.swap_map.keys())
        self.pattern = re.compile('|'.join(pattern_words))
    
    def swap(self, text):
        return self.pattern.sub(self._replacer, text)
    
    def _replacer(self, match):
        word = match.group(0)
        return self.swap_map[word]

class FruitWordSwapFactory:
    @staticmethod
    def create_apple_peach_swapper():
        # Define mapping to swap both ways
        return FruitWordSwapper({
            'apple': 'peach',
            'peach': 'apple'
        })

class FruitWordSwapFacade:
    def __init__(self):
        self.swapper = FruitWordSwapFactory.create_apple_peach_swapper()
    
    def process(self, text):
        return self.swapper.swap(text)

if __name__ == '__main__':
    import sys
    input_text = sys.stdin.readline().rstrip('\n')
    facade = FruitWordSwapFacade()
    output_text = facade.process(input_text)
    print(output_text)