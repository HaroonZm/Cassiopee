class StringManipulator:
    def __init__(self, data: str):
        self._data = data

    def transform(self, strategy: 'TransformationStrategy') -> str:
        return strategy.apply(self._data)

class TransformationStrategy:
    def apply(self, data: str) -> str:
        raise NotImplementedError("Subclasses should implement this!")

class ReverseStrategy(TransformationStrategy):
    def apply(self, data: str) -> str:
        return data[::-1]

class InputReader:
    def __init__(self, source):
        self._source = source

    def read(self) -> str:
        return self._source.readline().strip()

class OutputWriter:
    def __init__(self, sink):
        self._sink = sink

    def write(self, content: str):
        self._sink.write(content + "\n")
        self._sink.flush()

class Application:
    def __init__(self, input_reader: InputReader, output_writer: OutputWriter):
        self._input_reader = input_reader
        self._output_writer = output_writer
        self._manipulator = None
        self._strategy = None

    def configure(self, manipulator: StringManipulator, strategy: TransformationStrategy):
        self._manipulator = manipulator
        self._strategy = strategy

    def run(self):
        input_str = self._input_reader.read()
        self._manipulator = StringManipulator(input_str)
        self._strategy = ReverseStrategy()
        reversed_str = self._manipulator.transform(self._strategy)
        self._output_writer.write(reversed_str)

if __name__ == "__main__":
    import sys
    app = Application(InputReader(sys.stdin), OutputWriter(sys.stdout))
    app.run()