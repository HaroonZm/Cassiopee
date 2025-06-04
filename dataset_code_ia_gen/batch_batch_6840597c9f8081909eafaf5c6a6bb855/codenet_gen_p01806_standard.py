import sys
sys.setrecursionlimit(10**7)

def rot_x_neg(die):
    l,r,f,b,d,u = die
    return (d,u,f,b,r,l)
def rot_x_pos(die):
    l,r,f,b,d,u = die
    return (u,d,f,b,l,r)
def rot_y_neg(die):
    l,r,f,b,d,u = die
    return (l,r,u,d,f,b)
def rot_y_pos(die):
    l,r,f,b,d,u = die
    return (l,r,d,u,b,f)

rot_map = {
    'L': rot_x_neg,
    'R': rot_x_pos,
    'F': rot_y_neg,
    'B': rot_y_pos,
}

def solve():
    input=sys.stdin.readline
    while True:
        N = int(input())
        if N==0:
            break
        dice = []
        for _ in range(N):
            x,y = map(int,input().split())
            l,r,f,b,d,u = map(int,input().split())
            rot = input().strip()
            die = (l,r,f,b,d,u)
            bottom_cells = []
            # Simulate the falling and rotations, record bottom number and position
            # bottom position always at (x,y)
            # Each rotation x or y shifts the top/bottom face accordingly.
            # Since the dice always lands on the designated cell at the start and after each rotation,
            # the bottom cell remains (x,y)
            bottom_nums=[]
            cur_die = die
            # At first drop, bottom number overwrite board at (x,y)
            bottom_nums.append( (x,y,cur_die[4]) ) # d is bottom
            for c in rot:
                cur_die = rot_map[c](cur_die)
                bottom_nums.append( (x,y,cur_die[4]) )
            dice.append(bottom_nums)
        # We have N dice, each with list of (x,y,num) for bottom cell after drop and rotations.
        # We must press N buttons (dice) in some order (can repeat dice).
        # After all, sum of numbers on the board cells.
        # Repeated same button yields same sequence.
        # pressing the dice in order sets board cell to bottom num per step, finally last write counts.
        # Our goal is to maximize sum on board after N presses.

        # Since N<=15, board cells can be many positions (-1000 to 1000 coords). 
        # But max we can have is N dice with up to 31 bottom updates, so max 15*31=465 cells affected per full sequence.
        # However many coincide, so total distinct cells <= 15*31=465. Not too large.

        # Idea:
        # For each dice, get final bottom write as list of (cell,num) in order.
        # For the N presses, order them to maximize sum of last write on each cell.

        # Since each press overwrites its bottom cells sequentially, last write remain.
        # Because pressing a dice overwrites the cell multiple times, but only last overwrite per press counts.

        # Observing carefully:
        # The final bottom write of each press is the last in its bottom_nums list.
        # But earlier overwrites in that press are overwritten later in the same press.
        # So only last bottom write per cell in that press counts.

        # But since only one dice allowed per press, and it removes dice after its rotations,
        # so the bottom writing sequence per press is sequential and can't be interrupted.

        # Actually, the board updates per press are sequential overwrites on cells, but since only one cell per press (x,y),
        # and the dice only writing at (x,y), no multiple cells per press to consider.

        # Wait, problem states the dice only writes on the cell it lands on during each rotation.
        # So only one cell per die, given by (x,y) per dice, so the output is only on that cell.

        # But the rotations do not change dice position, only orientation. So all writes in the same cell.

        # So for each dice press, we overwrite the same cell multiple times, finally last value counts.

        # Since the initial board is all zeros.
        # We do N presses.
        # Each press picks a dice i (possibly same multiple times),
        # and writes the last bottom number on dice i's cell (x,y).

        # So we must pick which dice to press at each turn.

        # But we can press dice multiple times, each press overwriting that cell.

        # But since dice have fixed cell positions, some dice may overwrite same cell multiple times.

        # The final sum is sum over all unique cells of the last number written on that cell.

        # We want to select N dice (with repetition), to maximize sum of last numbers per cell.

        # Observation: If we press dice i at time t, it overwrites cell c_i with value last bottom num.

        # The last dice pressed on each cell c determines the value in that cell.

        # So problem reduces to:
        # Out of N presses, assign to dice (possibly repeats),
        # For each cell, last press that wrote that cell determines the value.

        # Since dice writes only on its cell, and we have N presses,
        # and up to N unique cells.

        # Let C be set of unique cells from all dice.

        # For each cell c, we want to know the last dice pressed on c and its last bottom num.

        # To maximize sum over all cells of the last written numbers.

        # We must assign presses to dice so that for each cell c, the last dice assigned to press on c gives maximum value.

        # We can press any dice multiple times, order sequence length N.

        # But the dice presses overwrite only their own cell.

        # So to maximize sum, we want to assign the last press on each cell to the dice with maximum last value for that cell.

        # For example, if cell c is unique to dice i, then pressing dice i last on c sets the value at c.

        # Since multiple dice can have same cell? Probably no, since dice drop positions may overlap.

        # Check if different dice can have the same (x,y)?

        # Problem statement doesn't forbid it.

        # So cells can be overwritten by multiple dice.

        # So for each cell c, we consider dice that write to c.

        # Let's preprocess: for each cell c, find dice that write there and their last bottom number.

        # We want to arrange N presses (sequence of dice indices), possibly with repeats,

        # so that the final written value on each cell c is maximum possible, sum over all c.

        # Since dice presses overwrite their cell.

        # The last dice pressed on that cell c determines that cell's value.

        # So we want to choose the last dice pressed on c to be the dice that writes maximum value at c.

        # So to maximize sum over all cells, we want the last dice pressed on each cell to be the dice with maximum last value at c.

        # The problem is, total N presses.

        # For each cell c, last dice pressed on c is dice_max[c].

        # But presses overwrite only one cell each.

        # So last presses on different cells are different indices.

        # The last press on a cell c is assigned to dice dice_max_c.

        # So for each such dice, it must be pressed at least once.

        # And total presses N.

        # Also, dice can be pressed multiple times.

        # The ordering: last press on cell c is the last press of dice dice_max[c] on that cell.

        # For multiple cells per dice, the last press for that dice can only be last for one cell.

        # Because last presses define cell values.

        # So arranging the order, we can arrange last presses for each cell in any order.

        # But each last press must be unique (since one press at a time).

        # For dice with multiple cells, if their maximum valued cells are multiple, picking last press per cell is impossible since only one last press per dice press.

        # Wait, each dice covers only one cell (x,y).

        # So dice i only writes on cell c_i.

        # So for each cell, dice with that cell writes on it.

        # So cell->dice unique mapping.

        # So cell c has unique dice i writing on it.

        # So last press on c is press of dice i.

        # To maximize sum, for each cell c, use the dice i assigned to it.

        # The question: we have N presses, and dice count N.

        # So each dice must be pressed at least once (since N presses, dice can be repeated).

        # But order is ours to choose.

        # Since only last press for cell matters.

        # If dice i is pressed multiple times, only the last press counts for its cell in final value.

        # So to maximize final sum, for each cell pick the last press of dice i, value is fixed.

        # Others affect order, but sum is same.

        # So just sum over all dice last bottom numbers.

        # So maximum sum is sum over all dice i of their last bottom number.

        # But as problem states, we have N presses, meaning total presses equal to dice count.

        # But we can press same dice multiple times.

        # So best is to press all dice once in any order => sum last bottom number of all dice.

        # But can we do better by pressing a dice multiple times?

        # No, because for each cell assigned to that dice, only last press counts.

        # So pressing a dice multiple times overwrite its cell multiple times, last one wins.

        # So value on that cell is constant per dice last bottom number.

        # So sum of final board is sum of all dice last bottom number for all dice pressed at least once.

        # What if we skip pressing some dice?

        # No, we must press N times.

        # Pressing dice multiple times only overwrite their cell repeatedly. It can’t help other cells.

        # So optimal is pressing each dice once, sum of their last bottom numbers.

        # But N times presses total. If more presses available, pressing unmatched dice multiple times just overwrites same cell, no increase in total sum.

        # Problem states pressing buttons N times total, and have N dice.

        # So pressing each die once.

        # But problem states same button can be pressed multiple times, total presses N.

        # So input N up to 15.

        # Maybe some dice share the same cell? Then the last pressed dice on that cell defines value.

        # Then dice share a cell, we want to pick dice with max value to be last to press on that cell.

        # Could be that dice assigned to same cell, pressing the dice with max value last to that cell beats others.

        # So summary:

        # For each cell c, there may be multiple dice write to c.

        # For each cell c, we want to pick dice with maximum last bottom number to be last on that cell.

        # For that dice, we must press it at least once and ensure its last press is after other dice presses that write on that cell.

        # So ordering matters.

        # Implementing a DP to find best score considering these constraints is complicated.

        # But since N and number of cells are small (<=15 dice), brute forcing order is impossible (N! too big).

        # Instead, the solution:

        # Since dice write on unique cells, no overlapping cells for different dice? Problem allows overlapping.

        # So multiple dice can write to same cell.

        # But only last press on that cell counts.

        # So for each cell c, among dice which write c, last press of one dice defines cell value.

        # So to maximize sum, for each cell c, last press on c must be button with maximum last bottom value for c.

        # Therefore, we want to build a sequence of presses of length N, so that for each cell c, last press on that cell is the max value dice for c.

        # Since a dice may contribute multiple cells?

        # From problem, each die has only one cell x,y.

        # So each die only writes to one cell.

        # So cell->dice mapping is one to one.

        # Meaning multiple dice may write to same cell.

        # So for cells with multiple dice, last press on cell is the dice last pressed on that cell.

        # Since die only write their own cell, cell to dice is one to many.

        # So dice have unique cell.

        # So each cell can have multiple dice.

        # But each dice only writes on their unique cell.

        # So final mapping cell->dice can be multiple.

        # So the bottom line:

        # For each die i, position c_i.

        # For each cell c, dice_i writing c.

        # So for each dice, only their own cell.

        # So to maximize sum, for each cell choose dice with max last bottom value as last press that writes on that cell.

        # Since dice only overwrite their own cell, last press on cell c is from dice in dice_list[c].

        # So if dice_i writes cell c_i

        # We want to press dice with maximum last bottom value last for that cell.

        # To ensure the order feasible, since all dice write only one cell, no dice can be last press to multiple cells.

        # Because that die writes only one cell.

        # So no conflicts.

        # So last press on cell c is dice with max value among dice writing on cell c.

        # So last press per cell is unique dice.

        # So the set of last presses is dice with maximum last bottom number per cell.

        # Now problem reduces to arranging the last press for each cell accordingly.

        # Now, since order can be arranged arbitrarily, and repeats allowed, the max sum is sum over cells c of max last bottom value for c.

        # Then for dice which are not last press on any cell, can be pressed any number of times or not at all, no effect on final score.

        # Since total presses must be N.

        # Then to maximize sum, press dice last on their cell.

        # For other presses, press any dice in any order.

        # So final max score is sum over cells c of max last bottom value for c.

        # So implementation:

        # Map cell to list of dice idx that write it and their last bottom value.

        # For each cell, find max last bottom value.

        # Sum over cells these max values.

        # Output sum.

        # Implement with input accordingly.

        cell_to_values = dict()
        # For each dice i:
        # dice[i] = list of (x,y,num)
        # x,y is fixed per dice, so assign (x,y) -> dice i last bottom num

        for i in range(N):
            x,y,_ = dice[i][0]
            cell = (x,y)
            last_num = dice[i][-1][2]
            if cell not in cell_to_values:
                cell_to_values[cell] = []
            cell_to_values[cell].append( (last_num,i) )
        ans=0
        for cell in cell_to_values:
            vals = cell_to_values[cell]
            maxv = max( v for v,_ in vals )
            ans += maxv
        print(ans)

if __name__=='__main__':
    solve()