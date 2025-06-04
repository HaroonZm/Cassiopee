S = int(input())

count = 0

for b_minus_a in range(S):
    for d_minus_c in range(S):
        # We consider rectangle sizes (height, width) = (b_minus_a + 1, d_minus_c +1)
        height = b_minus_a + 1
        width = d_minus_c + 1

        # The sum of numbers in the rectangle from a..b and c..d is:
        # sum = (sum_i=a^b i) * (sum_j=c^d j)
        # sum_i=a^b i = (a + b) * height / 2
        # Let x = a + b, y = c + d
        # sum = (x * height / 2) * (y * width / 2) = (x * y * height * width) / 4 = S
        # So x * y = 4 * S / (height * width)

        if (4 * S) % (height * width) != 0:
            continue

        val = (4 * S) // (height * width)

        # Find the number of factor pairs (x, y) of val such that:
        # x >= height (because x = a + b and a <= b, minimum a is 1)
        # We must have integers a and b with a <= b and a,b >=1, and a + b = x
        # For a given x, number of integer pairs (a,b) with a <= b and a + b = x:
        # a in [ceil(x/2), x-1] but a >=1 and b = x - a
        # a <= b => a <= x - a => 2a <= x => a <= x//2
        # Also a <= b, so a <= b and a + b = x => a <= x//2
        # So a in [1, x//2]
        # But since a,b >=1, a<=b and a+b = x, number of pairs = floor((x-1)/2)

        # Similarly for y, same reasoning

        # So number of (a,b) pairs = (x-1)//2, number of (c,d) pairs = (y -1)//2
        # Total number of rectangles with this height and width = number of (x,y) factor pairs satisfying above

        # So we find all positive divisors of val and for each divisor x, set y=val//x
        # For each (x,y), check if number of pairs for x and y >0, sum their products

        for x in range(1, int(val**0.5)+1):
            if val % x == 0:
                y = val // x

                # count pairs for x:
                if x > 1:
                    count_x = (x -1)//2
                else:
                    count_x = 0

                # count pairs for y:
                if y >1:
                    count_y = (y -1)//2
                else:
                    count_y = 0

                count += count_x * count_y

                if x != y:
                    # consider (y,x) pair
                    if y >1:
                        count_x = (y -1)//2
                    else:
                        count_x = 0

                    if x >1:
                        count_y = (x -1)//2
                    else:
                        count_y = 0

                    count += count_x * count_y

print(count)