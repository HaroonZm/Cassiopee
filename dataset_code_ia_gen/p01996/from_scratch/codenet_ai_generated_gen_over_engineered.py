class Seat:
    def __init__(self, position: int):
        self.position = position
        self.occupied_by = None  # Will hold Student or None

    def is_occupied(self):
        return self.occupied_by is not None

    def seat_student(self, student: 'Student'):
        self.occupied_by = student
        student.seated_at = self

    def remove_student(self):
        student = self.occupied_by
        self.occupied_by = None
        if student:
            student.seated_at = None
        return student

class Student:
    def __init__(self, id_: int):
        self.id = id_
        self.seated_at: Seat | None = None

class Classroom:
    def __init__(self, total_seats: int):
        self.seats = [Seat(pos) for pos in range(1, total_seats + 1)]

    def get_seat(self, position: int) -> Seat:
        return self.seats[position - 1]

    def first_empty_seat(self):
        for seat in self.seats:
            if not seat.is_occupied():
                return seat
        return None

    def seats_occupied_positions(self):
        return [seat.position for seat in self.seats if seat.is_occupied()]

class TestSeatingController:
    def __init__(self, N: int, M: int, seated_positions: list[int]):
        self.N = N
        self.M = M
        self.classroom = Classroom(N)
        self.students = [Student(i+1) for i in range(M)]
        # Assign initial seating
        for student, pos in zip(self.students, seated_positions):
            self.classroom.get_seat(pos).seat_student(student)

    def condition_met(self):
        # Check if seats 1..M are all occupied
        return all(self.classroom.get_seat(pos).is_occupied() for pos in range(1, self.M + 1))

    def get_last_student(self):
        # Get the student sitting at the maximal occupied seat position
        max_pos = max((student.seated_at.position for student in self.students if student.seated_at is not None), default=None)
        if max_pos is None:
            return None
        return self.classroom.get_seat(max_pos).occupied_by

    def perform_operation(self):
        # Move the last student to the earliest empty seat
        last_student = self.get_last_student()
        if last_student is None:
            return False
        last_student_current_seat = last_student.seated_at
        # Find earliest empty seat
        empty_seat = self.classroom.first_empty_seat()
        if empty_seat is None:
            return False
        # Remove last student from current seat
        last_student_current_seat.remove_student()
        # Seat last student in earliest empty seat
        empty_seat.seat_student(last_student)
        return True

    def calculate_min_operations(self):
        operations = 0
        while not self.condition_met():
            if not self.perform_operation():
                break
            operations += 1
        return operations

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    seated_positions = list(map(int, input().split()))
    controller = TestSeatingController(N, M, seated_positions)
    print(controller.calculate_min_operations())

if __name__ == "__main__":
    main()