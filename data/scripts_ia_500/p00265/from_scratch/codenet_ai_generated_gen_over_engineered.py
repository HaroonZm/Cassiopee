class CardSet:
    def __init__(self, cards):
        # Stocke les cartes uniques et trie pour un accès efficace
        self.cards = sorted(set(cards))
        self.max_card = self.cards[-1] if self.cards else 0
        # Pré-calcul d'une structure pour accélérer les recherches
        self.index_by_value = {v: i for i, v in enumerate(self.cards)}
    
    def max_remainder(self, modulo):
        """
        Calcule le reste maximal modulo 'modulo' parmi les cartes.
        Utilise un algorithme sophistiqué qui évite de parcourir toutes les cartes pour chaque requête.
        """
        max_r = 0
        max_c = self.max_card
        
        # Nous parcourons les multiples de modulo jusqu'à max_card
        # pour trouver le plus grand reste possible parmi les cartes.
        for base in range(modulo, max_c + modulo, modulo):
            # Trouve le plus grand élément dans cards < base
            # car ce sera le candidat à avoir un reste important (car remainder = card - base + modulo)
            idx = self._bisect_left(base)
            if idx > 0:
                candidate = self.cards[idx - 1]
                r = candidate % modulo
                if r > max_r:
                    max_r = r
                    if max_r == modulo - 1:
                        break  # Meilleur reste possible trouvé, on peut s'arrêter
            
        return max_r
    
    def _bisect_left(self, x):
        """
        Implémentation personnalisée de bisect_left pour une abstraction complète.
        """
        low, high = 0, len(self.cards)
        while low < high:
            mid = (low + high) // 2
            if self.cards[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low


class QueryProcessor:
    def __init__(self, card_set):
        self.card_set = card_set
        self.answered = set()
    
    def process_queries(self, queries):
        results = []
        for q in queries:
            if q not in self.answered:
                rem = self.card_set.max_remainder(q)
                self.answered.add(q)
                results.append(rem)
            else:
                # La spécification indique que mêmes questions ne seront pas posées deux fois,
                # mais on anticipe une extension ici.
                results.append(self.card_set.max_remainder(q))
        return results


def main():
    import sys
    input_data = sys.stdin.read().split()
    N, Q = int(input_data[0]), int(input_data[1])
    cards = list(map(int, input_data[2:2+N]))
    queries = list(map(int, input_data[2+N:2+N+Q]))
    
    card_set = CardSet(cards)
    processor = QueryProcessor(card_set)
    results = processor.process_queries(queries)
    
    print('\n'.join(map(str, results)))


if __name__ == '__main__':
    main()