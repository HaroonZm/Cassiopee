from collections import deque
from typing import List, Optional, Tuple


class Car:
    def __init__(self, car_id: int, park_duration: int, arrival_time: int):
        self.car_id = car_id
        self.park_duration = park_duration
        self.arrival_time = arrival_time
        self.departure_time = arrival_time + park_duration
        # park_position: None if not parked, else (space_index, level) where level=0 bottom,1 top
        self.park_position: Optional[Tuple[int, int]] = None
        # When parked on top, must wait bottom car to depart first
        self.waiting_for_lower = False


class ParkingSpace:
    def __init__(self, index: int):
        self.index = index
        # bottom car or None
        self.bottom: Optional[Car] = None
        # top car or None
        self.top: Optional[Car] = None

    def is_empty(self):
        return self.bottom is None and self.top is None

    def has_no_car(self):
        # no car either bottom or top
        return self.is_empty()

    def has_one_car(self):
        return (self.bottom is None) != (self.top is None)

    def cars(self):
        result = []
        if self.bottom is not None:
            result.append(self.bottom)
        if self.top is not None:
            result.append(self.top)
        return result

    def empty_positions(self):
        pos = []
        if self.bottom is None:
            pos.append(0)
        if self.top is None:
            pos.append(1)
        return pos


class ParkingLot:
    def __init__(self, m: int):
        self.spaces = [ParkingSpace(i + 1) for i in range(m)]  # 1-indexed internally for numbering convenience
        self.wait_queue: deque[Car] = deque()
        self.current_time = 0
        self.output_order: List[int] = []  # car_id in order of leaving

    def can_park_in_space(self, space: ParkingSpace, dp_time: int) -> bool:
        # always true, but check for empty or not
        return space.bottom is None or space.top is None

    def _remaining_time(self, car: Car, now: int) -> int:
        remain = car.departure_time - now
        return max(remain, 0)

    def _find_spaces_no_cars(self):
        return [space for space in self.spaces if space.is_empty()]

    def _find_spaces_with_one_car(self):
        return [space for space in self.spaces if space.has_one_car()]

    def _find_spaces_bottom_only(self):
        return [space for space in self.spaces if space.bottom is not None and space.top is None]

    def _assign_park_position(self, car: Car, space: ParkingSpace):
        if space.is_empty():
            # Simply park bottom first
            space.bottom = car
            car.park_position = (space.index, 0)
        else:
            # The rules says if one car, new one goes up and old moves down: but here no movement after parked
            # Actually the problem states: when parking on an occupied space, the existing car below moves to top, and new car is on bottom
            # Or the new car goes on top, and existing is pushed bottom? The problem states that when we park on a spot with 1 car, the existing car is pushed to top and new car is bottom.

            # Implement that existing car moves to top, new car bottom:
            if space.bottom is not None and space.top is None:
                # push bottom car up, new car bottom
                # But problem says the existing car "が先に駐車していた車 B は上段になります." in example : the previous car moves to top and new car bottom.
                # But higher in description it says: 上段の車を出す時、下段の車が先に出る必要があるので上段の車の駐車時間が過ぎても下段の車の持ち主が戻っていないと出せない。
                # So bottom and top clause is as described: existing bottom is pushed up, new car is bottom.
                old_car = space.bottom
                space.top = old_car
                old_car.park_position = (space.index, 1)
                space.bottom = car
                car.park_position = (space.index, 0)
            elif space.top is not None and space.bottom is None:
                # Should not happen based on problem statement, but just handle anyway
                old_car = space.top
                space.bottom = car
                car.park_position = (space.index, 0)
                space.top = old_car
                old_car.park_position = (space.index, 1)
            else:
                # Both occupied cannot assign here
                raise RuntimeError("Trying to park on a full space")

    def _remaining_park_time_in_space(self, space: ParkingSpace, now: int) -> List[int]:
        # returns remaining time of cars in that space
        times = []
        if space.bottom is not None:
            times.append(space.bottom.departure_time - now)
        if space.top is not None:
            times.append(space.top.departure_time - now)
        return times

    def _min_diff_space(self, car: Car, now: int) -> Optional[ParkingSpace]:
        # Implements the rules:
        # 「駐車してある車の残り駐車時間が駐車しようとしている車の駐車時間以上のものがある場合、その差が一番小さい駐車スペースに駐車します。」
        # 「駐車してあるどの車の残り駐車時間も駐車しようとしている車の駐車時間未満である場合、その差が一番小さい駐車スペースに駐車します。」
        # かつ条件に合うもの複数あれば番号小さい方
        # We consider all spaces with 1 car (because if no car, will park first in empty spaces)
        candidates = []
        for space in self._find_spaces_with_one_car():
            # Calculate minimum remaining parking time of cars in space
            remaining_times = self._remaining_park_time_in_space(space, now)
            if not remaining_times:
                continue
            min_remaining = min(remaining_times)
            if min_remaining >= car.park_duration:
                # difference >= 0
                diff = min_remaining - car.park_duration
                candidates.append((diff, space.index, space))
        if candidates:
            # Take minimal diff and smallest index
            candidates.sort(key=lambda x: (x[0], x[1]))
            return candidates[0][2]
        else:
            # no spaces with car whose remain time >= car's parking time
            # use smaller diff but now car's parking time larger than remaining times
            candidates = []
            for space in self._find_spaces_with_one_car():
                remaining_times = self._remaining_park_time_in_space(space, now)
                if not remaining_times:
                    continue
                min_remaining = min(remaining_times)
                # all less than car's time here
                diff = car.park_duration - min_remaining
                candidates.append((diff, space.index, space))
            if candidates:
                candidates.sort(key=lambda x: (x[0], x[1]))
                return candidates[0][2]
        return None

    def park_car(self, car: Car):
        # Step 1: if any empty space, park in minimal number empty space bottom
        empty_spaces = self._find_spaces_no_cars()
        if empty_spaces:
            empty_spaces.sort(key=lambda s: s.index)
            self._assign_park_position(car, empty_spaces[0])
            return

        # Step 2: try to park in space following the difference rule
        space = self._min_diff_space(car, self.current_time)
        if space is not None:
            self._assign_park_position(car, space)
            return

        # Step 3: no space available, wait queue
        self.wait_queue.append(car)

    def _remove_car(self, car: Car):
        space_idx, level = car.park_position
        space = self.spaces[space_idx - 1]
        if level == 0:
            space.bottom = None
        else:
            space.top = None
        car.park_position = None

    def _find_departing_cars(self):
        # find cars that must depart at current time
        # must handle:
        # - lower cars depart first
        # - top cars must wait their lower to depart first if in same space
        # Return list of cars that can depart now ordered by space index
        departing_bottom = []
        departing_top = []
        for space in self.spaces:
            b = space.bottom
            t = space.top
            if b and b.departure_time <= self.current_time:
                departing_bottom.append((space.index, b))
            if t and t.departure_time <= self.current_time:
                departing_top.append((space.index, t))

        departing_bottom.sort(key=lambda x: x[0])
        departing_top.sort(key=lambda x: x[0])

        # Bottom cars depart first
        bottom_cars_departing = [c for _, c in departing_bottom]

        # For top cars, only depart if bottom car has departed or not present
        top_cars_departing = []
        for space_idx, top_car in departing_top:
            space = self.spaces[space_idx - 1]
            # can depart only if bottom is None or bottom has departure_time <= current_time (already departing)
            if space.bottom is None or (space.bottom.departure_time <= self.current_time and space.bottom not in bottom_cars_departing):
                top_cars_departing.append(top_car)
            else:
                # must wait for bottom car
                pass

        # top cars depart simultaneous after their bottom cars
        # but possible multiple top cars in different spaces
        # return all departing cars bottom then top ordered by space index
        return bottom_cars_departing, top_cars_departing

    def process_departures(self):
        bottom_depart, top_depart = self._find_departing_cars()
        # depart bottom cars
        for car in bottom_depart:
            self._remove_car(car)
            self.output_order.append(car.car_id)
        # depart top cars after bottom cars
        for car in top_depart:
            self._remove_car(car)
            self.output_order.append(car.car_id)
        return len(bottom_depart) + len(top_depart)

    def tick(self):
        # process departures first at current time
        departed_count = self.process_departures()
        # After all departures, process waiting queue for parking if spaces free
        while self.wait_queue:
            car = self.wait_queue[0]
            # check if can park now at current time (there may newly opened space)
            # search empty space
            empty_spaces = self._find_spaces_no_cars()
            if empty_spaces:
                empty_spaces.sort(key=lambda s: s.index)
                self._assign_park_position(car, empty_spaces[0])
                self.wait_queue.popleft()
                continue
            else:
                # try min diff space
                space = self._min_diff_space(car, self.current_time)
                if space is not None:
                    self._assign_park_position(car, space)
                    self.wait_queue.popleft()
                    continue
                else:
                    break  # no space for first waiting car, wait further time

    def run_simulation(self, cars: List[Car]):
        # cars arrive 10 minutes apart starting time 0, indexes are 1-based car_id
        # simulation time step in minutes: minimal unit 1 minute, but cars arrive every 10 minutes
        # simulation ends when all cars departed

        total_cars = len(cars)
        parked_count = 0
        arrived_idx = 0
        last_arrival_time = (cars[-1].arrival_time if cars else 0)
        max_time = max(c.departure_time for c in cars) if cars else 0
        # we simulate from time=0 forward in minutes

        # an abstraction: event loop

        # maintain when next car arrives
        # We proceed minute per minute for simplicity (max 120 parking time; time may go max 100*10 + max t)
        # but since max number of cars 100 and max parking time 120, it's acceptable.

        while len(self.output_order) < total_cars:

            # Arrival of cars
            # Cars arrive exact at their arrival_time
            while arrived_idx < total_cars and cars[arrived_idx].arrival_time == self.current_time:
                car = cars[arrived_idx]
                self.park_car(car)
                arrived_idx += 1

            # depart cars and park waiting at this time
            self.tick()
            self.current_time += 1


def parse_input() -> List[Tuple[int, int, List[int]]]:
    import sys
    dataset = []
    lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while idx < len(lines):
        if lines[idx].strip() == '':
            idx += 1
            continue
        m_n = lines[idx].split()
        if len(m_n) < 2:
            break
        m, n = int(m_n[0]), int(m_n[1])
        idx += 1
        if m == 0 and n == 0:
            break
        t_list = []
        for _ in range(n):
            t_list.append(int(lines[idx]))
            idx += 1
        dataset.append((m, n, t_list))
    return dataset


def main():
    dataset = parse_input()
    for (m, n, t_list) in dataset:
        parking_lot = ParkingLot(m)
        cars = []
        for i, t in enumerate(t_list):
            # arrival time every 10 minutes * index starting from 0 => i*10
            cars.append(Car(i + 1, t, i * 10))
        parking_lot.run_simulation(cars)
        print(' '.join(map(str, parking_lot.output_order)))


if __name__ == '__main__':
    main()