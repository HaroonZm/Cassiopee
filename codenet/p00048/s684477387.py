while True:
    try:
        weight = float(input())

        if(weight <= 48.00):
            print("light fly")
        elif(weight <= 51.00):
            print("fly")
        elif(weight <= 54.00):
            print("bantam")
        elif(weight <= 57.00):
            print("feather")
        elif(weight <= 60.00):
            print("light")
        elif(weight <= 64.00):
            print("light welter")
        elif(weight <= 69.00):
            print("welter")
        elif(weight <= 75.00):
            print("light middle")
        elif(weight <= 81.00):
            print("middle")
        elif(weight <= 91.00):
            print("light heavy")
        else:
            print("heavy")
    except:
        break;