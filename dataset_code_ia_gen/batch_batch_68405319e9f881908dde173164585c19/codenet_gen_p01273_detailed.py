# Solution to identify infected computers based on packet transmission records
# Approach:
# 1. We read multiple datasets until we encounter a dataset with N=0 and M=0.
# 2. For each dataset:
#    - We have N computers and M data packets.
#    - The virus starts from computer 1.
#    - We maintain a list or set of infected computers, initialized with computer 1.
#    - We sort the data packets by their time of transmission to simulate the timeline.
#    - For each packet in increasing order of time:
#       If the source computer is infected at that point,
#       then the destination computer becomes infected as well.
# 3. After processing all packets for a dataset,
#    we print the count of infected computers.
# This simulates the infection propagation through the network over time.

import sys

def main():
    input = sys.stdin.readline
    
    while True:
        # Read N (number of computers) and M (number of data packets)
        line = input()
        if not line:
            break
        N, M = map(int, line.split())
        if N == 0 and M == 0:
            # End of all datasets
            break
        
        packets = []
        for _ in range(M):
            t, s, d = map(int, input().split())
            packets.append((t, s, d))
        
        # Sort packets by their time t in ascending order
        packets.sort(key=lambda x: x[0])
        
        # Set of infected computers, initially only computer 1 is infected
        infected = set([1])
        
        # Iterate through packets in time order
        for t, s, d in packets:
            # If source is infected, destination becomes infected
            if s in infected:
                infected.add(d)

        # Print the number of infected computers after processing all packets
        print(len(infected))


if __name__ == "__main__":
    main()