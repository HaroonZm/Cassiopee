import sys
import threading
from bisect import bisect_left,bisect_right
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
threading.stack_size(2**27)

class Fenwick2D:
    def __init__(self,h,w):
        self.h=h
        self.w=w
        self.data=[[0]*(w+1) for _ in range(h+1)]
    def _add(self,x,y,v):
        i=x
        while i<=self.h:
            j=y
            while j<=self.w:
                self.data[i][j]+=v
                j+=j&(-j)
            i+=i&(-i)
    def add(self,x,y,v=1):
        # x,y are 1-based indexes
        self._add(x,y,v)
    def _sum(self,x,y):
        # sum of rectangle (1,1,x,y)
        s=0
        i=x
        while i>0:
            j=y
            while j>0:
                s+=self.data[i][j]
                j-=j&(-j)
            i-=i&(-i)
        return s
    def query(self,x1,y1,x2,y2):
        # sum of rectangle (x1,y1)-(x2,y2), inclusive, 1-based
        if x2<x1 or y2<y1:
            return 0
        return self._sum(x2,y2)-self._sum(x1-1,y2)-self._sum(x2,y1-1)+self._sum(x1-1,y1-1)

class TaiyakiStatus:
    # Status codes for clarity of future expansion
    EMPTY=0
    UNBAKED=1
    BAKED=2

class TaiyakiManager:
    def __init__(self,H,W,T):
        self.H=H
        self.W=W
        self.T=T
        # Board status for each cell (1-based indexing)
        # store 0: empty, 1: unbaked, 2: baked
        self.board=[[TaiyakiStatus.EMPTY]*(W+1) for _ in range(H+1)]
        # Fenwicks for baked and unbaked counts
        self.fenw_baked=Fenwick2D(H,W)
        self.fenw_unbaked=Fenwick2D(H,W)
        # To track baking completion events (t+T, h,w)
        # We'll rely on event chronological order to process baking completions
        self.bake_finish_events=[]
        self.filled_positions=set()
    def set_taiyaki(self,h,w,t):
        # Set Taiyaki at (h,w) at time t if empty
        # Insert as unbaked and schedule baking completion at t+T
        if (h,w) in self.filled_positions:
            return False
        self.filled_positions.add((h,w))
        self.board[h][w]=TaiyakiStatus.UNBAKED
        self.fenw_unbaked.add(h,w,1)
        # Insert bake finish event
        self.bake_finish_events.append((t+self.T,h,w))
        return True
    def eat_taiyaki(self,h,w):
        # Eat baked taiyaki if present
        if self.board[h][w]!=TaiyakiStatus.BAKED:
            return False
        self.board[h][w]=TaiyakiStatus.EMPTY
        self.fenw_baked.add(h,w,-1)
        self.filled_positions.remove((h,w))
        return True
    def count_taiyaki(self,h1,w1,h2,w2):
        # Count baked and unbaked taiyaki in the rectangle
        count_baked=self.fenw_baked.query(h1,w1,h2,w2)
        count_unbaked=self.fenw_unbaked.query(h1,w1,h2,w2)
        return (count_baked,count_unbaked)
    def process_bake_finish(self,current_t):
        # Process all baking finishes scheduled on or before current_t
        # As events are sorted chronologically, we can pop from front
        while self.bake_finish_events and self.bake_finish_events[0][0]<=current_t:
            _,h,w=self.bake_finish_events.pop(0)
            # For safety, check
            if self.board[h][w]==TaiyakiStatus.UNBAKED:
                # Change status unbaked->baked
                self.board[h][w]=TaiyakiStatus.BAKED
                self.fenw_unbaked.add(h,w,-1)
                self.fenw_baked.add(h,w,1)

class EventProcessor:
    def __init__(self,H,W,T,Q,raw_events):
        self.H=H
        self.W=W
        self.T=T
        self.Q=Q
        self.events=raw_events
        self.tm=TaiyakiManager(H,W,T)
        # bake finish events per time for organized baking processing
        self.bake_events=[]
        # outputs for c=2 queries
        self.outputs=[]
    def organize_bake_events(self):
        # Sort baking finish events by time
        self.tm.bake_finish_events.sort(key=lambda x:x[0])
    def process_all(self):
        # Sort baking finish events now? Done on insert anyway at end
        # We alternatively can be sure events sorted by input t_i
        # We will merge baking finish events into event stream
        # But given how we wrote - baking_finish_events not appended during event reading
        # So we can rely on sorting them before main loop
        self.org_bake_events()
        # For efficiency, we process events in chronological order by t_i
        # Gather all baking finish events t_bake and input events t_i in a time ordered queue
        # Instead, we process input events in order, then process baking events when t_i grows
        # We'll maintain a pointer for baking events
        bake_idx=0
        bake_events=self.tm.bake_finish_events
        # For efficient insertion and removal, convert to list sorted by time
        # But as baking events added dynamically during processing, we will go iteratively
        # We'll integrate baking events on the fly
        # Let's recreate tm.bake_finish_events as a heap or sorted list for efficient process_bake_finish
        # We refactor bake_finish_events into a list and use pointer for baking event handling
        # We'll store baking events into an internal list and pointer
        bake_events=bake_events.copy()
        bake_events.sort(key=lambda x:x[0])
        bake_len=len(bake_events)
        bake_ptr=0
        for ev in self.events:
            t=ev['t']
            # process all baking finishes up to time t
            while bake_ptr<bake_len and bake_events[bake_ptr][0]<=t:
                _,h,w=bake_events[bake_ptr]
                if self.tm.board[h][w]==TaiyakiStatus.UNBAKED:
                    self.tm.board[h][w]=TaiyakiStatus.BAKED
                    self.tm.fenw_unbaked.add(h,w,-1)
                    self.tm.fenw_baked.add(h,w,1)
                bake_ptr+=1
            c=ev['c']
            if c==0:
                # Set event
                h,w=ev['h1'],ev['w1']
                # set taiyaki and add its bake finish event into bake_events in sorted order
                if (h,w) not in self.tm.filled_positions:
                    self.tm.filled_positions.add((h,w))
                    self.tm.board[h][w]=TaiyakiStatus.UNBAKED
                    self.tm.fenw_unbaked.add(h,w,1)
                    # Insert bake finish event in sorted order by time (t+T)
                    bake_time=t+self.T
                    # binary insert to keep bake_events sorted to allow bake_ptr optimization
                    idx=bisect_right(bake_events,bake_time,key=lambda x:x[0])
                    bake_events.insert(idx,(bake_time,h,w))
                    bake_len+=1
                    # if inserted before bake_ptr, have to fix bake_ptr
                    if idx<=bake_ptr:
                        bake_ptr+=1
            elif c==1:
                # Eat event
                h,w=ev['h1'],ev['w1']
                if self.tm.board[h][w]==TaiyakiStatus.BAKED:
                    self.tm.board[h][w]=TaiyakiStatus.EMPTY
                    self.tm.fenw_baked.add(h,w,-1)
                    self.tm.filled_positions.remove((h,w))
            else:
                # Count event
                h1,w1,h2,w2=ev['h1'],ev['w1'],ev['h2'],ev['w2']
                baked,unbaked=self.tm.count_taiyaki(h1,w1,h2,w2)
                self.outputs.append((baked,unbaked))
        # process the remained baking finish events after last event time if any ?
        # Problem states no events after last t_i so no pending count requested so skips
    def org_bake_events(self):
        # Sort initial baking finish events (normally empty at initialization)
        self.tm.bake_finish_events.sort(key=lambda x:x[0])
    def print_outputs(self):
        print('\n'.join(f"{a} {b}" for a,b in self.outputs))

def parse_input():
    H,W,T,Q=map(int,input().split())
    events=[]
    for _ in range(Q):
        parts=input().split()
        t=int(parts[0])
        c=int(parts[1])
        if c==2:
            h1,w1,h2,w2=map(int,parts[2:6])
            events.append({'t':t,'c':c,'h1':h1,'w1':w1,'h2':h2,'w2':w2})
        else:
            h1,w1=map(int,parts[2:4])
            events.append({'t':t,'c':c,'h1':h1,'w1':w1})
    return H,W,T,Q,events

def main():
    H,W,T,Q,events=parse_input()
    ep=EventProcessor(H,W,T,Q,events)
    ep.process_all()
    ep.print_outputs()

if __name__=="__main__":
    threading.Thread(target=main).start()