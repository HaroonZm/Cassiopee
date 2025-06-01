from typing import List, Tuple, Iterator
import sys


class SurveyData:
    def __init__(self, n_students: int, m_places: int, preferences: List[List[int]]):
        self.n_students = n_students
        self.m_places = m_places
        self.preferences = preferences


class PlacePopularity:
    def __init__(self, place_id: int, popularity: int):
        self.place_id = place_id
        self.popularity = popularity

    def __lt__(self, other: 'PlacePopularity') -> bool:
        # Sort descending popularity, tie break ascending place_id
        if self.popularity != other.popularity:
            return self.popularity > other.popularity
        return self.place_id < other.place_id


class SurveyProcessor:
    def __init__(self, survey_data: SurveyData):
        self.survey_data = survey_data

    def compute_popularity(self) -> List[PlacePopularity]:
        popularity_counts = [0] * self.survey_data.m_places
        for student_prefs in self.survey_data.preferences:
            for i, pref in enumerate(student_prefs):
                popularity_counts[i] += pref
        return [
            PlacePopularity(place_id=i + 1, popularity=pop)
            for i, pop in enumerate(popularity_counts)
        ]

    def sorted_places_by_popularity(self) -> List[int]:
        popularities = self.compute_popularity()
        # Python sort is stable, but we rely on __lt__ for the correct ordering.
        popularities.sort()
        return [p.place_id for p in popularities]


class InputParser:
    def __init__(self, source: Iterator[str]):
        self.source = source

    def read_next_dataset(self) -> SurveyData:
        while True:
            line = next(self.source).strip()
            if line == '':
                continue
            n_m = line.split()
            if len(n_m) != 2:
                continue
            n, m = map(int, n_m)
            if n == 0 and m == 0:
                return None
            preferences = []
            read_lines = 0
            while read_lines < n:
                prefs_line = next(self.source).strip()
                if not prefs_line:
                    continue
                prefs = list(map(int, prefs_line.split()))
                if len(prefs) != m:
                    raise ValueError("Preference line length mismatch")
                preferences.append(prefs)
                read_lines += 1
            return SurveyData(n, m, preferences)


class SolutionRunner:
    def __init__(self, input_source: Iterator[str]):
        self.parser = InputParser(input_source)

    def run(self):
        while True:
            dataset = self.parser.read_next_dataset()
            if dataset is None:
                break
            processor = SurveyProcessor(dataset)
            sorted_places = processor.sorted_places_by_popularity()
            print(' '.join(map(str, sorted_places)))


def main():
    input_lines = (line for line in sys.stdin)
    runner = SolutionRunner(input_lines)
    runner.run()


if __name__ == "__main__":
    main()