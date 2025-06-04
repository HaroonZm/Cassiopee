class Vector(tuple):

    def __neg__(self):
        return Vector([-component for component in self])

    def __abs__(self):
        return sum(component ** 2 for component in self) ** 0.5

    def __add__(self, other_vector):
        if len(self) != len(other_vector):
            raise ValueError("Vectors must have the same dimension.")
        return Vector([component_self + component_other for component_self, component_other in zip(self, other_vector)])

    def __sub__(self, other_vector):
        return self.__add__(-other_vector)

    def norm(self):
        magnitude = abs(self)
        return Vector([component / magnitude for component in self])

    def __mul__(self, other_vector):
        """Dot product of two vectors"""
        if len(self) != len(other_vector):
            raise ValueError("Vectors must have the same dimension.")
        return round(sum(component_self * component_other for component_self, component_other in zip(self, other_vector)), 14)


def main():
    while True:
        number_of_points_input = input()
        try:
            number_of_points = int(number_of_points_input)
        except:
            continue
        
        if number_of_points == 0:
            break

        list_of_vectors = []
        for _ in range(number_of_points):
            raw_coordinates = input()
            vector_components = list(map(int, raw_coordinates.split()))
            list_of_vectors.append(Vector(vector_components))

        sequence_of_vectors = [
            Vector([0, -1]),
            Vector([0, 0])
        ]

        while len(list_of_vectors) > 0:
            previous_direction = sequence_of_vectors[-1] - sequence_of_vectors[-2]
            
            list_of_vectors.sort(
                key=lambda candidate_vector: abs(candidate_vector - sequence_of_vectors[-1]),
                reverse=True
            )

            list_of_vectors.sort(
                key=lambda candidate_vector: (candidate_vector - sequence_of_vectors[-1]).norm() * previous_direction.norm()
            )

            next_vector = list_of_vectors.pop()
            sequence_of_vectors.append(next_vector)

        total_distance = sum(
            abs(current_vector - previous_vector)
            for previous_vector, current_vector in zip(sequence_of_vectors[1:], sequence_of_vectors[2:])
        )

        print(round(total_distance, 1))


if __name__ == "__main__":
    main()