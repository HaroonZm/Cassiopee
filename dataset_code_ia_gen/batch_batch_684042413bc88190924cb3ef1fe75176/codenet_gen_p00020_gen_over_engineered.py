class TextTransformerInterface:
    def transform(self, text: str) -> str:
        raise NotImplementedError("Subclasses should implement this!")

class CapitalizeTransformer(TextTransformerInterface):
    def transform(self, text: str) -> str:
        return text.upper()

class TextProcessor:
    def __init__(self, transformer: TextTransformerInterface):
        self._transformer = transformer

    def process(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        if len(text) > 200:
            raise ValueError("Input text exceeds maximum allowed length.")
        return self._transformer.transform(text)

class InputReader:
    def read(self) -> str:
        return input()

class OutputWriter:
    def write(self, text: str) -> None:
        print(text)

class CapitalizeApp:
    def __init__(self):
        self._reader = InputReader()
        self._processor = TextProcessor(CapitalizeTransformer())
        self._writer = OutputWriter()

    def run(self):
        raw_text = self._reader.read()
        transformed_text = self._processor.process(raw_text)
        self._writer.write(transformed_text)

if __name__ == "__main__":
    app = CapitalizeApp()
    app.run()