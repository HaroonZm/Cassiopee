class StringReversalStrategy:
    def reverse(self, s: str) -> str:
        raise NotImplementedError("Subclasses should implement this!")

class SimpleSliceReversalStrategy(StringReversalStrategy):
    def reverse(self, s: str) -> str:
        return s[::-1]

class AbstractStringProcessor:
    def __init__(self, strategy: StringReversalStrategy):
        self._strategy = strategy

    def process(self, input_str: str) -> str:
        preprocessed = self._preprocess(input_str)
        reversed_str = self._strategy.reverse(preprocessed)
        postprocessed = self._postprocess(reversed_str)
        return postprocessed

    def _preprocess(self, s: str) -> str:
        # Placeholder for potential preprocessing steps
        return s.strip()

    def _postprocess(self, s: str) -> str:
        # Placeholder for potential postprocessing steps
        return s

class InputOutputHandler:
    def __init__(self, processor: AbstractStringProcessor):
        self._processor = processor

    def read_input(self) -> str:
        return input()

    def write_output(self, output_str: str):
        print(output_str)

    def execute(self):
        input_str = self.read_input()
        output_str = self._processor.process(input_str)
        self.write_output(output_str)

if __name__ == "__main__":
    strategy = SimpleSliceReversalStrategy()
    processor = AbstractStringProcessor(strategy)
    io_handler = InputOutputHandler(processor)
    io_handler.execute()