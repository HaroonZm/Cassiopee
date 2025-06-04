def calculate_area_and_center():
    import sys
    W,H,X,Y = [int(i) for i in sys.stdin.readline().split()]
    def area(w,h): return w*h*0.5
    center_flag = 1 if float(W)/2==X and (lambda h,y: h/2==y)(H,Y) else 0
    print(area(W,H), center_flag)

calculate_area_and_center()