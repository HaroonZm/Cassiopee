def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        books = input().strip()

        # shelves are numbered 1 to 4N
        # We want to find minimal cost path starting from position 0,
        # to putting all books with ID = shelf number that have Y.

        # Model:
        # There are N+1 sub passages numbered 0 to N (vertical)
        # There are 4 horizontal shelves arranged in 4 rows:
        # shelf number s corresponds to (row, col):
        # row = (s-1)//N (0..3)
        # col = (s-1)%N (0..N-1)
        #
        # Positions she can stop:
        # - intersections of passages: (row, col) where row in 0..3, col in 0..N
        #   but walking allowed only forward on main passages:
        #   Main passages: horizontal rows 0..3 have directional edges from col to col+1
        # - middle of shelves, which are positions between intersections:
        #   At (row, col+0.5) between (row, col) and (row, col+1)
        #
        # Start position: intersection at (0,0) (white circle)
        # End position: intersection at (3,N) (black circle)

        # She can move on main passages only forward (left to right) intersections
        # Walking from intersection to adjacent intersection cost =1
        # Walking from intersection to middle of shelf or vice versa =0.5

        # She must put books at shelves with Y.
        # Putting a book at shelf s means stopping at middle of shelf s at least once.
        #
        # Objective: minimal total cost to put all books and move from start to end.

        # Observation:
        # Since moving backward is forbidden on main passages, path is essentially from col=0 to col=N.
        #
        # She can move up/down between main passages only at shelves middle?
        # No vertical movement between rows is not allowed directly.
        #
        # But problem mentions only forward walking on main passages.
        # Vertical movement allowed only at intersections or shelves middle?
        #
        # Actually, problem states she can only stop at intersections or shelf middles.
        # The vertical movement is not described explicitly,
        # but because shelves are stacked vertically and passages horizontal and vertical,
        # we can represent as a grid with edges:
        #
        # Vertical edges: moves between rows at same col position (intersection to intersection or middle to middle).
        #
        # At intersection, she can move vertically up/down with cost 1.
        #
        # At shelf middle, vertical movement is not explicitly forbidden, so maybe also cost 1?
        #
        # Because it's not stated forbidden, we assume vertical edges between same col intersection rows exist with cost 1.
        #
        # So model the grid nodes as:
        # For each col (0 to N)
        # For each row (0 to 3)
        # nodes:
        #   intersection (r,c)
        #
        # For each col (0 to N-1)
        # For each row (0 to 3)
        # nodes:
        #   middle (r, c+0.5)

        # Moves allowed:
        # - intersection(r,c) <-> middle(r, c+0.5) cost 0.5
        # - intersection(r,c) <-> intersection(r,c+1) cost 1 (only forward)
        # - intersection(r,c) <-> intersection(r+1,c) cost 1 if 0 <= r+1 <= 3 (vertical movement)
        # Similar vertical at intersection up/down allowed.

        # We want to find minimal cost path from start = intersection(0,0)
        # to end = intersection(3,N)
        # passing through all shelf middles where books exist.

        # The best way is to find minimal path visiting required nodes (all shelf middles with books).
        # Since N can be large, no TSP approach possible.

        # Note: Because forward walking only on main passages,
        # horizontal movement only allowed left->right on intersections

        # Plan:
        # Since shelves are divided in 4 rows and N columns,
        # and movement only forward horizontally (from col to col+1),
        # and vertical movement between rows allowed at each col with cost 1,
        #
        # The problem reduces to:
        #
        # At each column c (0..N):
        #    She can move vertically along intersections between rows (cost 1 each step)
        #
        # Moving from col c to c+1 on same row cost 1
        #
        # To put a book at shelf s = (r, c), she must stop at middle(r, c+0.5)
        #
        # She can move at middle nodes only between intersections to put books,
        # cost 0.5 step to/from middle.

        # So to put required books, at each column c, some set of rows (0..3) will have shelves with books.
        # To put those, she must at that column stop at middle of shelf.
        #
        # So the minimal cost is:
        #
        # Walking from start intersection(0,0),
        # For each column from 0 to N-1:
        #   Move in current column intersection rows to visits all required middles.
        #   Put books at these middles (cost 0.5 + 0.5 per shelf for going to and from middle)
        #   Then move right to next column intersections (cost 1) on some row.
        #
        # Finally, reach intersection(3,N)

        # Because vertical movement on intersections costs 1 per row visited,
        # to visit all required books in that column, best is to walk minimal vertical path covering all rows with books.

        # So at each column c, find minimal cost to cover all rows with books at column c:
        # That means:
        # - Start at some row at column c (the row chosen by previous step)
        # - visit all rows that have books (put books in their middle)
        # - end at some row at column c to move to next column

        # We can do DP over columns and possible rows at intersection:
        # dp[c][r] = minimal cost to be at intersection (r,c) after handling column c

        # Initialization: dp[0][0] = 0 (start at intersection(0,0))
        # others dp[0][r] = INF

        # Transition from dp[c][r1] to dp[c+1][r2]:
        # At column c, must visit all book rows:
        # - Cost to vertically move from r1 to cover all book rows at col c and end at temp row r3
        #   plus cost of putting books (0.5 * 2 per book) = 1 per book.
        #
        # vertical path to cover rows with books at col c:
        #
        # As vertical movement costs 1 per step,
        # minimal path covering rows = minimal vertical path starting at r1, visiting all book rows to end at r3.

        # Because rows are line 0..3,
        # minimal vertical path visiting all rows in set S of rows with books is:
        #
        # The vertical path must start at r1, visit all rows in S, and end at r3.
        #
        # The minimal cost vertical path visiting all rows in S starting at r1 and ending at r3 will be:
        #
        # med = min(S), mid = max(S)
        # The path covers from med to mid inclusive
        #
        # vertical distance is abs(r1 - med) + (mid - med) + abs(r3 - mid)
        #
        # But we can swap med and mid depending on order.
        #
        # We try both orders:
        # 1) up to med first then down to mid:
        # cost1 = abs(r1 - med) + (mid - med) + abs(r3 - mid)
        # 2) up to mid first then down to med:
        # cost2 = abs(r1 - mid) + (mid - med) + abs(r3 - med)
        #
        # minimal vertical cost = min(cost1, cost2)
        #
        # Adding putting books cost: number of books at col c
        #
        # Then moving horizontally from col c intersection r3 to col c+1 intersection r2 cost=1 if r3 == r2 else infinite
        #
        # Because horizontal move allowed only forward along main passages:
        # on same row only (move from (r, c) to (r, c+1)) cost 1
        #
        # So dp transition only possible if r3 == r2, so let's rename r3 to r2, intersection at col c+1.

        # So:
        # dp[c+1][r2] = min over r1 dp[c][r1] + vertical_path_cost(r1, r2, rows_with_books_c) + num_books_c + 1

        INF = 10**9

        # Extract rows with books at each column:
        rows_with_books_cols = [[] for _ in range(N)]
        for s in range(4 * N):
            if books[s] == 'Y':
                r = s // N
                c = s % N
                rows_with_books_cols[c].append(r)

        dp = [INF] * 4
        dp[0] = 0  # start at intersection (0,0)

        for c in range(N):
            next_dp = [INF] * 4
            b_rows = sorted(rows_with_books_cols[c])
            if not b_rows:
                # no books at this column, just move horizontally to next column
                for r in range(4):
                    if dp[r] == INF:
                        continue
                    # move horizontally on same row
                    # cost horizontal = 1
                    next_dp[r] = min(next_dp[r], dp[r] + 1)
            else:
                med = b_rows[0]
                mid = b_rows[-1]
                num_books = len(b_rows)
                for r1 in range(4):  # start row at col c intersection
                    if dp[r1] == INF:
                        continue
                    for r2 in range(4):  # end row at col c intersection (must match next col start)
                        # two possible vertical path costs
                        cost1 = abs(r1 - med) + (mid - med) + abs(r2 - mid)
                        cost2 = abs(r1 - mid) + (mid - med) + abs(r2 - med)
                        vertical = min(cost1, cost2)
                        # plus putting books cost = 1 per book (0.5 to middle, 0.5 back)
                        total_col_cost = vertical + num_books
                        # plus horizontal move to next col on same row r2 cost 1
                        total_cost = dp[r1] + total_col_cost + 1
                        if next_dp[r2] > total_cost:
                            next_dp[r2] = total_cost
            dp = next_dp

        # end position is intersection (3,N)
        print(int(dp[3]))