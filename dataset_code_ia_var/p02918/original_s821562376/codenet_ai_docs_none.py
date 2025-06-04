N, K = map(int, input().split())
S = input()
packet = []
packet_len = 1
direction = S[0]
seq = 1
for i in range(1, N - 1):
    if S[i] == direction:
        seq += 1
    else:
        packet.append(seq)
        seq = 1
        direction = S[i]
        packet_len += 1
if S[N - 1] == direction:
    seq += 1
    packet.append(seq)
else:
    packet.append(seq)
    seq = 1
    direction = S[N - 1]
    packet.append(seq)
    packet_len += 1
num = 2 * K + 1
if packet_len == 1 or packet_len == 2 or num >= packet_len:
    print(N - 1)
elif num < packet_len:
    rem = packet_len - num
    print(N - rem - 1)