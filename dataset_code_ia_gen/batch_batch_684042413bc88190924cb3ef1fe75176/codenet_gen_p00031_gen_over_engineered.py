class WeightScale:
    class WeightSet:
        def __init__(self, weights):
            self._weights = sorted(weights)

        def __iter__(self):
            return iter(self._weights)

        def total_weight(self):
            return sum(self._weights)

    class WeightBalancer:
        def __init__(self, weights):
            self.weights = weights

        def find_weights_for_right_plate(self, target_weight):
            # Using the binary representation approach since weights are powers of two
            selected_weights = []
            remainder = target_weight
            for w in reversed(self.weights):
                if w <= remainder:
                    selected_weights.append(w)
                    remainder -= w
                if remainder == 0:
                    break
            return sorted(selected_weights)

    def __init__(self):
        # Define weights as powers of two from 1 to 512 grams
        powers_of_two = [2 ** i for i in range(10)]
        self.weight_set = self.WeightSet(powers_of_two)
        self.balancer = self.WeightBalancer(self.weight_set)

    def balance(self, target_weight):
        if target_weight > self.weight_set.total_weight():
            raise ValueError("Weight exceeds maximum measurable limit")
        # Since the problem states the right plate must balance the left plate's given item weight,
        # and weights are powers of two, we can directly use the binary decomposition.
        return self.balancer.find_weights_for_right_plate(target_weight)


class InputHandler:
    def __init__(self):
        self.scale = WeightScale()

    def process(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            target_weight = int(line)
            selected_weights = self.scale.balance(target_weight)
            print(' '.join(map(str, selected_weights)))


if __name__ == "__main__":
    handler = InputHandler()
    handler.process()