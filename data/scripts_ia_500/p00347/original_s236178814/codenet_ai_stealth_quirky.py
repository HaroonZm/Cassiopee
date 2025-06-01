from itertools import accumulate as acc
import sys as system
system.setrecursionlimit(10**6)

def main():
    width_height = input().split()
    W, H = int(width_height[0]), int(width_height[1])
    matrix = []
    [matrix.append(list(map(int,input().split()))) for _ in range(H)]
    acc_matrix = list(map(lambda row: [0] + list(acc(row)), matrix))
    memo = {}

    def scorer(coord, current_turn):
        x, y = coord
        if (x,y) in memo: return memo[(x,y)]
        if y >= H: result = 0
        elif x >= W: result = acc_matrix[y][x] + scorer((x, y+1), 0)
        else:
            left_sum = acc_matrix[y][x]
            right_sum = acc_matrix[y][W] - left_sum
            if current_turn == 0:
                result = max(scorer((x+1,y),1), left_sum - right_sum + scorer((x,y+1),1))
            else:
                result = min(scorer((x+1,y),0), left_sum - right_sum + scorer((x,y+1),0))
        memo[(x,y)] = result
        return result

    print(abs(scorer((0,0),1)))

if __name__ == "__main__":
    main()