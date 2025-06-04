import sys
from collections import deque

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        m, n = map(int, line.split())
        if m == 0 and n == 0:
            break
        times = [int(input()) for _ in range(n)]
        # arrival times: car i arrives at i*10
        # parking spots: each has upper and lower slot (None or (car_id, leave_time))
        spots = [ [None,None] for _ in range(m)]  # [lower, upper]
        leave_order = []
        waiting = deque()
        time = 0
        car_idx = 0
        total_cars = n
        parking_cars = 0

        def remaining_time(pos):
            # returns list of remaining times of cars in this spot (lower then upper)
            res = []
            for car in spots[pos]:
                if car is None:
                    res.append(None)
                else:
                    res.append(car[1]-current_time)
            return res

        def park_car(car_id, park_time):
            # find spot following the rules
            # 1) any empty spot (both None) -> pick smallest spot #
            empty_spots = [i for i,(l,u) in enumerate(spots) if l is None and u is None]
            if empty_spots:
                spot = empty_spots[0]
                spots[spot][0] = (car_id, park_time)
                return True

            # 2) any spot with 1 car: put new car in upper slot, but may need to move previous lower to upper
            empty_one = [i for i,(l,u) in enumerate(spots) if (l is not None and u is None) or (l is None and u is not None)]
            # but problem states that 2段式 has 1 lower and 1 upper, so first is lower, second is upper,
            # and already parking assigns first car to lower, second car to upper

            # 3) For spots partly occupied or full?
            # Actually, per problem:
            # when parking, first try spots with 0 cars
            # if no such spot, then pick spots with 1 car whose remaining parking time satisfies conditions

            # So, find spots that have exactly one car
            one_car_spots = []
            for i in range(m):
                l,u = spots[i]
                count = (l is not None) + (u is not None)
                if count==1:
                    one_car_spots.append(i)

            ctime = park_time # the leave time of new car

            # For these spots with one car, compute difference with existing car(s)
            # For difference calculation, use existing car remaining time(s)
            # Existing remaining time = leave time - current_time
            # But what is current_time? The arrival time of the incoming car: 10*car_id (starting id=0)
            current_time = car_id*10

            candidates = []
            less_equal = []
            less = []
            for pos in one_car_spots:
                # get occupied car's remaining time
                l,u = spots[pos]
                exist_car = l if l is not None else u
                rt = exist_car[1]-current_time
                diff = rt - times[car_id]
                if rt >= times[car_id]:
                    # diff >= 0
                    less_equal.append((diff,pos))
                else:
                    # diff < 0
                    less.append((abs(diff),pos))
            if less_equal:
                less_equal.sort(key=lambda x:(x[0],x[1]))
                spot = less_equal[0][1]
                # park upper
                spots[spot][1] = (car_id+1, park_time)
                # move existing lower to upper? no, existing is lower, we put new car upper
                return True
            if less:
                less.sort(key=lambda x:(x[0],x[1]))
                spot = less[0][1]
                spots[spot][1] = (car_id+1, park_time)
                return True

            # no available spots, return False
            return False


        def park_car_full(car_id):
            current_time = car_id*10
            ct = current_time + times[car_id]

            # 1) check empty spots no cars
            empty_spots = [i for i,(l,u) in enumerate(spots) if l is None and u is None]
            if empty_spots:
                spot = empty_spots[0]
                spots[spot][0] = (car_id+1, ct)
                return True

            # 2) spots with one car, per problem's parking rule
            one_car_spots = []
            for i in range(m):
                l,u = spots[i]
                cnt = (l is not None)+(u is not None)
                if cnt == 1:
                    one_car_spots.append(i)

            less_equal = []
            less = []
            for pos in one_car_spots:
                l,u = spots[pos]
                exist_car = l if l is not None else u
                remain = exist_car[1]-current_time
                diff = remain - times[car_id]
                if remain >= times[car_id]:
                    less_equal.append((diff,pos))
                else:
                    less.append((abs(diff),pos))
            if less_equal:
                less_equal.sort(key=lambda x:(x[0],x[1]))
                spot = less_equal[0][1]
                spots[spot][1] = (car_id+1, ct)
                return True
            if less:
                less.sort(key=lambda x:(x[0],x[1]))
                spot = less[0][1]
                spots[spot][1] = (car_id+1, ct)
                return True
            return False

        # simulate each 10 min interval until all cars have arrived and left
        # but multiple cars come and leave at same time may occur
        # So track next arrival, next departure times
        # departure can be multiple cars at same time, output in spot order

        all_leave = 0
        current_time = 0
        waiting = deque()
        arriving_cars = 0 # next car to come index
        left = [False]*n
        output = []

        # convert spots with (car_id,leave_time) with car_id 1-based
        # At each time:
        # 1) remove cars whose leave_time == current_time (for upper slot, must wait lower leaves)
        # 2) after all removals, park waiting cars as many as possible
        # 3) if next car arrival_time == current_time, add to waiting (or try park immediately)
        # iterate time by 10 min steps until all cars left

        max_time = 1500 # safe upper limit, as max times 120*10 cars ~1200

        while len(output)<n:
            current_time = arriving_cars*10 if arriving_cars<n else current_time+10
            # First, remove cars leaving now (if any), order spots by number
            # But upper must wait lower car to leave first

            # find cars leaving now
            leaving_now = []
            for i in range(m):
                lower = spots[i][0]
                upper = spots[i][1]
                # check lower
                if lower and lower[1] <= current_time:
                    leaving_now.append((current_time,i,0,lower[0]))
                # check upper condition: leave time passed & lower must be empty
            # output lower cars leaving first
            leaving_now.sort(key=lambda x: (x[1], x[2])) # spot asc, lower(0) before upper(1)

            for _,i,pos,car_id in leaving_now:
                if pos == 0:
                    # lower car leaves
                    spots[i][0] = None
                    output.append(car_id)
                    left[car_id-1]=True
                # upper leave delayed
            # now check upper cars leaving
            upper_leaving_now = []
            for i in range(m):
                upper = spots[i][1]
                lower = spots[i][0]
                if upper and upper[1] <= current_time and lower is None:
                    upper_leaving_now.append((i,upper[0]))
            upper_leaving_now.sort(key=lambda x:x[0])
            for i,car_id in upper_leaving_now:
                spots[i][1] = None
                output.append(car_id)
                left[car_id-1] = True

            # after removals, try to park waiting cars
            while waiting:
                c = waiting[0]
                if not park_car_full(c):
                    break
                waiting.popleft()

            # finally, current arriving car tries to park
            if arriving_cars < n and current_time == arriving_cars*10:
                if not park_car_full(arriving_cars):
                    waiting.append(arriving_cars)
                arriving_cars+=1

            # avoid stuck, increment time if no cars arriving
            if arriving_cars>=n and not waiting:
                # no car waiting or arriving, time step by 10 to exit leaving loop
                # but break if all cars left
                if len(output) == n:
                    break
                current_time += 10

        print(' '.join(map(str, output)))

if __name__ == "__main__":
    main()