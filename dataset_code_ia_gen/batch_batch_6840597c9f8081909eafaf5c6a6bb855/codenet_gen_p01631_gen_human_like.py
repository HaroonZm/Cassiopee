from collections import defaultdict

# directions: 8 neighboring cells (vertical, horizontal, diagonal)
DIRECTIONS = [(-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0),  (1,1)]

def main():
    N = int(input())
    word_score = {}
    max_len = 0
    for _ in range(N):
        w, s = input().split()
        word_score[w] = int(s)
        max_len = max(max_len, len(w))
    board = [input() for _ in range(4)]
    T = int(input())

    # Build a dictionary indexing words by their first letter for pruning
    # also build a prefix set for pruning search paths
    prefix_set = set()
    for w in word_score:
        for l in range(1, len(w)+1):
            prefix_set.add(w[:l])

    def in_board(x,y):
        return 0 <= x < 4 and 0 <= y < 4

    found_paths = defaultdict(set)  # {word : set of tuple of positions}

    # DFS to find all distinct paths spelling dictionary words
    def dfs(x, y, visited, path, word_so_far):
        if word_so_far not in prefix_set:
            return
        if word_so_far in word_score:
            # store path as tuple of positions to count distinct paths
            found_paths[word_so_far].add(tuple(path))
        if len(word_so_far) == max_len:
            return
        for dx, dy in DIRECTIONS:
            nx, ny = x+dx, y+dy
            if in_board(nx, ny) and (nx, ny) not in visited:
                dfs(nx, ny, visited | {(nx, ny)}, path+[(nx, ny)], word_so_far + board[nx][ny])

    # For each cell, start DFS for words starting from its letter
    for i in range(4):
        for j in range(4):
            dfs(i, j, {(i, j)}, [(i,j)], board[i][j])

    # Each path for each word costs word length seconds and gives score
    # We want to choose a collection of distinct path-words (distinct path means distinct indexing)
    # maximizing score with time limit T.
    # This is a 0/1 knapsack where each (word,path) is an item, cost = len(word), value = word_score[word].
    # However, since same word with different paths is multiple items with same value and cost,
    # we must treat each path as a separate item.
    
    items = []
    for w, paths in found_paths.items():
        time = len(w)
        score = word_score[w]
        for _ in paths:
            items.append((time, score))

    dp = [0]*(T+1)
    for cost, val in items:
        for time_left in range(T, cost-1, -1):
            dp[time_left] = max(dp[time_left], dp[time_left - cost] + val)

    print(max(dp))


if __name__ == "__main__":
    main()