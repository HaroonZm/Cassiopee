import sys
import threading
def main():
    sys.setrecursionlimit(10**7)
    input=sys.stdin.readline
    while True:
        N=int(input())
        if N==0:
            break
        # parse marks
        jump_marks=[None]*N  # (type:str, number:int) or None
        has_v=[False]*N
        for i in range(N):
            s=input().strip()
            if s=='-':
                continue
            if 'v' in s:
                has_v[i]=True
                s=s.replace('v','')
            if s=='':
                continue
            # jump mark present
            # separate type and number
            # type: a-z letters, number: digits at end
            j=0
            while j<len(s) and s[j].isalpha():
                j+=1
            t=s[:j]
            n=int(s[j:])
            jump_marks[i]=(t,n)
        # precompute:
        # For each jump mark type, number, store list of indices in ascending order
        jm_pos = dict()  # (type,number) -> sorted list of indices
        for i,(t,n) in enumerate(jump_marks):
            if t is None:
                continue
            if (t,n) not in jm_pos:
                jm_pos[(t,n)] = []
            jm_pos[(t,n)].append(i)
        # store for jump mark type t the index of most recently read letter with (t,1)
        last_read_type = dict()
        read = [False]*N
        order = []

        # we start reading with the first letter if it is not skipped by rule 2 (jump mark with number>=2)
        # but the problem's rule 1 says first letter is read first anyway, but rule 2 says if jump mark number>=2 skip
        # so we try first letter, but if jump mark number >=2 skip it and move on
        # but precise reading from rules: first letter should be read or skipped first, i.e. start from 0 index
        i = 0
        # Use function to get next letter index without reading it
        def next_linear(k):
            # k is the index of last read letter with number 1 or previous letter in normal reading order ? see rules
            # rule 3 says: If no such letter L (jump mark t,n+1) . the (k+1)-th letter is read,
            # where k is the index of most recent read letter with jump mark t,1
            # So linear reading is from 0 upwards skipping read, so next <= N-1
            n = k+1
            while n < N and read[n]:
                n += 1
            if n >= N:
                return -1
            return n
        def find_unread_pos(lst):
            # lst sorted ascending letter indices
            # find unread letter with minimal index in lst
            # binary search to find first unread
            left,right=0,len(lst)
            while left<right:
                mid=(left+right)//2
                if read[lst[mid]]:
                    left=mid+1
                else:
                    right=mid
            if left==len(lst):
                return -1
            return lst[left]

        # According to rules priority:
        # 1) if the i-th letter read has jump mark (t,n), n>=2 skip it.
        # 2) when reading i-th letter with (t,n), if exists unread letter with (t,n+1) at pos < i, read it next
        #    else read (k+1)-th letter where k is last read letter with (t,1)
        # 3) letter with 'v' must be skipped
        # 4) if i-th read letter's previous letter (i-1) has 'v', read i-1-th letter next
        # 5) read next letter in linear order default
        # Multiple rules applicable: apply latter in the list first.
        # So rule 4 first, then 3,2,1

        # We'll proceed stepwise:
        current = None
        # find first letter that can be read (start at 0)
        # because first letter may be skipped (number>=2 or v)
        # so implement loop until find first readable letter
        pos = 0
        while pos<N and (read[pos] or has_v[pos] or (jump_marks[pos] is not None and jump_marks[pos][1]>=2)):
            pos+=1
        if pos==N:
            # no letter can be read? problem states input well formed and all letters read, so this doesn't happen
            continue
        current = pos
        while current!=-1:
            order.append(current)
            read[current]=True
            # update last_read_type
            jm = jump_marks[current]
            if jm is not None and jm[1]==1:
                last_read_type[jm[0]]=current
            # find the next letter to read
            nxt=-1
            # Rule 4: if current>0 and previous letter has 'v' and not read, read it next
            if current>0 and has_v[current-1] and not read[current-1]:
                nxt=current-1
            # else Rule3 &2 &1 combined:
            # if current letter has jump mark (t,n), n>=1
            if nxt==-1 and jm is not None:
                t,n=jm
                if n>=2:
                    # letter with jump mark number >=2 must be skipped (already skipped before reading)
                    # no action needed, but if read, nothing special said; already skipped before reading
                    pass
                else:
                    # n=1
                    # Rule2: if exists unread letter with (t,n+1) at pos < current, read it next
                    lst = jm_pos.get((t,n+1),[])
                    ch = -1
                    if lst:
                        # find unread position < current in lst
                        # lst is sorted ascending
                        # find max index in lst less than current and unread
                        # binary search with upper_bound for current
                        # then scan backward since must be pos < current and unread
                        import bisect
                        idx = bisect.bisect_left(lst,current)
                        # scan left from idx-1 down to 0
                        for p in range(idx-1,-1,-1):
                            if not read[lst[p]]:
                                ch = lst[p]
                                break
                    if ch!=-1:
                        nxt = ch
                    else:
                        # else read (k+1)-th letter where k = last read letter with (t,1)
                        k = last_read_type.get(t,-1)
                        candidate = next_linear(k)
                        if candidate!=-1 and not read[candidate]:
                            nxt = candidate
            # if no jump mark or no next found by jump mark:
            if nxt==-1:
                # Rule1 and 3 and 4 not triggered, so read next letter in linear order
                nxt = next_linear(current)
            current = nxt
        for o in order:
            print(o+1)
threading.Thread(target=main).start()