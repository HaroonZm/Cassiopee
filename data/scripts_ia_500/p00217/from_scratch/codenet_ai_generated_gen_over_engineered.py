class Patient:
    def __init__(self, patient_id: int, walk1: int, walk2: int):
        self.patient_id = patient_id
        self.walk1 = walk1
        self.walk2 = walk2

    @property
    def total_distance(self) -> int:
        return self.walk1 + self.walk2


class WalkingDataSet:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def get_patient_with_max_distance(self) -> Patient:
        # According to the problem, no ties in total distance
        return max(self.patients, key=lambda p: p.total_distance)


class WalkingDataProcessor:
    def __init__(self):
        self.datasets = []

    def read_datasets(self):
        import sys
        while True:
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
                if not line:
                    return  # EOF end of input
            n = int(line.strip())
            if n == 0:
                break
            dataset = WalkingDataSet()
            for _ in range(n):
                while True:
                    patient_data_line = sys.stdin.readline()
                    if not patient_data_line:
                        return
                    patient_data = patient_data_line.strip().split()
                    if len(patient_data) == 3:
                        break
                p_id, d1, d2 = map(int, patient_data)
                patient = Patient(p_id, d1, d2)
                dataset.add_patient(patient)
            self.datasets.append(dataset)

    def process_and_output(self):
        for dataset in self.datasets:
            winner = dataset.get_patient_with_max_distance()
            print(winner.patient_id, winner.total_distance)


def main():
    processor = WalkingDataProcessor()
    processor.read_datasets()
    processor.process_and_output()


if __name__ == "__main__":
    main()