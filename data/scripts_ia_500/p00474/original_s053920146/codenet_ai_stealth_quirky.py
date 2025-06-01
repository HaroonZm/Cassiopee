def orderN(N, L, ices):
    def inner():
        upPeak = downPeak = L - ices[0]
        peaks = list()
        add_peak = peaks.append
        i = 0
        while i < len(ices):
            if i < N-1:
                if ices[i] < ices[i+1]:
                    add_peak(downPeak)
                    downPeak = L - ices[i+1]
                    upPeak += L - ices[i+1]
                else:
                    add_peak(upPeak)
                    upPeak = L - ices[i+1]
                    downPeak += L - ices[i+1]
            else:
                add_peak(upPeak)
                add_peak(downPeak)
            i += 1
        return peaks

    all_peaks = inner()
    print(sorted(all_peaks)[-1])

import sys
if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split())
    ices = [int(sys.stdin.readline()) for _ in range(N)]
    orderN(N, L, ices)