#-------最強ライブラリString(Python)ver25252------
#全然わからん 翻訳しただけ

from functools import cmp_to_key
THRESHOLD_NAIVE = 10
THRESHOLD_DOUBLING = 40

# ナイーブな実装？
# O(n^2 log n かな？)
def sa_naive(s):
  def cmp(r, l):
    if l == r: return -1
    while (l < n and r < n):
      if s[l] != s[r]: return 1 if s[l] < s[r] else -1
      l += 1
      r += 1
    return 1 if l == n else -1
  n = len(s)
  sa = [i for i in range(n)]
  sa.sort(key=cmp_to_key(cmp))
  return sa

# わかんねー
# O(↑と↓の間くらい)
def sa_doubling(s):
  n = len(s)
  sa = [i for i in range(n)]
  rnk = s
  tmp = [0] * n
  k = 1
  while k < n:
    def cmp(y, x):
      if rnk[x] != rnk[y]: return 1 if rnk[x] < rnk[y] else -1
      rx = rnk[x + k] if x + k < n else -1
      ry = rnk[y + k] if y + k < n else -1
      return 1 if rx < ry else -1
    sa.sort(key=cmp_to_key(cmp))
    tmp[sa[0]] = 0
    for i in range(1, n):
      tmp[sa[i]] = tmp[sa[i - 1]] + (1 if cmp(sa[i], sa[i - 1]) == 1 else 0)
    tmp, rnk = rnk, tmp
    k *= 2
  return sa

# メインディッシュ
# O(n + upper のはず)
def sa_is(s, upper):
  n = len(s)
  if n == 0: return []
  if n == 1: return [0]
  if n == 2:
    if s[0] < s[1]: return [0, 1]
    else: return [1, 0]
  if n < THRESHOLD_NAIVE:
    return sa_naive(s)
  if n < THRESHOLD_DOUBLING:
    return sa_doubling(s)

  sa = [0] * n
  ls = [False] * n
  for i in range(n - 2, -1, -1):
    ls[i] = ls[i + 1] if s[i] == s[i + 1] else s[i] < s[i + 1]
  sum_l = [0] * (upper + 1)
  sum_s = [0] * (upper + 1)
  for i in range(n):
    if not ls[i]: sum_s[s[i]] += 1
    else: sum_l[s[i] + 1] += 1
  for i in range(upper + 1):
    sum_s[i] += sum_l[i]
    if i < upper: sum_l[i + 1] += sum_s[i]

  def induce(lms):
    for i in range(n): sa[i] = -1
    buf = [0] * (upper + 1)
    for i in range(len(sum_s)): buf[i] = sum_s[i]
    for d in lms:
      if d == n: continue
      sa[buf[s[d]]] = d
      buf[s[d]] += 1
    for i in range(len(sum_l)): buf[i] = sum_l[i]
    sa[buf[s[n - 1]]] = n - 1
    buf[s[n - 1]] += 1
    for i in range(n):
      v = sa[i]
      if v >= 1 and not ls[v - 1]:
        sa[buf[s[v - 1]]] = v - 1
        buf[s[v - 1]] += 1
    for i in range(len(sum_l)): buf[i] = sum_l[i]
    for i in range(n - 1, -1, -1):
      v = sa[i]
      if v >= 1 and ls[v - 1]:
       buf[s[v - 1] + 1] -= 1
       sa[buf[s[v - 1] + 1]] = v - 1

  # なげ～
  lms_map = [-1] * (n + 1)
  m = 0
  for i in range(1, n):
    if not ls[i - 1] and ls[i]:
      lms_map[i] = m
      m += 1
  lms = []
  for i in range(1, n):
    if not ls[i - 1] and ls[i]:
      lms.append(i)

  induce(lms)

  if m:
    sorted_lms = []
    for v in sa:
      if lms_map[v] != -1: sorted_lms.append(v)
    rec_s = [0] * m
    rec_upper = 0
    rec_s[lms_map[sorted_lms[0]]] = 0
    for i in range(1, m):
      l, r = sorted_lms[i - 1], sorted_lms[i]
      end_l = lms[lms_map[l] + 1] if lms_map[l] + 1 < m else n
      end_r = lms[lms_map[r] + 1] if lms_map[r] + 1 < m else n
      same = True
      if end_l - l != end_r - r:
        same = False
      else:
        while l < end_l:
          if s[l] != s[r]: break
          l += 1
          r += 1
        if l == n or s[l] != s[r]: same = False
      if not same: rec_upper += 1
      rec_s[lms_map[sorted_lms[i]]] = rec_upper

    rec_sa = sa_is(rec_s, rec_upper)

    for i in range(m):
      sorted_lms[i] = lms[rec_sa[i]]
    induce(sorted_lms)

  # つかれた
  return sa

# upper以下の配列の接尾辞配列
# O(n + upper だとうれしいな)
def suffix_array(s, upper):
  sa = sa_is(s, upper)
  return sa

# ull以下の配列の接尾辞配列
# O(n log n なのかな）
def suffix_array(s):
  if type(s) == str: return suffix_array_str(s)
  def cmp(r, l):
    return 1 if s[l] < s[r] else -1
  n = len(s)
  idx = [i for i in range(n)]
  idx.sort(key=cmp_to_key(cmp))
  s2 = [0] * n
  now = 0
  for i in range(n):
    if i and s[idx[i - 1]] != s[idx[i]]: now += 1
    s2[idx[i]] = now
  return sa_is(s2, now)

# 文字列の接尾辞配列
# O(n ってマジ？)
def suffix_array_str(s):
  n = len(s)
  s2 = list(map(ord, s))
  return sa_is(s2, 255)

# 最長共通接頭辞配列
# O(n)
def lcp_array(s, sa):
  # 文字列の場合はユニコ頑張ります
  if type(s) == str: s = list(map(ord, s))
  n = len(s)
  rnk = [0] * n
  for i in range(n):
    rnk[sa[i]] = i
  lcp = [0] * (n - 1)
  h = 0
  for i in range(n):
    if h > 0: h -= 1
    if rnk[i] == 0: continue
    j = sa[rnk[i] - 1]
    while j + h < n and i + h < n:
      if s[j + h] != s[i + h]: break
      h += 1
    lcp[rnk[i] - 1] = h
  return lcp

# zアルゴリズム
def z_algorithm(s):
  # 文字はうにこ
  if type(s) == str: s = list(map(ord, s))
  n = len(s)
  if n == 0: return []
  z = [0] * n
  j = 0
  for i in range(1, n):
    # ポインタわからん
    z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
    while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
    if j + z[j] < i + z[i]: j = i
  z[0] = n
  return z

#-------最強ライブラリここまで------

s = input()

sa = suffix_array(s)
ans = len(s) * (len(s) + 1) // 2
for x in lcp_array(s, sa):
  ans -= x

print(ans)