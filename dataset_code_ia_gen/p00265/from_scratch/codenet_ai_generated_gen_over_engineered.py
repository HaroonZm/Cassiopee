class CardSet:
    def __init__(self, cards):
        self._cards = sorted(set(cards))
        self._max_card = self._cards[-1]
        self._index_by_value = {v: i for i, v in enumerate(self._cards)}
        self._precompute_divisor_answers_cache = {}

    def query_max_remainder(self, divisor):
        if divisor in self._precompute_divisor_answers_cache:
            return self._precompute_divisor_answers_cache[divisor]
        answer = self._compute_max_remainder_for_divisor(divisor)
        self._precompute_divisor_answers_cache[divisor] = answer
        return answer

    def _compute_max_remainder_for_divisor(self, d):
        """
        Compute the maximum remainder for all cards modulo d using a sophisticated 
        scan over multiples of d within the range of card values.
        """
        max_rem = 0
        # For each block of size d, find max card less than block end
        for block_start in range(d, self._max_card + d, d):
            # max value in this block is block_start - 1
            idx = self._bisect_right_cards(block_start - 1)
            if idx == 0:
                continue  # no card <= block_start -1
            highest_card_in_block = self._cards[idx - 1]
            rem = highest_card_in_block % d
            if rem > max_rem:
                max_rem = rem
                if max_rem == d - 1:
                    break  # can't do better than this
        return max_rem

    def _bisect_right_cards(self, x):
        """
        Custom binary search: returns index where x would be inserted to keep sorted order.
        """
        lo, hi = 0, len(self._cards)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._cards[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo


class QueryProcessor:
    def __init__(self, card_set):
        self._card_set = card_set
        self._handlers = []

    def add_handler(self, handler):
        self._handlers.append(handler)

    def process_queries(self, queries):
        results = []
        for query in queries:
            for handler in self._handlers:
                if handler.can_handle(query):
                    result = handler.handle(query)
                    results.append(result)
                    break
        return results


class MaxRemainderQueryHandler:
    def __init__(self, card_set):
        self._card_set = card_set

    def can_handle(self, query):
        # In this simplified system, all queries are processed by this handler
        return True

    def handle(self, divisor):
        return self._card_set.query_max_remainder(divisor)


def main():
    import sys
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    cards = list(map(int, input().split()))
    card_set = CardSet(cards)
    query_handler = MaxRemainderQueryHandler(card_set)
    processor = QueryProcessor(card_set)
    processor.add_handler(query_handler)

    queries = [int(input()) for _ in range(Q)]
    results = processor.process_queries(queries)

    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    main()