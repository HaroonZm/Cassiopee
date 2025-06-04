KX = input().split()
packet_of_koalas, xisme = int(KX[0]), int(KX[1])
yes_list = ['Y', 'e', 's']
no_list = ['N', 'o']
checker = (packet_of_koalas << 9) + (packet_of_koalas << 1)        # Fancy way to compute 500*K
print(''.join(yes_list) if not (checker < xisme) else ''.join(no_list))