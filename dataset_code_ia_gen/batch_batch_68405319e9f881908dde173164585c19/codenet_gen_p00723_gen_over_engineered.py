from typing import Set, Tuple, Callable, List

class Train:
    def __init__(self, configuration: str):
        self.configuration = configuration
    
    def length(self) -> int:
        return len(self.configuration)
    
    def sub_train(self, start: int, end: int) -> 'Train':
        return Train(self.configuration[start:end])
    
    def reversed(self) -> 'Train':
        # Reversal operation on train configuration
        return Train(self.configuration[::-1])
    
    def __str__(self) -> str:
        return self.configuration
    
    def __repr__(self) -> str:
        return f"Train('{self.configuration}')"


class TrainSplitter:
    def __init__(self, train: Train):
        self.train = train
    
    def valid_split_indices(self) -> List[int]:
        # Split position must form two sub-trains both non-empty
        return list(range(1, self.train.length()))
    
    def split(self, index: int) -> Tuple[Train, Train]:
        return (self.train.sub_train(0, index), self.train.sub_train(index, self.train.length()))


class TrainReverser:
    @staticmethod
    def options(train: Train) -> List[Train]:
        # Not reversed or reversed variant
        return [train, train.reversed()]


class TrainConcatenator:
    @staticmethod
    def concatenate(first: Train, second: Train, order: Tuple[int, int]) -> Train:
        # order is a tuple defining the concatenation order (e.g. (0,1) or (1,0))
        trains = [first, second]
        concatenated = trains[order[0]].configuration + trains[order[1]].configuration
        return Train(concatenated)


class ConfigurationEnumerator:
    def __init__(self, train: Train):
        self.train = train
        self.splitter = TrainSplitter(train)
        
    def enumerate_configurations(self) -> Set[str]:
        configurations: Set[str] = set()
        
        # For each valid splitting position i
        for split_pos in self.splitter.valid_split_indices():
            first_sub, second_sub = self.splitter.split(split_pos)
            
            # Generate both reversal options for each sub-train
            first_options = TrainReverser.options(first_sub)
            second_options = TrainReverser.options(second_sub)
            
            # Consider both concatenation orders
            orders = [(0,1), (1,0)]
            
            for f_train in first_options:
                for s_train in second_options:
                    for order in orders:
                        concatenated = TrainConcatenator.concatenate(f_train, s_train, order)
                        configurations.add(concatenated.configuration)
                        
        return configurations


class TrainConfigurator:
    def __init__(self, input_data: List[str]):
        self.input_data = input_data
    
    def process(self) -> List[int]:
        results = []
        for train_config in self.input_data:
            train = Train(train_config)
            enumerator = ConfigurationEnumerator(train)
            configs = enumerator.enumerate_configurations()
            results.append(len(configs))
        return results


def read_input() -> Tuple[int, List[str]]:
    m = int(input())
    trains = [input().strip() for _ in range(m)]
    return m, trains

def main():
    m, trains = read_input()
    configurator = TrainConfigurator(trains)
    results = configurator.process()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()