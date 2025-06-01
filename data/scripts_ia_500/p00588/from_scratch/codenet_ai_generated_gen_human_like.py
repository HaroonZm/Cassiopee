def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        books = input().strip()

        # Positions go from 1 to 4N
        # The library layout has 4 rows (shelves) of N columns each
        # Shelves numbering:
        # row 0: 1 .. N
        # row 1: N+1 .. 2N
        # row 2: 2N+1 .. 3N
        # row 3: 3N+1 .. 4N

        # We know:
        # - She starts at middle of shelf 1 (position 1)
        # - She ends at middle of shelf 4N (position 4N)
        # - She can only move forward along main passages (vertical travel down only)
        # - Horizontal moves along sub passages are bi-directional since no restriction is stated
        # - Walking between intersections cost 1
        # - Walking from intersection to middle of shelf costs 0.5
        # - She can only stop at intersections or middles of shelves to drop books

        # We want minimal cost to cover all shelves with books (positions where books[pos-1] == 'Y')

        # Model:
        # Each shelf corresponds to a cell (row, col) with row in [0..3], col in [0..N-1]
        # position p = row*N + col +1

        # Approach:
        # Start is shelf 1 => row=0, col=0
        # End is shelf 4N => row=3, col=N-1

        # To visit a shelf, must stop at the middle of that shelf
        # She can only move forward on main passages (vertical) (downward)
        # Horizontal passages are free to go left and right (no forward constraint)
        # Actually, the problem states "She only walks main passages forward" => vertical moves only allowed downwards
        # Horizontal moves along sub passages are undirected (can move left or right freely)
        # We assume she can move horizontally freely between intersections on same main passage level
        # She walks intersections to intersections cost 1 per move
        # Walking from intersection to shelf middle or vice versa cost 0.5

        # Thus, layout:
        # 4 horizontal main passages (at y=0,1,2,3), connecting via vertical sub passages at columns 0..N
        # Shelves are between two intersections horizontally, at middle between intersections
        # Intersections are at (row, col) indices (row in 0..3, col in 0..N)

        # Start at shelf 1 middle = (0,0) shelf middle = intersection (0,0) + 0.5 cost to shelf middle
        # End at shelf 4N middle = (3,N-1)

        # Determine minimal walking cost to visit all shelves with books:

        # We'll consider the problem as visiting a set of shelves in order to minimize walking cost
        # Restrictions:
        # - vertical movement only downward along main passages (row increasing)
        # - horizontal movement free on same row

        # Strategy:
        # We have 4 rows, N columns
        # Shelves numbered as per rows and columns
        # We want to find a path from (0,0) shelf middle to (3,N-1) shelf middle visiting all shelves with books

        # Observations:
        # Because vertical moves only allowed downward, path goes from row=0 to row=3 in order
        # To cover shelves with books, on each row we must visit all columns with books on that row
        # On each row, the possible paths go from some leftmost stopping position in that row to some rightmost stopping position in that row

        # Since horizontal moves are free left or right, the minimal walking on a row to cover all required shelves on that row is:
        # walk from leftmost required shelf on that row to rightmost required shelf (if any) horizontally,
        # plus moving from intersection to shelf middle cost (0.5 each side)

        # Because start and end shelf are fixed (start at shelf 1 = row0,col0 middle; end at shelf 4N = row3,colN-1 middle),
        # we must start at leftmost top shelf and end at rightmost bottom shelf

        # So on each row, define the minimal and maximal column of shelves required to be visited.
        # For rows with no books, we can avoid any horizontal travel.

        # Vertical moves:
        # Move downward between main passages cost 1 per move (between intersections)
        # For vertical moves between rows, she must be at an intersection at column c
        # So path is intersection to intersection, plus half cost to shelf middle when stopping

        # On each row, she will move horizontally from some entry column to some exit column,
        # visiting all shelves with books horizontally
        # Then move down to next row at position exit column

        # Since only forward vertical moves allowed, but horizontal moves free, we can store:
        # For each row, the minimal and maximal column of shelves to visit (if any)
        # On row 0, start at col 0 shelf middle
        # On row 3, end at col N-1 shelf middle

        # On rows 1 and 2, need to find optimal route visiting all required shelves

        # We can solve by dynamic programming over rows, keeping track of possible entry and exit columns on each row:

        # However, we have constraints in the problem to write a correct solution from scratch

        # Let's formalize the problem:

        # For each row r from 0 to 3:
        #   Determine min_col[r], max_col[r] of shelves with books (or None if no books)
        # Start:
        #   At row 0, start at col=0
        # End:
        #   At row 3, must end at col=N-1

        # For rows with no books, min_col[r] = max_col[r] = None

        # DP approach:
        # At each row r, we arrive at some column c
        # We must cover all shelves in [min_col[r], max_col[r]] if they exist
        # The cost of visiting shelves on row r starting at enter column c:
        #   If no books => cost 0, only need to be at column c to descend at that row
        #   Else, must walk from c to one end (min or max), then walk horizontally through all shelves and exit at min or max (whichever gives minimal cost)
        #   Because horizontal moves cost 1 per move between intersections and 0.5 for shelf, total walking per horizontal unit is 1 per column
        #   But walking between intersections cost 1, walking intersection<->shelf middle 0.5, we have to consider precisely

        # Correction:
        # Horizontal moves are between intersections at columns 0..N
        # Shelves are between 2 intersections horizontally (between col and col+1)
        # Walking from intersection to shelf middle is 0.5
        # So moving horizontally from shelf middle at col a to shelf middle at col b is:
        # From shelf middle at col a: 0.5 (to intersection a)
        # Horizontal cost between intersections: |b - a| * 1
        # To shelf middle at col b: 0.5
        # So total = |b - a| + 1

        # So traveling horizontally from shelf middle at col a to shelf middle at col b costs (|b-a| + 1)

        # For vertical moves down:
        # Moving vertically between intersections between row r and r+1 at column c: cost 1
        # Moving from shelf middle to intersection vertical at same row cost 0.5

        # So from shelf middle row r col c to shelf middle row r+1 col c vertical move costs:
        # 0.5 (to intersection at row r)
        # +1 (vertical move)
        # +0.5 (to shelf middle at row r+1)
        # = 2.0

        # So vertical move directly below from shelf middle col c row r to shelf middle col c row r+1 costs always 2

        # Thus vertical moves can only be done in straight lines at intersection columns

        # Algorithm:
        # Since vertical moves allowed only downward at same column, to move from row r to r+1, we must be at some column c
        # We have to choose c on row r to position ourselves to vertical move down
        # On row r, we can visit shelves from min_col[r] to max_col[r]
        # How to model cost to enter and exit row r at columns (left, right)

        # Because horizontal moves between shelves cost |right-left| + 1 (from shelf middle at left to shelf middle at right)
        # But she can start and end at any shelf middle on that row as long as all shelves are covered

        # To simplify:
        # For each row r, define segment of shelves to be visited from min_col[r] to max_col[r]
        # On that row, only shelves in this range are visited
        # She can choose to start at min_col[r] shelf middle or max_col[r] shelf middle, and end at the opposite

        # Vertical moves use columns where vertical passages exist (columns 0..N)
        # Shelves at columns 0..N-1 between intersections

        # Important: vertical passages are at columns 0..N
        # Shelf middles at columns 0..N-1

        # On each row r:
        # Possible entry and exit points are intersection columns c in [min_col[r], max_col[r]+1], because shelves are between two intersections
        # Actually entrance and exit points for vertical moves are at intersections column c in 0..N

        # There is a subtlety here:
        # To cover shelves from min_col to max_col, she must walk horizontally from that minimal to maximal shelf
        # She can enter row r at the intersection left or right of that segment

        # Let's model row r visits as visiting shelves between s and t (min_col[r], max_col[r])
        # She can enter row r at intersection c_in and exit at intersection c_out (both in [s, t+1])


        # Because the shelf between intersections c and c+1
        # So shelf col c is between intersection at column c and c+1
        # To cover shelf col c she must be able to move from intersection c to intersection c+1 horizontally.

        # Our state variable in DP will be the column where she arrived at row r (vertical passage column), representing the intersection where she descends.

        # On row r, to cover shelves from s to t, she needs to be able to reach intersection s and intersection t+1 because shelves between s and t correspond to passages between intersections s..t+1

        # The walking cost on row r from intersection c_in to cover [s, t] shelves and exit at intersection c_out is:
        # horizontal walking between intersections (c_in to s or t+1 or c_out)
        # plus 0.5 cost each time going to shelf middle from adjacent intersection

        # Implement DP:

        # We will keep for each row r:
        # possible entry intersections: columns in [0..N]
        # possible exit intersections: columns in [0..N]

        # We'll calculate minimal cost to cover shelves in row r starting at entry intersection c_in and exiting intersection c_out

        # But since on row 0 start is fixed at shelf 1 middle (row0, col0)
        # which is between intersection 0 and 1, but the start position is shelf middle col0,
        # the vertical passage column is ambiguous: vertical passages at intersections column 0..N

        # Because she starts at shelf middle col=0 (between intersections 0 and 1)
        # She can start vertical move at either intersection 0 or 1 (both adjacent to shelf 0)

        # Priority is to define DP as minimal cost to reach vertical column c at row r

        # We will model DP[r][c]: minimal cost to reach intersection c at row r (after visiting shelves on row r)

        # At row 0:
        # We start at shelf middle col=0
        # So she can start at intersection 0 or 1 with cost 0.5 (from shelf to intersection)
        # Because vertical passage columns at 0..N

        # Define function cost_to_cover_row(r, c_in, c_out):
        # returns minimal cost to visit all shelves on row r covering [min_col[r], max_col[r]] from entrance at intersection c_in and exit at intersection c_out

        # Steps to compute cost_to_cover_row:
        # If no books on row r, cost = abs(c_out - c_in) (walk along main passage at row level) (cost from intersection to intersection)
        # shelves must be visited on [min_col, max_col] for row r
        # To cover shelves from s to t:
        # must walk horizontally from c_in to s, then from s to t+1, then from t+1 to c_out in intersections
        # plus 0.5 cost to shelf middle left and right (since putting books), or maybe just once each side

        # Actually, she put the books only at shelf middles
        # She must stop at shelf middles on shelves that have books (cannot put books from intersections)

        # So the minimal cost strategy is to walk from c_in to one end (s or t+1), walk through all shelf segments, then to c_out

        # There are two possible horizontal routes on row r:
        # 1. From c_in to s, walk shelves from s to t+1, then to c_out
        # 2. From c_in to t+1, walk shelves backward from t+1 to s, then to c_out

        # Walking horizontally between intersections cost: abs(c_in - s) + (t+1 - s) + abs(c_out - t -1)
        # Or abs(c_in - (t+1)) + (t+1 - s) + abs(c_out - s)

        # Adding 0.5 cost on each shelf for putting books:

        # Because she puts books at shelf middle, and shelves are between intersections s..t+1
        # For each shelf in [s..t]:
        # Putting books cost 0 because she only stops at shelf middle (which she must reach)
        # Actually cost is the walking cost, the code states reaching shelf middle 0.5 cost from intersection, but since she visits all shelves between s and t, and walks the horizontal distances between intersections, that cost is embedded in the walking cost

        # Simplify:
        # To cover shelves from s to t walking horizontally from c_in to c_out following through s..t+1, cost is:
        # distance to reach shelf segment: abs(c_in - s or t+1)
        # length of shelf segment: (t+1 - s)
        # distance from segment end to c_out: abs(c_out - otherSide)
        # plus 1 for each end to account for 0.5 to shelf middle each side?
        # Actually, since we walk intersection to intersection, and shelf middle is 0.5 cost from intersection, then we add 0.5 at each end?

        # Let's account shelf middle cost correctly:
        # For shelves, each shelf middle costs 0.5 from adjacent intersection
        # So to visit one shelf we spend at least 0.5 from intersection to shelf middle
        # But when walking horizontally through the shelf segment, the cost of visiting shelves is accounted in the horizontal walking between intersections plus the 0.5 cost moving to shelf middle at start and end

        # So for the horizontal path covering shelves from s to t, we add 0.5 cost to enter the first shelf middle and 0.5 cost to leave the last shelf middle

        # Therefore, horizontal cost to cover shelves from s to t by walking intersections from c_in to c_out is:

        # cost = abs(c_in - x) + (t+1 - s) + abs(c_out - y) + 1
        # where (x,y) is either (s, t+1) or (t+1, s) depending on path direction
        # The +1 accounts for 0.5+0.5 cost entering and leaving shelf middles

        # DP:

        # For each row r:
        # if there are no books:
        #   dp[r][c_out] = min over c_in of dp[r-1][c_in] + abs(c_out - c_in) + 0 vertical move cost (if r>0)
        # if there are books [s,t]:
        #   dp[r][c_out] = min over c_in of dp[r-1][c_in]
        #       + vertical_move_cost from c_in at r-1 to c_in at r =2
        #       + minimal horizontal cost covering shelves at row r from c_in to c_out

        # But vertical moves are only allowed if c_in == c_out (since vertical passages are columns)
        # Because vertical moves down happen at same column

        # So vertical moves cost 2 if c_in == c_out else infinite (not valid)

        # Thus:
        # dp[r][c] = min over c' of {
        #   dp[r-1][c'] +
        #   (2 if c' == c else INF) +  # vertical move cost
        #   horizontal covering cost on row r starting at c and ending at c
        # }

        # Since vertical moves fixed on column, the enter and exit column on a row must be the same to go vertical down

        # That means on each row, we enter and exit at same column c

        # Horizontal covering cost from c_in to c_out on row is now from c to c (same column) plus cover shelves [s,t].

        # Horizontal covering cost with same start/end c is:

        # Option 1:
        # walk from c to s, walk shelves from s to t+1, then back to c
        # cost = abs(c-s) + (t+1-s) + abs(c - (t+1)) + 1
        # Option 2:
        # walk from c to t+1, walk shelves backward from t+1 to s, then back to c
        # cost = abs(c - (t+1)) + (t+1 - s) + abs(c - s) + 1

        # Both equal
        # Simplify:
        # cost = abs(c - s) + abs(c - (t+1)) + (t+1 - s) + 1

        # Therefore horizontal cost at row r with shelves from s to t and start/end column c is:

        # horizontal_cost(r,c) = abs(c - s) + abs(c - (t+1)) + (t+