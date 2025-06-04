import sys

def max_consecutive_ones(grid, n):
    max_len = 0
    # dp arrays for horizontal, vertical, diagonal (top-left to bottom-right), anti-diagonal (top-right to bottom-left)
    hori = [0]*n
    vert = [0]*n
    diag = [0]*(n+1)  # use offset j - i + n to handle negative indices if needed, here we adjust differently
    adiag = [0]*(n+1) # j + i
    
    # Better to use 2D arrays instead for clarity and O(n^2) complexity acceptable here
    hori = [[0]*n for _ in range(n)]
    vert = [[0]*n for _ in range(n)]
    diag = [[0]*n for _ in range(n)]
    adiag = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                hori[i][j] = hori[i][j-1] + 1 if j>0 else 1
                vert[i][j] = vert[i-1][j] + 1 if i>0 else 1
                diag[i][j] = diag[i-1][j-1] + 1 if i>0 and j>0 else 1
                adiag[i][j] = adiag[i-1][j+1] + 1 if i>0 and j<n-1 else 1
                curr_max = max(hori[i][j], vert[i][j], diag[i][j], adiag[i][j])
                if curr_max > max_len:
                    max_len = curr_max
            else:
                hori[i][j] = 0
                vert[i][j] = 0
                diag[i][j] = 0
                adiag[i][j] = 0
    return max_len

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = input_lines[idx].strip()
        idx+=1
        if n == '0':
            break
        n = int(n)
        grid = input_lines[idx:idx+n]
        idx += n
        print(max_consecutive_ones(grid, n))
        
if __name__ == "__main__":
    main()