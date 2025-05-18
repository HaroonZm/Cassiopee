class Team:
    def __init__(self, num, P):
        self.num = num
        self.times = [ 0 for _ in range(P) ]
        self.solved = [ False for _ in range(P) ]
        self.ps = None
        self.tt = None
    
    def submit(self, m, p, j):
        if j == 0:
            self.solved[p] = True
            self.times[p] += m
        else:
            self.times[p] += 20
    
    def probsSolved(self):
        if self.ps == None:
            self.ps = len(list(filter(lambda x: x, self.solved)))
        return self.ps

    def totalTime(self):
        if self.tt == None:
            total = 0
            for i in range(len(self.solved)):
                if self.solved[i]:
                    total += self.times[i]
            self.tt = total
        return self.tt

if __name__ == '__main__':
    while True:
        M, T, P, R = [ int(x) for x in list(filter(lambda x: x != '', \
            input().strip().split(' '))) ]

        if M == 0 and T == 0 and P == 0 and R == 0:
            break

        teams = [ Team(n + 1, P) for n in range(T) ]

        for _ in range(R):
            m, t, p, j = [ int(x) for x in list(filter(lambda x: x != '', \
                input().strip().split(' '))) ]
            teams[t-1].submit(m, p - 1, j)

        teams.sort(key=lambda t: (-t.probsSolved(), t.totalTime(), -t.num))

        print(teams[0].num, end='')
        for i in range(1, T):
            team = teams[i]
            prevTeam = teams[i - 1]
            if team.probsSolved() == prevTeam.probsSolved() and \
                team.totalTime() == prevTeam.totalTime():
                print("={}".format(team.num), end='')
            else:
                print(",{}".format(team.num), end='')
        print()