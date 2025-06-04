class Shelf:
    def __init__(self, shelf_id: int, has_book: bool):
        self.id = shelf_id
        self.has_book = has_book

class PassagePoint:
    def __init__(self, horizontal_idx: int, vertical_idx: int):
        self.h = horizontal_idx
        self.v = vertical_idx

    def distance_to_shelf_middle(self) -> float:
        # Distance from an intersection point to the middle of an adjacent shelf (0.5 cost)
        return 0.5

class LibraryGraph:
    def __init__(self, n: int, books_pattern: str):
        self.n = n
        self.total_shelves = 4 * n
        # Create shelves with boolean if there are books or not
        self.shelves = [Shelf(i + 1, books_pattern[i] == 'Y') for i in range(self.total_shelves)]

        # The library layout specifics:
        # Horizontal passages rows: 4 (numbered 0 to 3)
        # Vertical passages columns: n+1
        # She moves forward on main passages (horizontal passages) from top to bottom (0 to 3)
        # She can move only on main passages forward direction (downwards)
        # She can move horizontally on sub passages between intersections
        # Allowed stops: shelf middles or intersections

    def shelf_position(self, shelf_id: int) -> PassagePoint:
        # Given shelf id (1-based), find the vertical and horizontal position
        # Shelves distributed on rows 0 to 3, vertically from left to right along sub passages 1..n columns
        row = (shelf_id - 1) // self.n
        col = (shelf_id - 1) % self.n + 1
        return PassagePoint(row, col)

    def compute_minimum_cost(self) -> int:
        # Abstract route planner engine:
        route_engine = RoutePlanner(self.n, self.shelves)
        return route_engine.plan_route()

class RoutePlanner:
    def __init__(self, n: int, shelves: list):
        self.n = n
        self.shelves = shelves
        # Preprocessing book shelves by their positions per row
        self.books_by_row = [[] for _ in range(4)]
        for shelf in shelves:
            if shelf.has_book:
                row = (shelf.id - 1) // n
                pos_in_row = (shelf.id - 1) % n + 1
                self.books_by_row[row].append(pos_in_row)

        # She starts at the top-left (intersection at row 0, col 0),
        # and ends at bottom-left (intersection at row 3, col 0)

    def plan_route(self) -> int:
        # State abstraction:
        # For each row from 0 to 3, we select the range of shelves to visit on that row (if any)
        # Minimal walking cost within a row is minimal walking along the row's sub passages plus shelf middles

        # She can only move forward on main passages: row 0 to row 3 in order
        # Between rows must walk vertically down on main passages: cost = 1 per row step
        # To cover the shelves in a row:
        # She must start at the left intersection (col=0), move to leftmost needed shelf,
        # then walk to rightmost needed shelf, then back to left intersection, or only one direction if optimized

        # The problem is a variant of shortest path with constraints and ordered visits per row

        from math import inf

        # If no books in a row => just go straight down: cost 1 per vertical move
        # When there are books, find min max indices in that row

        # dp[row][pos] - minimal cost to have covered all shelves up to given row
        # pos = 0 means at left intersection (col 0)
        # pos = 1 means at rightmost shelf visited in this row (max_col)
        # Since she must finish at left intersection row 3 col 0 at the end

        # We'll define the dp to carry cost of having completed all rows up to i, and currently positioned at pos on that row

        dp = [[inf, inf] for _ in range(4)]
        # Starting at row 0, left intersection col 0, cost 0
        dp[0][0] = 0

        for row in range(4):
            books = self.books_by_row[row]
            if not books:
                # No shelves to visit on this row
                if row == 0:
                    # start row 0 at left intersection, no shelves: cost 0 or inf handled above
                    continue
                else:
                    # vertical move cost 1 to next row from previous row pos
                    prev_dp = dp[row-1]
                    # can only come from pos 0 or 1 of previous row, add cost 1 to move down main passage
                    dp[row][0] = min(prev_dp) + 1
                    dp[row][1] = inf  # cannot stand at rightmost shelf if no shelves in this row
            else:
                leftmost = min(books)
                rightmost = max(books)

                vertical_move_cost = 1
                # To reach shelves, must move horizontally from col 0 at row start to leftmost shelf middle(0.5), 
                # then walk to rightmost shelf middle (difference between positions),
                # then decide if finish at left or right side for next row moves

                # horizontal passages between intersections cost 1 per segment (between sub passages)
                # distance between two shelf middles (positions along row) = difference in col indices * 1
                # plus 0.5 to get on shelf, 0.5 to get off shelf

                # walk to first shelf middle from left intersection on the same row:
                # 0.5 cost to shelf middle + (leftmost - 1) cost horizontally (each passage 1 cost)
                # Because moving from col 0 to col leftmost on sub passages costs (leftmost - 1), each step 1 cost
                # Adding 0.5 to step into shelf middle

                # One step along vertical main passage = 1 cost
                # One step along horizontal passage between intersections = 1 cost
                # Moving from shelf middle to intersection = 0.5 cost

                # Let's compute cost scenarios carefully for using dp:

                prev_dp = dp[row - 1] if row > 0 else [0, 0]

                # We can arrive at current row's left intersection (col 0) either from previous row's left or right, plus vertical move cost =1
                # We want minimal total cost finishing at left or right side of shelves visit on this row

                # Options moving within row:
                # Scenario A: Start at left intersection, go to leftmost shelf, then to rightmost shelf, then come back to left intersection
                # Scenario B: Start at left intersection, go to rightmost shelf, then back to leftmost shelf, then back to left intersection (longer, ignore)
                # We want minimal sub-route covering all shelves between leftmost and rightmost

                # However, because she can stop only at shelf middles or intersections,
                # she must put books at all shelves with books => must cover full segment [leftmost, rightmost]

                # Cost components on this row:
                # - vertical move from previous row intersection to this row intersection (1)
                # - moving horizontally from left intersection to furthest leftmost shelf middle: (leftmost -1) * 1 + 0.5
                # - moving horizontally between shelves in this row: rightmost - leftmost * 1
                # - moving horizontally back to left intersection: (rightmost -1)*1 + 0.5

                # Because she can finish on left or right, we consider two states dp[row][0] and dp[row][1]
                # dp[row][0]: finishing at left intersection (col 0)
                # dp[row][1]: finishing at rightmost shelf middle (col rightmost)

                # From previous dp states {left intersection (pos0), rightmost shelf (pos1)},

                # Transition 1: finish previous row at left intersection (pos0), then vertical move 1 to current left intersection

                cost_to_cover_row = 0
                # horizontal cost from left intersection (col0) to leftmost shelf middle
                cost_to_leftmost = (leftmost - 1) + 0.5
                # horizontal cost between leftmost and rightmost shelves middles
                cost_between = rightmost - leftmost
                # horizontal cost from rightmost shelf middle back to left intersection
                cost_back_to_left = (rightmost - 1) + 0.5

                # Total cost to cover all books in row starting and ending at left intersection:
                cost_cover_left = cost_to_leftmost + cost_between + cost_back_to_left
                # Total cost to cover all books in row starting at left intersection, ending at rightmost shelf middle:
                cost_cover_right = cost_to_leftmost + cost_between

                # From previous row dp:
                dp_left = min(
                    prev_dp[0] + vertical_move_cost,
                    prev_dp[1] + vertical_move_cost + (rightmost - 1) + 0.5  # coming from prev rightmost to current left intersection via vertical and horizontal
                )
                dp_right = min(
                    prev_dp[0] + vertical_move_cost + cost_back_to_left - 0.5,  # previous left + vertical + horizontal back cost to right shelf middle
                    prev_dp[1] + vertical_move_cost + (rightmost - leftmost)  # previous right + vertical + horizontal partial
                )

                # Actually transitions above are complicated, but since forward direction on main passage only, 
                # she comes vertically down at column 0 from previous row, so previous dp[1] must pay detour to return to left intersection?

                # Simplifying: assume she always comes down on column 0 intersection from previous row
                # So previous row dp[1] states must include cost to get back to col 0 intersection in previous row.
                # Our DP always finishes a row at either left intersection or right shelf middle of that row

                # To align with problem sample answers, we do as follows:

                # Compute new dp for current row ending at left intersection (pos 0):
                # - Must pay vertical cost 1 from previous row’s left intersection (pos0)
                #   + cost to cover shelves in this row (full trip left to right to left)

                # From pos0 previous row:
                cost_pos0_to_0 = prev_dp[0] + vertical_move_cost + cost_cover_left
                # From pos1 previous row (right shelf middle), she must go to left intersection vertically with extra cost 
                # but since forward only on main passages downwards and in sub passages horizontally, she must walk back horizontally:
                # Actually going backward is forbidden on main passages => we force return to left intersection in prev row
                # So consider that prev_dp[1] includes penalty to come back to left intersection at prev row.
                # For DP correctness, we assume at every row ending at pos1, reach left intersection at that row cost is included to next row

                cost_pos1_to_0 = prev_dp[1] + vertical_move_cost + cost_cover_left

                dp[row][0] = min(cost_pos0_to_0, cost_pos1_to_0)

                # For dp[row][1], ending at rightmost shelf middle:
                # Start at left intersection, cover shelves left to right, stop at rightmost shelf, no return to left intersection

                cost_pos0_to_1 = prev_dp[0] + vertical_move_cost + cost_cover_right
                cost_pos1_to_1 = prev_dp[1] + vertical_move_cost + cost_cover_right

                dp[row][1] = min(cost_pos0_to_1, cost_pos1_to_1)

        # Finally she must end at bottom-left intersection (row 3, col 0)
        # If dp[3][1] finished at rightmost shelf middle, must return to left intersection:
        # cost to move horizontally from rightmost shelf middle to left intersection = (rightmost - 1) + 0.5

        books_in_last_row = self.books_by_row[3]
        if books_in_last_row:
            leftmost = min(books_in_last_row)
            rightmost = max(books_in_last_row)
            return_to_left_cost = (rightmost - 1) + 0.5
            res = min(dp[3][0], dp[3][1] + return_to_left_cost)
        else:
            res = dp[3][0]

        # The problem requires integer cost output
        # Costs calculated include 0.5 steps, all costs should sum to integer as per problem examples
        return int(round(res))

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        books_pattern = input().strip()
        library = LibraryGraph(N, books_pattern)
        print(library.compute_minimum_cost())