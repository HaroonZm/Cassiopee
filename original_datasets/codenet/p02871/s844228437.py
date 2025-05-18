out = open('out.txt','a')
class graph:
    INF = 10000
    G = []
    Path = []
    E = 0
    V = 0
    def __init__(self):
        dataRaw = raw_input()
        raw = dataRaw.strip().split(' ')
        self.E = int(raw[0])+1
        self.V = int(raw[1])
        self.G = [[self.INF] * (self.E) for i in range(self.E)]
        self.Path = [[0] * (self.E) for i in range(self.E)]

        # check unicom component
        def find(root, parent):
            while root != parent[root]:
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

        def connect( u, v, parent) :
            # ru = find(u, parent)
            rv = find(v, parent)
            parent[u] = rv

        # father = [0]* (self.E)

        # for i in range(1,self.E):
        #    father[i] = i

        for _ in range(0,self.V):
            dataRaw = raw_input()
            raw = dataRaw.strip().split(' ')
            i = int(raw[0])
            j = int(raw[1])
            k = int(raw[2])
            self.G[i][j] = k
            self.G[j][i] = k
            # connect(i,j,father)

        # compent = set()
        # for i in range(1,self.E):
        #    compent.add(find(i,father))

        #print "compoent : ",
        #print compent
        #print father

        for i in range(1,self.E):
            self.G[i][i] = 0

        for i in range(0,self.E):
            for j in range(0, self.E):
                for k in range(0, self.E):
                    if self.G[i][k]+self.G[k][j] < self.G[i][j]:
                        self.G[i][j] = self.G[i][k]+self.G[k][j]
                        self.Path[i][j] = k

        #for i in self.G :
        #    print i

    def shortPath(self,i,j):
        path = []

        def core(i,j,path):
            if self.Path[i][j] == 0:
                if len(path) == 0 or path[-1] != i:
                    path.append(i)
                path.append(j)
                return
            else :
                core(i, self.Path[i][j],path)
                core(self.Path[i][j], j, path)
        core(i, j,path)
        path.pop(0)
        return path

class driver :
    plan = []
    order = set()
    location = 1
    nextSegmentLeftTime = 0
    target = 1

    def __init__(self,g):
        self.map = g

    def route(self):
        # choose target
        # route
        # print self.order,
        # print self.plan
        if len(self.order)==0 and len(self.plan) == 0:
            self.order.add(1)

        last = self.location

        if len(self.plan) > 0:
            last = self.plan[-1]

        # out.write("| last : " + str(last) +" "+ str(type(last)) )
        if len(self.order) > 0:
            for i in self.order:
                path = self.map.shortPath(last,i)
                for j in path:
                    self.plan.append(j)
                last = i
            self.order = set()

        # print self.order,
        # print self.plan
        if len(self.plan) > 0:
            self.target = self.plan[0]
            self.nextSegmentLeftTime = self.map.G[self.location][self.target]
            self.plan.pop(0)

    def move(self):
        #out.write('-1\n')
        #return

        if self.location == self.target:
            #stay
            #out.write('-1\n')
            print (-1)
            return

        assert(self.nextSegmentLeftTime > 0)
        self.nextSegmentLeftTime = self.nextSegmentLeftTime - 1
        #out.write(str(self.target)+'\n')
        print (self.target)
        if self.nextSegmentLeftTime == 0:
            self.location = self.target

    def onRoute(self):
        return self.nextSegmentLeftTime != 0

class shop :
    order = set()

class timer :
    orders = []
    times = []
    orderIndex = 0
    currTime = 0
    Tmax = 0
    def __init__(self):
        Tmax = raw_input()
        self.Tmax = int(Tmax)
        for i in range(0, self.Tmax):
            n = raw_input()
            n = int(n)

            if n==0 :
                continue
            else :
                dataRaw = raw_input()
                data = dataRaw.strip().split(' ')
                self.times.append(i+1)
                self.orders.append(int(data[1]))

    def run(self,shop,driver):
        while self.currTime < self.Tmax:
            self.currTime = self.currTime + 1
            '''
            out.write ("================================\n")
            out.write ("curr time : " + str(self.currTime))

            out.write ("status before : ")
            out.write ("shop status : " + str(shop.order))
            out.write ("driver status : ")
            out.write ("order : " + str(driver.order),)
            out.write ("| plan : " + str(driver.plan),)
            out.write ("| on route : " + str(driver.onRoute()))
            out.write ("| location : " + str(driver.location),)
            out.write ("| target : " + str(driver.target),)
            out.write ("| left time : " + str(driver.nextSegmentLeftTime) + '\n')
            '''
            # add goods
            if self.orderIndex < len(self.times) and self.currTime == self.times[self.orderIndex]:
                if driver.map.G[1][self.orders[self.orderIndex]] < 10000:
                    shop.order.add(self.orders[self.orderIndex])
                self.orderIndex = self.orderIndex + 1

            if driver.onRoute() == False and driver.location == 1:
                driver.order = driver.order | shop.order
                shop.order = set()

            if driver.onRoute() == False:
                driver.route()

            driver.move()

            
            out.write ("status after : ")
            out.write ("shop status : " + str(shop.order))
            out.write ("driver status : ")
            out.write ("order : " + str(driver.order),)
            out.write ("| plan : " + str(driver.plan),)
            out.write ("| on route : " + str(driver.onRoute()))
            out.write ("| location : " + str(driver.location),)
            out.write ("| target : " + str(driver.target),)
            out.write ("| left time : " + str(driver.nextSegmentLeftTime) + '\n')
            out.write ("================================\n")
            '''

if __name__=="__main__":

    shop = shop()
    g = graph()

    #print(g.shortPath(1,6))

    driver = driver(g)
    ti = timer()
    ti.run(shop,driver)