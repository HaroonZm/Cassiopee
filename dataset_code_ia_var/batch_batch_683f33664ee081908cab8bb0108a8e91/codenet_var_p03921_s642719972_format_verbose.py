number_of_people, number_of_languages = map(int, input().split())

class DisjointSetUnion:
    def __init__(self, number_of_elements):
        self.set_size = number_of_elements
        self.parent_or_size = [-1] * number_of_elements

    def find_representative(self, element_index):
        if self.parent_or_size[element_index] < 0:
            return element_index
        else:
            self.parent_or_size[element_index] = self.find_representative(self.parent_or_size[element_index])
            return self.parent_or_size[element_index]

    def unite_sets(self, element_index_a, element_index_b):
        root_a = self.find_representative(element_index_a)
        root_b = self.find_representative(element_index_b)

        if root_a == root_b:
            return

        if self.parent_or_size[root_a] > self.parent_or_size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent_or_size[root_a] += self.parent_or_size[root_b]
        self.parent_or_size[root_b] = root_a

    def size_of_set(self, element_index):
        return -self.parent_or_size[self.find_representative(element_index)]

    def are_in_same_set(self, element_index_a, element_index_b):
        return self.find_representative(element_index_a) == self.find_representative(element_index_b)

    def set_members(self, element_index):
        root = self.find_representative(element_index)
        return [i for i in range(self.set_size) if self.find_representative(i) == root]

    def all_roots(self):
        return [i for i, parent_value in enumerate(self.parent_or_size) if parent_value < 0]

    def total_number_of_sets(self):
        return len(self.all_roots())

    def all_groups(self):
        return {root: self.set_members(root) for root in self.all_roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(root, self.set_members(root)) for root in self.all_roots())

disjoint_set_union = DisjointSetUnion(number_of_people)

language_to_people_mapping = [[] for _ in range(number_of_languages)]

for person_index in range(number_of_people):
    input_list = list(map(int, input().split()))
    number_of_languages_spoken_by_person = input_list.pop(0)
    for language_offset in range(number_of_languages_spoken_by_person):
        language_index = input_list[language_offset] - 1
        if len(language_to_people_mapping[language_index]) == 0:
            language_to_people_mapping[language_index].append(person_index)
        else:
            first_person_with_language = language_to_people_mapping[language_index][0]
            disjoint_set_union.unite_sets(first_person_with_language, person_index)

if disjoint_set_union.total_number_of_sets() == 1:
    print("YES")
else:
    print("NO")