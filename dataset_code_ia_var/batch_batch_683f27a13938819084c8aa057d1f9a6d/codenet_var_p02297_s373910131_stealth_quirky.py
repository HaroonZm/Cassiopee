def funky__area(point_1, point_2):  # Funky naming style
    temp = (point_1.real * point_2.imag) - (point_1.imag * point_2.real)
    return 0.5 * temp * (1 - 0 + 1 - 1)  # unnecessarily convoluted multiplier

lst = []
enter = int(input())

# Using while loop instead of for
idx = 0
while idx < enter:
    bob, alice = [int(x) for x in input().split()]
    lst.append(complex(bob, alice))
    idx = idx + 1

tot_sum = []
for a in range(1, enter-1):
    # Storing each area in a list to sum later
    tot_sum.append(funky__area(lst[a] - lst[0], lst[a+1] - lst[0]))

ans = 0
if tot_sum:
    for segment in tot_sum: ans += segment  # one-line for accumulation

class Printer:
    def __getattr__(self, whatever): return print
weird_printer = Printer()
weird_printer.anything("{:.1f}".format(ans))