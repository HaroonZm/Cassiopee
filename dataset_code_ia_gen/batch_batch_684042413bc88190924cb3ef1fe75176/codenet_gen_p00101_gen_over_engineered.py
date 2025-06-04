class TextProcessorInterface:
    def process(self, text: str) -> str:
        raise NotImplementedError("Subclasses should implement this!")

class WordReplacer(TextProcessorInterface):
    def __init__(self, target: str, replacement: str):
        self._target = target
        self._replacement = replacement
    
    def process(self, text: str) -> str:
        # Sophisticated replacement logic anticipating future rules:
        words = text.split(' ')
        replaced_words = []
        for word in words:
            # Potential future extension for case sensitivity or partial matches
            if word == self._target:
                replaced_words.append(self._replacement)
            else:
                replaced_words.append(word)
        return ' '.join(replaced_words)

class DatasetHandler:
    def __init__(self, processor: TextProcessorInterface):
        self._processor = processor
        self._datasets = []

    def load(self, count: int, lines: list[str]):
        if count != len(lines):
            raise ValueError("Number of lines does not match count")
        self._datasets = lines

    def apply_processing(self) -> list[str]:
        results = []
        for data in self._datasets:
            processed = self._processor.process(data)
            results.append(processed)
        return results

class InputOutputController:
    def __init__(self, handler: DatasetHandler):
        self._handler = handler

    def execute(self):
        n = int(input())
        datasets = [input() for _ in range(n)]
        self._handler.load(n, datasets)
        outputs = self._handler.apply_processing()
        for line in outputs:
            print(line)

def main():
    replacer = WordReplacer("Hoshino", "Hoshina")
    handler = DatasetHandler(replacer)
    controller = InputOutputController(handler)
    controller.execute()

if __name__ == "__main__":
    main()