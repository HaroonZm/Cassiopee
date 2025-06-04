import sys
import bisect

input = sys.stdin.readline

MAX_SECTOR = 10**9

class FileSystem:
    def __init__(self):
        # free_intervals: list of (start, end) sorted by start; end inclusive
        self.free_intervals = [(0, MAX_SECTOR)]
        # file_map: file_id -> list of (start,end) intervals occupied by that file
        self.file_map = {}
        # occupied_intervals: list of (start, end, file_id) sorted by start, disjoint intervals
        self.occupied = []

    def _add_free(self, start, end):
        # Add free interval [start,end], merge with neighbors if possible
        fi = self.free_intervals
        pos = bisect.bisect_left(fi, (start, end))
        # Try merge left
        left = pos - 1
        right = pos
        new_start, new_end = start, end
        to_del = []
        if left >= 0 and fi[left][1] + 1 >= start:
            new_start = fi[left][0]
            new_end = max(fi[left][1], end)
            to_del.append(left)
        if right < len(fi) and fi[right][0] -1 <= end:
            new_start = min(new_start, fi[right][0])
            new_end = max(new_end, fi[right][1])
            to_del.append(right)
        # Remove merged intervals
        for i in reversed(to_del):
            fi.pop(i)
        bisect.insort(fi, (new_start, new_end))

    def _remove_free(self, start, end):
        # Remove the interval [start,end] from free_intervals
        fi = self.free_intervals
        pos = bisect.bisect_left(fi, (start, -1))
        # maybe interval before pos overlap
        if pos >0:
            pos -= 1
        updates = []
        while pos < len(fi):
            fstart, fend = fi[pos]
            if fstart > end:
                break
            # overlapping with [start,end]
            if fend < start:
                pos += 1
                continue
            # Cut out [start,end]
            # Cases:
            # 1) fstart < start <= fend < end: shrink to fstart,start-1
            # 2) start <= fstart <= end < fend: shrink to end+1,fend
            # 3) fstart < start and fend > end: split into two intervals
            # 4) full covered: remove interval
            to_remove = fi.pop(pos)
            if to_remove[0] < start:
                updates.append((to_remove[0], start-1))
            if to_remove[1] > end:
                updates.append((end+1, to_remove[1]))
        for u in updates:
            bisect.insort(fi, u)

    def _occupied_add(self, start, end, fid):
        # Insert occupied interval in self.occupied, keep sorted and disjoint
        oi = self.occupied
        bisect.insort(oi, (start, end, fid))

    def _occupied_remove_file(self, fid):
        # Remove all intervals occupied by fid from self.occupied
        oi = self.occupied
        new_oi = [iv for iv in oi if iv[2] != fid]
        self.occupied = new_oi

    def _occupied_find(self, sector):
        oi = self.occupied
        pos = bisect.bisect_right(oi, (sector, MAX_SECTOR+1, 10**10))
        if pos == 0:
            return -1
        interval = oi[pos-1]
        if interval[0] <= sector <= interval[1]:
            return interval[2]
        return -1

    def write(self, fid, size):
        # We write file of size sectors with id fid
        # Find earliest free space(s) from start for writing
        # If meet occupied sector during writing, skip occupied part and continue at next free segment
        remaining = size
        intervals = []
        fi = self.free_intervals
        # We scan free intervals from the beginning until total size is covered
        idx = 0
        while remaining > 0 and idx < len(fi):
            start, end = fi[idx]
            length = end - start +1
            if length <= 0:
                idx += 1
                continue
            take = min(remaining, length)
            block_start = start
            block_end = start + take -1
            intervals.append((block_start, block_end))
            remaining -= take
            if take == length:
                # full free interval used: remove it later
                idx += 1
            else:
                # partial use: update free interval
                fi[idx] = (start+take, end)
                break
        if remaining >0:
            # not enough free space, problem states nothing about this case; just write partial
            pass
        # Remove these intervals from free_intervals
        for s,e in intervals:
            self._remove_free(s,e)
        # Add intervals to occupied_intervals
        for s,e in intervals:
            self._occupied_add(s,e,fid)
        self.file_map[fid] = intervals

    def delete(self, fid):
        if fid not in self.file_map:
            return
        intervals = self.file_map[fid]
        # Remove from occupied_intervals
        self._occupied_remove_file(fid)
        # Add back to free intervals and merge automatically
        for s,e in intervals:
            self._add_free(s,e)
        del self.file_map[fid]

    def read(self, sector):
        return self._occupied_find(sector)

def main():
    while True:
        line = input()
        if not line:
            break
        N = int(line)
        if N == 0:
            break
        fs = FileSystem()
        for _ in range(N):
            cmd_line = input().strip()
            if not cmd_line:
                continue
            parts = cmd_line.split()
            cmd = parts[0]
            if cmd == 'W':
                fid = int(parts[1])
                size = int(parts[2])
                fs.write(fid,size)
            elif cmd == 'D':
                fid = int(parts[1])
                fs.delete(fid)
            elif cmd == 'R':
                sector = int(parts[1])
                print(fs.read(sector))
        print()

if __name__ == '__main__':
    main()