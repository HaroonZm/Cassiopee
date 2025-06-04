# Un style excentrique : variables camelCase exagéré, boucles inversées,
# abus de lambdas, tout en une fonction, lambda print pour briller, type hints dans les noms
def whizzBangMain():
    GetInputAsIntList = lambda: list(map(int, input().split()))
    numberOfCities_Num, movesAllowed_Num = GetInputAsIntList()

    MODZ_Const = 10 ** 9 + 7

    # Matrix factory by overloading range in a funny way
    createStateGrid_Matrix = lambda n: [[0] * n for _ in "~" * n]
    cityStateMatrix = createStateGrid_Matrix(numberOfCities_Num)

    cityStateMatrix[numberOfCities_Num-1][0] = 1

    # A poetic alternative to range -- reversed, custom loop var names
    for _whizzMoveId in list(reversed(range(movesAllowed_Num)))[::-1]:
        futureCityStates_Ndp = createStateGrid_Matrix(numberOfCities_Num)
        for leftUnvisited_ZeroStat in range(numberOfCities_Num-1, -1, -1):
            for onesStatusCounter in range(numberOfCities_Num-1, -1, -1):

                # VISIT UNVISITED: decrease zeros, increase ones
                if leftUnvisited_ZeroStat and onesStatusCounter != numberOfCities_Num-1:
                    aBizarreVal = cityStateMatrix[leftUnvisited_ZeroStat][onesStatusCounter] * leftUnvisited_ZeroStat
                    futureCityStates_Ndp[leftUnvisited_ZeroStat-1][onesStatusCounter+1] += aBizarreVal
                    futureCityStates_Ndp[leftUnvisited_ZeroStat-1][onesStatusCounter+1] %= MODZ_Const

                # STAY IN ONES: only if any exist
                if onesStatusCounter > 0:
                    mmmVal = cityStateMatrix[leftUnvisited_ZeroStat][onesStatusCounter] * onesStatusCounter
                    futureCityStates_Ndp[leftUnvisited_ZeroStat][onesStatusCounter] += mmmVal
                    futureCityStates_Ndp[leftUnvisited_ZeroStat][onesStatusCounter] %= MODZ_Const

                # STATE2er: warp all ones -> twos
                classicTwos = cityStateMatrix[leftUnvisited_ZeroStat][onesStatusCounter] * (
                        numberOfCities_Num - leftUnvisited_ZeroStat - onesStatusCounter)
                futureCityStates_Ndp[leftUnvisited_ZeroStat][0] += classicTwos
                futureCityStates_Ndp[leftUnvisited_ZeroStat][0] %= MODZ_Const

        cityStateMatrix = futureCityStates_Ndp

    (lambda x: print(x))(cityStateMatrix[0][0] % MODZ_Const)

whizzBangMain()