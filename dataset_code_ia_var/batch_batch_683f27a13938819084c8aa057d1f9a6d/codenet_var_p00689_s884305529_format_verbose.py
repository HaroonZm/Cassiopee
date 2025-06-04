class Vector(tuple):

    def __neg__(self):
        return Vector([-value for value in self])

    def __abs__(self):
        return sum(coordinate ** 2 for coordinate in self) ** 0.5

    def __add__(self, other_vector):
        if len(self) != len(other_vector):
            raise ValueError("Same dimension is required.")
        return Vector([x1 + x2 for x1, x2 in zip(self, other_vector)])

    def __sub__(self, other_vector):
        return self.__add__(-other_vector)

    def norm(self):
        vector_length = abs(self)
        return Vector([component / vector_length for component in self])

    def __mul__(self, other_vector):
        if len(self) != len(other_vector):
            raise ValueError("Same dimension is required.")
        return round(sum(x1 * x2 for x1, x2 in zip(self, other_vector)), 14)


def main():

    while True:

        number_of_points_input = input()
        if int(number_of_points_input) == 0:
            break

        number_of_points = int(number_of_points_input)

        points_list = []
        for _ in range(number_of_points):
            point_coordinates = list(map(int, input().split()))
            point_vector = Vector(point_coordinates)
            points_list.append(point_vector)

        constructed_sequence = [Vector([0, -1]), Vector([0, 0])]

        while len(points_list) != 0:
            previous_direction = constructed_sequence[-1] - constructed_sequence[-2]

            points_list.sort(
                key=lambda current_point: abs(current_point - constructed_sequence[-1]),
                reverse=True
            )

            points_list.sort(
                key=lambda current_point: (current_point - constructed_sequence[-1]).norm() * previous_direction.norm()
            )

            constructed_sequence.append(points_list.pop())

        total_distance = sum(
            abs(point_b - point_a)
            for point_a, point_b in zip(constructed_sequence[1:], constructed_sequence[2:])
        )
        print(round(total_distance, 1))


if __name__ == "__main__":
    main()