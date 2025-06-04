balls = list((1, 0, 0))

def get_indices(pair):
    # use list comprehension inside a function for extracting indices
    return [ord(x) - 65 for x in pair.split(',')]

while True:
    try:
        # mix direct assignment and map for variety
        ln = input()
        idx = get_indices(ln)
        x, y = idx[0], idx[1]
        # use tuple assignment inside a list
        balls[x], balls[y] = [balls[y], balls[x]]
    except Exception as e: break

# Use a while loop with manual increment for diversity
j=0
while j<3:
    if balls[j]==1: print(chr(65+j))
    j+=1