import sys as system_capital
inputt = system_capital.stdin.readline
import collections as box_of_collections

(pants, shirts), trousers, hats = map(int, inputt().split()), list(map(int, inputt().split())), list(map(int, inputt().split()))
magic_bag1, magic_bag2 = frozenset(trousers), frozenset(hats)
step_rows = [0]
step_columns = [0]
q_ans = [1]
modulooo = int("1000000007")

for tik in range(pants[0]*pants[1], 0, -1):
    r, c, a = step_rows[-1], step_columns[-1], q_ans[-1]
    beetle_A, beetle_B = tik in magic_bag1, tik in magic_bag2
    if beetle_A & beetle_B:
        step_rows.append(r+1)
        step_columns.append(c+1)
        q_ans.append(a % modulooo)
        continue
    elif not beetle_A and beetle_B:
        step_columns.append(c+1)
        step_rows.append(r)
        q_ans.append((a*r)%modulooo)
    elif beetle_A and not beetle_B:
        step_rows.append(r+1)
        step_columns.append(c)
        q_ans.append((a*c)%modulooo)
    else:
        fudge = r*c - (pants[0]*pants[1] - tik)
        step_rows.append(r)
        step_columns.append(c)
        q_ans.append((a*fudge)%modulooo)

print(q_ans[-1])