import math

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    red_length = 0
    blue_length = 0
    
    # on the line from (0,0) to (h-1,w-1)
    # the line length is sqrt((h-1)^2 + (w-1)^2)
    # the line passes through h+w-1 squares
    # number of segments is h+w-2
    # Each segment is either horizontal or vertical
    # but in this problem we consider the total length in red and blue squares
    
    # Calculate gcd to find the integer ratio
    g = math.gcd(h-1, w-1)
    
    # number of segments is (h-1)+(w-1) = h+w-2
    # the line crosses (h-1)+(w-1)+1 squares along the way = h+w-1 squares
    
    # length in each square along the line:
    # total length = sqrt((h-1)^2 + (w-1)^2)
    total_length = ((h-1)**2 + (w-1)**2)**0.5
    
    # the length is divided into (h-1)+(w-1) segments = h+w-2 segments
    # number of squares crossed = h+w-1
    # coloring alternates every square along the line starting from (0,0)
    # (0+0)=0 even => first square red
    # So the number of red squares along the line is:
    # if total squares is odd, red squares count = (total_squares +1)//2
    # if even, both red and blue squares count are equal
    
    total_squares = h + w -1
    
    red_squares = (total_squares +1)//2
    blue_squares = total_squares - red_squares
    
    # each square's length along the line is not uniform in general
    # but the problem states that the ratio a:b is always an integer ratio,
    # so we can just use the counts as ratio
    
    a = red_squares
    b = blue_squares
    
    g = math.gcd(a,b)
    a //= g
    b //= g
    
    print(a, b)