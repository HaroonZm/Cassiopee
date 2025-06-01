class WeightScale:
    class WeightSet:
        def __init__(self, weights):
            self.weights = sorted(weights)

        def total_weight(self):
            return sum(self.weights)

        def __iter__(self):
            return iter(self.weights)

    class WeightBalancer:
        def __init__(self, available_weights):
            self.available_weights = available_weights
            self.max_weight = sum(available_weights)

        def find_weights_for(self, target_weight):
            if not (0 <= target_weight <= self.max_weight):
                raise ValueError("Target weight out of bounds")

            result_weights = []
            remaining = target_weight
            # Greedy approach using binary weights by checking bits
            for w in reversed(self.available_weights):
                if remaining >= w:
                    remaining -= w
                    result_weights.append(w)

            result_weights.sort()
            return WeightScale.WeightSet(result_weights)

    def __init__(self):
        # Predefined 10 weights as per problem statement
        self.weights = [2**i for i in range(10)]
        self.balancer = WeightScale.WeightBalancer(self.weights)

    def balance(self, item_weight):
        return self.balancer.find_weights_for(item_weight)


def main():
    import sys
    scale = WeightScale()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        weight = int(line)
        balanced_set = scale.balance(weight)
        print(" ".join(str(w) for w in balanced_set))


if __name__ == "__main__":
    main()