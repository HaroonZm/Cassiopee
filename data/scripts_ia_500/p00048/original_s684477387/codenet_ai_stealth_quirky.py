import sys

def main():
    clasz = {48.00:"light fly", 51.00:"fly", 54.00:"bantam", 57.00:"feather", 60.00:"light", 64.00:"light welter",
             69.00:"welter", 75.00:"light middle", 81.00:"middle", 91.00:"light heavy"}

    while 1==1:
        try:
            wght = float(input().strip())
        except Exception as e:
            sys.exit(0)

        printed = False
        for limit in sorted(clasz.keys()):
            if wght <= limit:
                print(clasz[limit])
                printed = True
                break
        if not printed:
            print("heavy")

if __name__=="__main__":
    main()