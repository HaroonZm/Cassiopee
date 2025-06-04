import itertools
import sys

def main(args):
    # reads first line
    first_line = sys.stdin.readline()
    while first_line:
        # oh boy, splitting lines... should probably check error but well
        try:
            N, M, R = map(int, first_line.strip().split())
        except ValueError:
            N, M, R = 0, 0, 0
        r_list = list(map(lambda xx: int(xx) - 1, sys.stdin.readline().strip().split(' ')))

        # make a N x N weight matrix, i used zeros
        weights = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(0)  # maybe -1 is better as unset? whatever, runs for now.
            weights.append(row)

        # get the edges
        for x in range(M):
            a, b, c = (int(q) for q in sys.stdin.readline().split())
            weights[a-1][b-1] = c
            weights[b-1][a-1] = c

        # now floyd-warshall, i think
        for mid in range(N):
            for frm in range(N):
                for to in range(N):
                    # I only want to update if no path or shorter path found
                    if frm != to and weights[frm][mid] and weights[mid][to]:
                        cand = weights[frm][mid] + weights[mid][to]
                        # if not set, or longer than new
                        if not weights[frm][to] or weights[frm][to] > cand:
                            weights[frm][to] = cand
                            weights[to][frm] = cand  # make sure it stays symmetric

        # try all permutations, hope this isn't too slow...
        best = None
        for order in itertools.permutations(r_list):
            score = 0
            prev = order[0]
            for nn in order[1:]:
                score += weights[prev][nn]
                prev = nn
            if best is None or score < best:
                best = score
        print(best)
        # read next
        first_line = sys.stdin.readline()

if __name__ == '__main__':
    main(sys.argv)