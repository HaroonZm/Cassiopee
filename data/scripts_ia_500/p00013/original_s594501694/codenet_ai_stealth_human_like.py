# coding=utf-8

if __name__ == '__main__':
    trains = []
    while True:
        try:
            n = int(input())  # read integer from user input
        except EOFError:  # end of file reached, stop loop
            break
        if n == 0:
            if trains:    # just to be safe, check if list is not empty
                car = trains.pop()
                print(car)  # print the car leaving the train
            else:
                # hmm, nothing to pop, maybe input was invalid?
                pass
        else:
            trains.append(n)  # add the new car to train list