def main():
    while True:
        data = input()
        data = data.split(" ")
        
        for i in range(len(data)):
            data[i] = int(data[i])

        if data == [0, 0]:
            return 

        
        man = data[0]
        donst = data[1]
        print(game(man, donst))

def game(man, donst):
    manst = [0 for j in range(man)]

    while True:
        for j in range(len(manst)):
            if donst != 0:
                donst -= 1
                manst[j] += 1

                if donst == 0:
                    zerocount = 0
                    for item in manst:
                        if item == 0:
                            zerocount += 1

                    if zerocount == man - 1:
                        return j

            else:
                donst = manst[j]
                manst[j] = 0
main()