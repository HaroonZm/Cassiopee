from itertools import groupby
import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.subtree_size = 0  # Taille du sous-arbre incluant ce nœud

class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def add_string(self, input_string):
        current_node = self.root_node
        current_node.subtree_size += 1
        for character in input_string:
            character_index = ord(character) - ord('a')
            if character_index not in current_node.children:
                current_node.children[character_index] = TrieNode()
            current_node = current_node.children[character_index]
            current_node.subtree_size += 1
        # Marquer la fin de la chaîne par un enfant spécial indexé à 26
        current_node.children[26] = TrieNode()
        current_node.children[26].subtree_size += 1

    def compute_character_distribution_matrix(self, base_string):
        # Matrice 26x27 (lettres et fin de mot), pour compter les branches à chaque lettre
        character_distribution_matrix = [ [0] * 27 for _ in range(26) ]
        current_node = self.root_node
        for character in base_string:
            character_index = ord(character) - ord('a')
            character_distribution_row = character_distribution_matrix[character_index]
            for child_index, child_node in current_node.children.items():
                character_distribution_row[child_index] += child_node.subtree_size
            current_node = current_node.children[character_index]
        return character_distribution_matrix

def main():
    input_reader = sys.stdin.readline
    number_of_strings = int(input_reader())
    list_of_strings = [ input_reader().rstrip('\n') for _ in range(number_of_strings) ]

    trie_structure = Trie()
    for string_entry in list_of_strings:
        trie_structure.add_string(string_entry)

    number_of_queries = int(input_reader())
    query_entries = [ input_reader().split() for _ in range(number_of_queries) ]
    query_answers = [ -1 ] * number_of_queries

    # Tri des indices de requêtes par base_string_index pour groupby efficace
    sorted_query_indices = sorted( range(number_of_queries), key=lambda idx: query_entries[idx][0] )

    for base_index_value, group_indices in groupby(sorted_query_indices, key=lambda idx: query_entries[idx][0]):
        base_string_index = int(base_index_value) - 1
        character_distribution_matrix = trie_structure.compute_character_distribution_matrix( list_of_strings[base_string_index] )
        for query_index in group_indices:
            _, pattern_string = query_entries[query_index]
            pattern_character_indices = [ ord(character) - ord('a') for character in pattern_string ]
            current_answer = 1
            for pattern_position, current_pattern_index in enumerate(pattern_character_indices):
                for previous_pattern_index in pattern_character_indices[:pattern_position]:
                    current_answer += character_distribution_matrix[current_pattern_index][previous_pattern_index]
                current_answer += character_distribution_matrix[current_pattern_index][26]
            query_answers[query_index] = current_answer

    print( "\n".join( map(str, query_answers) ) )

main()