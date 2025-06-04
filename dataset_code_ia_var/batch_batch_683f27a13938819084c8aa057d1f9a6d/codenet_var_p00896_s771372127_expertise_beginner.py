import string
import sys

def main():
    alphabet = string.ascii_uppercase

    def find_index(ch):
        return alphabet.find(ch)

    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break

        words = []
        for _ in range(N):
            line = sys.stdin.readline().strip()
            words.append(tuple([find_index(c) for c in line]))

        s_line = sys.stdin.readline().strip()
        s_line = s_line[:-1]
        query_words = s_line.split()
        S = []
        T = set()
        for w in query_words:
            tpl = tuple([find_index(x) for x in w])
            S.append(tpl)
            T.add(tpl)
        T = list(T)
        U = []
        for s in T:
            g = []
            for idx, w in enumerate(words):
                if len(w) != len(s):
                    continue
                mapping = [-1]*26
                l = len(w)
                for k in range(l):
                    if mapping[s[k]] == mapping[w[k]] == -1:
                        mapping[s[k]] = w[k]
                        mapping[w[k]] = s[k]
                    elif mapping[s[k]] == -1 or mapping[w[k]] == -1 or mapping[s[k]] != w[k]:
                        break
                else:
                    g.append(idx)
            U.append( (s, g) )
        # sort to optimize DFS
        U.sort(key=lambda x: len(x[1]))
        L = len(U)
        res = None
        cnt = 0

        def dfs(i, curr_mapping, used):
            nonlocal res
            nonlocal cnt
            if i == L:
                res = curr_mapping[:]
                cnt += 1
                return
            s, g_list = U[i]
            for j in g_list:
                if used[j]:
                    continue
                w = words[j]
                temp_mapping = curr_mapping[:]
                l = len(w)
                for k in range(l):
                    if temp_mapping[s[k]] == temp_mapping[w[k]] == -1:
                        temp_mapping[s[k]] = w[k]
                        temp_mapping[w[k]] = s[k]
                    elif temp_mapping[s[k]] == -1 or temp_mapping[w[k]] == -1 or temp_mapping[s[k]] != w[k]:
                        break
                else:
                    used[j] = 1
                    dfs(i+1, temp_mapping, used)
                    used[j] = 0
                if cnt >= 2:
                    return
        dfs(0, [-1]*26, [0]*N)

        if cnt != 1:
            sys.stdout.write("-.\n")
        else:
            cA = ord('A')
            ans = []
            for s in S:
                t = []
                for e in s:
                    t.append(chr(res[e] + cA))
                ans.append("".join(t))
            sys.stdout.write(" ".join(ans))
            sys.stdout.write(".\n")

main()