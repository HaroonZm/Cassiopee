import sys
from heapq import heappush, heappop, heapreplace

def solve():
    """
    Reads competition events from standard input and determines the team leading
    at the end of the competition. The logic uses a priority queue to simulate 
    ranking changes over time based on scores and time progression.

    Input:
        The first line contains three integers:
            N: number of teams
            R: number of events (not directly used)
            L: final timestamp (competition end time)
        Each subsequent line describes an event with three integers:
            d: team id (1-based)
            t: timestamp of event (strictly increasing)
            x: score change for team d at time t

    The program prints the ID of the team who led by time L (with tie-breaker on 
    smallest team-id).
    """
    # Read input data from stdin
    file_input = sys.stdin

    # Parse number of teams (N), number of events (R), and final competition time (L)
    N, R, L = map(int, file_input.readline().split())
    
    # Initialize the priority queue:
    # Each entry: [score, team_id, leading_duration]
    # - score: total inverse score for ordering (lower = better)
    # - team_id: team's unique identifier (used for tie-breaking)
    # - leading_duration: how long the team was leading
    pq = [[0, i, 0] for i in range(1, N + 1)]
    
    # Map team_id to their tuple in the priority queue for quick access and updates
    m = dict(zip(range(1, N + 1), pq))
    
    # Variable to track the timestamp of the previous event
    pre_t = 0

    # Iterate through each event line in the input
    for line in file_input:
        # Parse event information: d (team), t (time), x (score change)
        d, t, x = map(int, line.split())
        
        # The current leading team is always at the top of the priority queue (min-heap)
        team = pq[0]

        # Update the duration that the leading team held the lead (since previous event)
        team[2] += t - pre_t

        # Advance the time marker for next iteration
        pre_t = t

        if team[1] == d:
            # If the team to update is currently leading

            # Adjust the score for this team
            team[0] -= x  # The heap is min-heap on score

            # If x < 0 (score increases for this team), their score improves and position may shift
            if x < 0:
                # Restore heap ordering since score improved
                heapreplace(pq, team)
        else:
            # The scoring team is not currently at the top, must update their record in the heap

            # Copy the team's current record to avoid aliasing issues
            scored_team = m[d][:]

            # Update the score for this team
            scored_team[0] -= x

            # Push the updated team record onto the heap
            heappush(pq, scored_team)

            # Mark the old record in the mapping as stale with leading_duration = -1
            m[d][2] = -1

            # Update mapping to the new heap item
            m[d] = scored_team

        # Remove stale entries (teams whose heap records are no longer valid)
        while pq[0][2] == -1:
            heappop(pq)

    # After all events, update the leading time for the team at the top until end-time L
    pq[0][2] += L - pre_t

    # Determine which team led for the longest total duration
    # Tie-breaker: team with lowest id if durations are equal
    ans_team = max(pq, key=lambda x: (x[2], -x[1]))

    # Output the answer (winning team's id)
    print(ans_team[1])

# Invoke the main solving function
solve()