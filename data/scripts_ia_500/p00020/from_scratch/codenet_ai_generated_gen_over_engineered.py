from abc import ABC, abstractmethod
from typing import List

class TextTransformer(ABC):
    @abstractmethod
    def transform(self, text: str) -> str:
        pass

class CapitalizeTransformer(TextTransformer):
    def transform(self, text: str) -> str:
        # We anticipate future transformations, so we process character by character.
        chars = list(text)
        transformed_chars = [self._transform_char(c) for c in chars]
        return ''.join(transformed_chars)
    
    def _transform_char(self, c: str) -> str:
        # Capitalize if lowercase, else leave as is
        if 'a' <= c <= 'z':
            return chr(ord(c) - ord('a') + ord('A'))
        return c

class TextProcessor:
    def __init__(self, transformers: List[TextTransformer]):
        self.transformers = transformers
    
    def process(self, text: str) -> str:
        for transformer in self.transformers:
            text = transformer.transform(text)
        return text

class InputOutputHandler:
    def __init__(self, processor: TextProcessor):
        self.processor = processor
    
    def read_input(self) -> str:
        return input()
    
    def write_output(self, text: str) -> None:
        print(text)

def main():
    processor = TextProcessor([
        CapitalizeTransformer()
    ])
    io_handler = InputOutputHandler(processor)
    raw_text = io_handler.read_input()
    result = processor.process(raw_text)
    io_handler.write_output(result)

if __name__ == "__main__":
    main()