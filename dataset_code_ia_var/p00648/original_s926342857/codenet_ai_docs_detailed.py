def main():
    """
    Main function to read input, process television program schedules,
    and calculate the minimum number of sessions needed to watch selected programs,
    according to the problem specifications.
    """
    while True:
        # Read number of programs for the current dataset
        n = int(input())
        if n == 0:
            # Termination condition (end of input)
            break

        # Mapping from program names to their indices in the program list
        name_to_index = {}
        # Table of program data; each entry: [start_time, end_time, is_selected, name]
        program_table = []

        # Read each program's information
        for i in range(n):
            # Program data: name, week, start_time
            nm, w, s = input().split()
            w = int(w)
            s = int(s)
            # Compute hours and minutes from start_time in HHMM format
            h = s // 100
            m = s % 100
            # Compute the starting minute offset within the week (0 <= s < 10080)
            s = (1440 * w + h * 60 + m) % 10080  # Minutes since the start of the week
            e = s + 30  # Each show lasts 30 minutes
            # Append the processed data: [start, end, is_selected, name]
            program_table.append([s, e, 0, nm])
            # Map name to index for quick access
            name_to_index[nm] = i

        # Number of selected programs to watch
        num_selected = int(input())
        for _ in range(num_selected):
            selected_name = input()
            # Mark the selected program in the table
            program_table[name_to_index[selected_name]][2] = 1

        # If there is only one program, only one session is needed
        if n == 1:
            print(1)
            continue

        # Sort all programs by their starting times and by selection flag (selected first in case of tie)
        program_table.sort(key=lambda x: (x[0], x[2]))

        # Find the index k of the first selected program in the sorted list
        for i in range(len(program_table)):
            if program_table[i][2]:
                k = i
                break

        # ans: minimal number of needed sessions
        # i: current program index (starting with the selected one)
        # j: next program index
        ans = 1
        i = k
        j = k

        while True:
            # Move to the next program in a circular way (wrap around)
            j += 1
            if i >= n:
                i = 0
            if j >= n:
                j = 0
            if j == k:
                # We have circled back to the starting point
                break

            # Calculate overlap for weekly wrap-around
            end_correction = program_table[i][1] - 10080 if program_table[i][1] >= 10080 else 0

            # If the next program starts within the current one's time window
            # (standard or wrapped around the week)
            if (program_table[i][0] <= program_table[j][0] < program_table[i][1]) or \
               (program_table[j][0] < end_correction):
                # If both overlap and both are selected, impossible to watch both
                if program_table[j][2] and program_table[i][2]:
                    ans = -1
                    break
                # If the next program is selected, switch to it
                elif program_table[j][2]:
                    i = j
            elif (program_table[j][0] <= program_table[k][0] < program_table[j][1]):
                # Special case: ignore if the starting program is covered in the interval of j
                pass
            else:
                # Need a new session for the next program (not overlapping)
                ans += 1
                i = j

        print(ans)

if __name__ == "__main__":
    main()