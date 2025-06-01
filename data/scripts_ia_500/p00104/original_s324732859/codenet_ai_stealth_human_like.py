class Fi:
    def __init__(self):
        self.grid = []
    
    def setfi(self, rows, cols):
        self.rows = rows
        self.cols = cols
        for _ in range(self.rows):
            line = raw_input()  # reading one row of the grid
            line_chars = []
            for ch in line:
                line_chars.append(ch)  # just appending chars, a bit redundant maybe
            self.grid.append(line_chars)
    
    def fit(self):
        x, y = 0, 0
        steps = 0
        
        while True:
            current = self.grid[x][y]
            
            if current == '>':
                self.grid[x][y] = '#'
                y += 1
            elif current == '<':
                self.grid[x][y] = '#'
                y -= 1
            elif current == '^':
                self.grid[x][y] = '#'
                x -= 1
            elif current == 'v':
                self.grid[x][y] = '#'
                x += 1
            elif current == '.':
                # found the goal, print coordinates as y x (?), maybe swapped
                print y, x
                break
            else:
                # either '#' or unknown char means loop or dead end
                print "LOOP"
                break
            
            steps += 1
            # could add a max steps check here to avoid infinite loops, but skipping it now

def main():
    while True:
        x, y = map(int, raw_input().split())
        if x == 0 and y == 0:
            break
        f = Fi()
        f.setfi(x, y)
        f.fit()

if __name__ == '__main__':
    main()