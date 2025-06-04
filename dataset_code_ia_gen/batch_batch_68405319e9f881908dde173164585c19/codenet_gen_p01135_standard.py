import sys
import heapq

def main():
    input=sys.stdin.readline
    while True:
        n,m=map(int,input().split())
        if n==0 and m==0:break
        dist=[[10**9]*n for _ in range(n)]
        adj=[[] for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for _ in range(m):
            a,b,c=map(int,input().split())
            a-=1;b-=1
            dist[a][b]=dist[b][a]=c
            adj[a].append((b,c))
            adj[b].append((a,c))
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                di=dist[i]
                dik=di[k]
                dk=dist[k]
                for j in range(n):
                    nd=dik+dk[j]
                    if nd<di[j]:
                        di[j]=nd
        # determine next hop from each node to dest
        next_hop=[[-1]*n for _ in range(n)]
        for s in range(n):
            for d in range(n):
                if s==d:
                    next_hop[s][d]=d
                    continue
                min_dist=dist[s][d]
                candidates=[]
                for (nx,_c) in adj[s]:
                    if dist[nx][d]+dist[s][nx]==min_dist:
                        candidates.append(nx)
                next_hop[s][d]=min(candidates)

        l=int(input())
        mails=[]
        for i in range(l):
            f,t,tm,*label=input().split()
            f=int(f)-1;t=int(t)-1;tm=int(tm)
            label=label[0]
            mails.append((f,t,tm,label,i))
        # mails sorted by arrival time at origin, input order preserved

        # for each post office
        # store state:
        # queue of mails: list of (arrival_time, label, mail)
        # mail: (orig,f,tm,label,index)
        # mail stores source, dest, arrival time at origin, label, input order
        # mails currently at this office's mail queue
        # employee state: free/busy
        # if busy: when returns

        # we simulate events:
        # event types:
        # 0: mail arrival at office: (time, 0, office, mail)
        # 1: employee returns to office: (time, 1, office)
        # also need to handle starting immediate transfers after returns or mail arrivals

        # store mails remaining per office in list
        mail_queues=[[] for _ in range(n)] # heap: (arrival_time,label,mail object)
        # mails delivered: output result: mail index->delivery time at destination

        delivered=[-1]*l
        # employees state: True if free, False if busy
        employee_free=[True]*n

        # To group mails that must be transferred together when same next_hop and arrival_time and same time as departure
        # We'll process per office when employee free and mails exist

        # we use an event heap
        event_heap=[]
        # add mail arrival events
        for mail in mails:
            f,t,tm,label,idx=mail
            heapq.heappush(event_heap,(tm,0,f,mail))

        # helper to process transfers at office at time T
        def try_start_transfer(office,time):
            if not employee_free[office]:
                return
            if not mail_queues[office]:
                return
            # sort mail_queues by arrival_time,label already heapq so top element is earliest
            # get earliest arrival time and next hop of first mail
            queues=mail_queues[office]
            earliest_time, earliest_label, first_mail = queues[0]
            # find next_hop for each mail to destination
            # group mails by next_hop that share earliest_time arrival_time (<= time? they arrive at earliest_time, employees leave at same time => mails arriving at departure time included)
            # only mails with arrival_time==earliest_time can be bundled
            # time of departure == current time (time)
            # mails arriving at time==departure_time included
            # we need to include mails with same next hop whose arrival_time == earliest_time and arrival_time<=departure_time
            # mails arriving later are not included
            # mails arriving exactly at departure are included

            # first, pick all mails with arrival_time==earliest_time
            same_time_mails=[]
            min_next_hop=10**9
            for at,label,mail in queues:
                if at!=earliest_time:
                    break
                nh=next_hop[office][mail[1]]
                if nh<min_next_hop:
                    min_next_hop=nh
            # gather mails with earliest_time and next_hop == min_next_hop
            # also include mails arriving exactly at departure time (time) that have same next_hop == min_next_hop
            # mails arriving at same time already considered (earliest_time), but mails arriving between earliest_time and time that are <=time must also be included if arrival time==time (tied time)
            # so all mails with arrival_time in {earliest_time,time} and next_hop==min_next_hop
            # but mails in queue always sorted by arrival_time ascending, label ascending
            # mails arrival_time>time cannot be included
            # we gather all mails arriving at earliest_time == at0, plus mails arriving exactly at time (if time>earliest_time)
            # .

            included=[]
            nh=min_next_hop
            # iterate mails to include those with arrival_time==earliest_time and next_hop==nh
            # possibly mails arriving at time == departure time (time), must take together
            remove_indices=[]
            for i,(at,label,mail) in enumerate(queues):
                if at>time:
                    break
                if at==earliest_time or at==time:
                    if next_hop[office][mail[1]]==nh:
                        included.append((at,label,mail))
                        remove_indices.append(i)
                else:
                    break
            # remove included mails from queues
            # as queues is a heap, we cannot just remove by index
            # instead, remove mails included from heap by making a new heap excluding included mails
            included_set=set()
            for at,label,mail in included:
                included_set.add((at,label,mail[4]))
            new_heap=[]
            for item in queues:
                if (item[0],item[1],item[2][4]) not in included_set:
                    new_heap.append(item)
            heapq.heapify(new_heap)
            mail_queues[office]=new_heap

            # employee goes busy
            employee_free[office]=False
            # compute travel time = distance to next_hop (always 1 per problem?)
            # problem states distance can vary,and travel time = distance (distance>=1)
            # So we use distance from office to next_hop[office][dest]
            # but mails have different destinations
            # here next_hop is unique for all included mails: nh

            # distance between office and nh
            # find adj dist
            # problem states edges exist, so find edge cost between office and nh from adj
            # adj[office] contains (v,dist)
            d=0
            for v,c in adj[office]:
                if v==nh:
                    d=c
                    break

            # total trip time = 2*d
            # the employee returns at time + 2*d
            return_time = time + 2*d
            heapq.heappush(event_heap,(return_time,1,office))
            # after time+d, mails arrive at nh office (except that delivering mails to destination ends here)
            # We simulate mail arrival at destination at time+d by generating arrival events at nh or delivering mails

            arrival_time = time + d
            # generate mail arrival events at nh for mails not yet at nh destination
            # if mail destination == nh, delivered at arrival_time
            for at,label,mail in included:
                dest=mail[1]
                idx=mail[4]
                if dest==nh:
                    # delivered
                    delivered[idx]=arrival_time
                else:
                    # add arrival event for mail at nh at arrival_time
                    heapq.heappush(event_heap,(arrival_time,0,nh,mail))

        # process events
        while event_heap:
            time,etype,*rest=heapq.heappop(event_heap)
            if etype==0:
                office,mail=rest
                # mail arrives at office at time
                # append to mail_queues[office]
                # use (arrival_time,label,mail)
                arrival_time, label, idx = time, mail[3], mail[4]
                heapq.heappush(mail_queues[office],(arrival_time,label,mail))
                # after arrival, try start transfer at office time (arrivals and departures at same time share mails)
                try_start_transfer(office,time)
            else:
                office=rest[0]
                # employee returns at time
                employee_free[office]=True
                # after returning, try start transfer if mails remain
                try_start_transfer(office,time)

        # output delivered mails sorted by delivery_time asc, then label asc
        outs=[]
        for i,mail in enumerate(mails):
            label=mail[3]
            outs.append((delivered[i],label))
        outs.sort(key=lambda x:(x[0],x[1]))
        for d,lbl in outs:
            print(f"{lbl} {d}")
        print()

if __name__=="__main__":
    main()