import sys
import bisect

input = sys.stdin.readline

class Member:
    __slots__ = ('name','motivation','order')
    def __init__(self,name,motivation,order):
        self.name = name
        self.motivation = motivation
        self.order = order
    def key(self):
        # Sort by motivation desc, order desc
        return (-self.motivation, -self.order)

def work_num(size):
    return size*20//100

def insert_member(st, member):
    k = member.key()
    pos = bisect.bisect_left(st, k)
    st.insert(pos, k)
    return pos

def remove_member(st, member):
    k = member.key()
    pos = bisect.bisect_left(st, k)
    # pos must be the element
    st.pop(pos)
    return pos

N = int(input())
members = {}
order_seq = 0

# Data structures to keep keys of members in order
# workhorses contain the top 20%, idle fellows the rest
workhorses = []
idles = []

# name_to_member for quick access
for _ in range(N):
    s,a = input().split()
    a = int(a)
    members[s] = Member(s,a,order_seq)
    order_seq += 1

def build_sets():
    # Build a list of all members ordered by key
    all_members = list(members.values())
    all_members.sort(key=lambda m:(-m.motivation, -m.order))
    cut = work_num(len(all_members))
    workhorses.clear()
    idles.clear()
    for i,m in enumerate(all_members):
        if i < cut:
            workhorses.append(m.key())
        else:
            idles.append(m.key())

build_sets()

M = int(input())

for _ in range(M):
    line = input().split()
    if line[0] == '+':
        # member join
        name = line[1]
        a = int(line[2])
        m = Member(name,a,order_seq)
        order_seq += 1
        members[name] = m

        # update sets
        # Insert into idles first
        # Compare with best in idles vs worst in workhorses and swap if needed
        # If work_num changes, fix sets accordingly

        # Update cutoff
        size = len(workhorses)+len(idles)+1
        new_cut = work_num(size)

        # Insert into idles tentatively
        # idles keys stored sorted
        bisect.insort_left(idles,m.key())

        # If new_cut > old cut, a member will move to workhorses
        # Need to fix for increase in workhorses

        if new_cut > len(workhorses):
            # Move best from idles to workhorses
            best_idle = idles.pop(0)
            bisect.insort_left(workhorses,best_idle)
        elif new_cut < len(workhorses):
            # Move worst from workhorses to idles
            worst_work = workhorses.pop()
            bisect.insort_left(idles,worst_work)
        # else same size sets

        # Now check if m is in workhorses
        # m.key() in idles or workhorses?
        # If m.key() in workhorses: print work
        # else print not working
        # If a member changed sets, print that change accordingly

        # Find m.key() in sets
        # We added m.key() to idles (or moved between sets)
        # Check if m.key() in workhorses
        # each time a single member moves
        # So total max two changes, but problem states only one change of workstyle ever per event

        # print join message of m
        if m.key() in workhorses:
            print(f"{m.name} is working hard now.")
        else:
            print(f"{m.name} is not working now.")

        # After join, one possible swap between sets may happen, but we have balanced sizes above
        # Check if a member changed group (except m)

        # The only possible swap is the member we moved from idles to workhorses or vice versa in size balancing

        # If new_cut changed (mostly by 1), a member changed sets before insertion of m in sets

        # but we did one move max:

        # The member swapped is the one moved to keep sizes correct

        # But if new_cut == old cut, no swap, no change except m joined

        old_size = len(workhorses)+len(idles)-1
        old_cut = work_num(old_size)
        changed = False
        if new_cut > old_cut:
            # member moved from idles to workhorses: best_idle
            # but best_idle may be m
            if best_idle != m.key():
                # find member name of best_idle
                # key = (-motivation, -order)
                mo,ordr = best_idle
                # find member by reverse
                for mm in members.values():
                    if mm.key() == best_idle:
                        print(f"{mm.name} is working hard now.")
                        break
                # Also member moved out from workhorses?
                # No: only one member moved here from idles to workhorses
            changed = True
        elif new_cut < old_cut:
            # member moved from workhorses to idles: worst_work
            if worst_work != m.key():
                for mm in members.values():
                    if mm.key() == worst_work:
                        print(f"{mm.name} is not working now.")
                        break
            changed = True

    else:
        # member leave
        name = line[1]
        if name not in members:
            # Already left, ignore
            continue
        m = members.pop(name)
        # remove from sets
        size = len(workhorses)+len(idles)
        old_cut = work_num(size)
        # Remove from where?
        # search for m.key() in workhorses or idles
        key = m.key()
        pos = bisect.bisect_left(workhorses,key)
        if pos<len(workhorses) and workhorses[pos]==key:
            workhorses.pop(pos)
            removed_from_workhorses = True
        else:
            pos = bisect.bisect_left(idles,key)
            idles.pop(pos)
            removed_from_workhorses = False

        size -= 1
        new_cut = work_num(size)

        # balancing sets sizes according to new_cut
        if new_cut > len(workhorses):
            # Move best from idles to workhorses
            if idles:
                best_idle = idles.pop(0)
                bisect.insort_left(workhorses,best_idle)
            else:
                best_idle = None
        elif new_cut < len(workhorses):
            # move worst from workhorses to idles
            worst_work = workhorses.pop()
            bisect.insort_left(idles,worst_work)
        else:
            best_idle = None
            worst_work = None

        # print changes of sets
        # For leaving member no message
        # Check if a member changed group due to balancing
        # If best_idle is not None and best_idle != removed m
        # member moved to workhorses: print working hard
        if new_cut > old_cut and best_idle is not None:
            for mm in members.values():
                if mm.key() == best_idle:
                    print(f"{mm.name} is working hard now.")
                    break
        elif new_cut < old_cut and worst_work is not None:
            for mm in members.values():
                if mm.key() == worst_work:
                    print(f"{mm.name} is not working now.")
                    break