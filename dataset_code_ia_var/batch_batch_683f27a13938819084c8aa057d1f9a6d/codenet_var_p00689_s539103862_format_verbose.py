class Vector(tuple):

    def __neg__(self):
        return Vector([-coordinate for coordinate in self])

    def __abs__(self):
        return sum(coordinate ** 2 for coordinate in self) ** 0.5

    def __add__(self, other_vector):
        if len(self) != len(other_vector):
            raise ValueError("Same dimension is required.")
        return Vector([coord_self + coord_other for coord_self, coord_other in zip(self, other_vector)])

    def __sub__(self, other_vector):
        return self.__add__(-other_vector)

    def norm(self):
        vector_length = self.__abs__()
        return Vector([coordinate / vector_length for coordinate in self])
    
    def __mul__(self, other_vector):
        if len(self) != len(other_vector):
            raise ValueError("Same dimension is required.")
        return round(sum(coord_self * coord_other for coord_self, coord_other in zip(self, other_vector)), 14)
        

def main():
    while True:
        number_of_points_input = input()
        if number_of_points_input == 0 or number_of_points_input == '0':
            break

        number_of_points = int(number_of_points_input)
        list_of_points = [
            Vector(list(map(int, input().split())))
            for _ in range(number_of_points)
        ]

        trajectory_sequence = [
            Vector([0, -1]),
            Vector([0, 0])
        ]

        while len(list_of_points) != 0:
            previous_direction = trajectory_sequence[-1] - trajectory_sequence[-2]

            list_of_points.sort(
                key=lambda candidate_point: abs(candidate_point - trajectory_sequence[-1]),
                reverse=True
            )
            list_of_points.sort(
                key=lambda candidate_point: (candidate_point - trajectory_sequence[-1]).norm() * previous_direction.norm()
            )

            point_norms = [
                (candidate_point - trajectory_sequence[-1]).norm() * previous_direction.norm()
                for candidate_point in list_of_points
            ]

            selected_next_point = list_of_points.pop()
            trajectory_sequence.append(selected_next_point)

        total_path_length = sum(
            abs(second_point - first_point)
            for first_point, second_point in zip(trajectory_sequence[1:], trajectory_sequence[2:])
        )
        print(round(total_path_length, 1))
        

if __name__ == "__main__":
    main()