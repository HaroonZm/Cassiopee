import sys

def process_dataset(M, T, P, R, submissions):
    # Initialize data structures to store team information:
    # - solved_problems: a set of problems solved by the team
    # - penalty_submissions: count of incorrect submissions before solved for each problem
    # - accepted_time: time at which the problem was solved
    # We use dictionaries keyed by team number, then by problem number.
    solved_problems = {team: set() for team in range(1, T + 1)}
    penalty_submissions = {team: {prob: 0 for prob in range(1, P + 1)} for team in range(1, T + 1)}
    accepted_time = {team: {} for team in range(1, T + 1)}

    # Process each submission record
    for m_k, t_k, p_k, j_k in submissions:
        # If the problem is already solved by this team, ignore further submissions as per problem statement
        if p_k in solved_problems[t_k]:
            continue

        if j_k == 0:
            # Correct submission: record time and mark problem as solved
            solved_problems[t_k].add(p_k)
            accepted_time[t_k][p_k] = m_k
        else:
            # Incorrect submission: increment penalty count
            # Only matters if the problem is later solved
            penalty_submissions[t_k][p_k] += 1

    # Calculate team results: (number_of_solved_problems, total_time)
    team_results = []
    for team in range(1, T + 1):
        solved_count = len(solved_problems[team])
        total_time = 0
        for prob in solved_problems[team]:
            # Total time for a solved problem includes:
            # accepted submission time + 20 * penalty submissions before acceptance
            total_time += accepted_time[team][prob] + 20 * penalty_submissions[team][prob]
        team_results.append((team, solved_count, total_time))

    # Sorting rules:
    # 1. More problems solved -> higher rank
    # 2. If tie in solved problems, smaller total time -> higher rank
    # 3. If tie in both, same rank
    # Teams with same rank are sorted in decreasing team number order
    # We sort first by solved_count desc, then total_time asc,
    # and finally team number ascending for grouping, but when printing same rank,
    # order is descending by team number

    # Sort by team number ascending first for stable grouping
    team_results.sort(key=lambda x: x[0])

    # Then sort by solved_count desc, total_time asc
    team_results.sort(key=lambda x: (-x[1], x[2]))

    # Group teams by (solved_count, total_time) to determine ties
    from itertools import groupby
    output_groups = []
    for key, group in groupby(team_results, key=lambda x: (x[1], x[2])):
        grouped_teams = list(group)
        # Within the tie group, sort by decreasing team number
        grouped_teams.sort(key=lambda x: x[0], reverse=True)
        output_groups.append(grouped_teams)

    # Build output string:
    # Teams in different groups are separated by commas
    # Teams in the same group are separated by equal signs '='
    output_parts = []
    for group in output_groups:
        if len(group) == 1:
            # Single team in group
            output_parts.append(str(group[0][0]))
        else:
            # Multiple tied teams, join by '='
            output_parts.append('='.join(str(team[0]) for team in group))

    return ','.join(output_parts)

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while idx < len(input_lines):
        MTPR = input_lines[idx].strip()
        idx += 1
        if MTPR == '0 0 0 0':
            # End of all datasets
            break
        M, T, P, R = map(int, MTPR.split())
        submissions = []
        for _ in range(R):
            m_k, t_k, p_k, j_k = map(int, input_lines[idx].split())
            idx += 1
            submissions.append((m_k, t_k, p_k, j_k))
        result = process_dataset(M, T, P, R, submissions)
        print(result)

if __name__ == "__main__":
    main()