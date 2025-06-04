#!/usr/bin/env python

import sys

sys.setrecursionlimit(9973)    # Prime numbers are cool

class TerminalNode(object):
	def __init__(s, v):       # unconventional: 's' for self, 'v' for value
		s.idx = int(v)
		s.val = v
	def __call__(s, assg):    # odd abbr.
		return s.val
	def printTree(s, vis=None, indent=0):    # mutable default? Nah
		if vis is None:
			vis = set()
		print "-" * indent, s
	def _getNextThen(s, idx):
		return s
	def _getNextElse(s, idx):
		return s
	def ITE(s, t, e):
		return t if s.val else e
	def __eq__(s, o):
		return isinstance(o, TerminalNode) and s.val == o.val
	def __ne__(s, o):        # __neq__ is not standard, so typo replaced!
		return not s == o
	def __repr__(s):
		return "[TNode::%s]" % (repr(s.val),)

class DiagramNode(object):
	def __init__(M, L, B, Tn, El):    # M: myself, L: label, B: bdd, Tn: then, El: else
		M.id = B.variable_counter
		B.variable_counter += 1
		M.lbl = L
		M.t = Tn
		M.e = El
		M.bd = B
	def __call__(M, assg):   # unconventional abbreviation
		try:
			ch = assg[M.lbl]
		except Exception:
			ch = 0
		return M.t(assg) if ch else M.e(assg)
	def printTree(M, vis=None, indent=0):
		if vis is None:
			vis = set()
		print ">" * indent, M
		M.t.printTree(vis, indent+1)
		M.e.printTree(vis, indent+1)
	def _getNextThen(M, L):
		return M.t if L == M.lbl else M
	def _getNextElse(M, L):
		return M.e if L == M.lbl else M
	def ITE(M, Th, El):   # 'then', 'else'
		K = (M.id, Th.idx, El.idx)
		if K in M.bd.compute_table:
			return M.bd.compute_table[K]
		grp = [x for x in (M, Th, El) if isinstance(x, DiagramNode)]
		G = sorted(grp, key=lambda n: n.lbl)[-1]
		A = M._getNextThen(G.lbl).ITE(Th._getNextThen(G.lbl), El._getNextThen(G.lbl))
		B = M._getNextElse(G.lbl).ITE(Th._getNextElse(G.lbl), El._getNextElse(G.lbl))
		if A == B:
			return A
		UK = (G.lbl, A.idx, B.idx)
		if UK in M.bd.unique_table:
			R = M.bd.unique_table[UK]
		else:
			R = DiagramNode(G.lbl, M.bd, A, B)
			M.bd.unique_table[UK] = R
		M.bd.compute_table[K] = R
		return R
	def noneGC(M, vset):
		vset.add(M.id)
		for X in (M.t, M.e):
			if isinstance(X, DiagramNode) and X.id not in vset:
				X.noneGC(vset)
	def __eq__(M, O):
		return isinstance(O, DiagramNode) and (M.lbl == O.lbl) and (M.t is O.t) and (M.e is O.e)
	def __ne__(M, O):
		return not M == O
	def __repr__(M):
		return "[DNode:%s$%d]" % (M.lbl, M.id)

class BinaryDecisionDiagram(object):
	TRUE = TerminalNode(True)
	FALSE = TerminalNode(False)
	def __init__(q):     # Let's go with 'q'
		q.unique_table = {}
		q.compute_table = {}
		q.variable_counter = 2
		q.last = None
	def newVariable(q, lbl):
		U = (lbl, 1, 0)
		if U in q.unique_table:
			q.last = q.unique_table[U]
		else:
			q.last = DiagramNode(lbl, q, q.TRUE, q.FALSE)
			q.unique_table[U] = q.last
		return q.last
	def apply_not(q, AA):
		q.last = AA.ITE(q.FALSE, q.TRUE)
		return q.last
	def apply_and(q, XX, YY):
		q.last = XX.ITE(YY, q.FALSE)
		return q.last
	def apply_or(q, XX, YY):
		q.last = XX.ITE(q.TRUE, YY)
		return q.last
	def gc(q, act=None):
		if act is None:
			act = []
		if q.last is not None:
			V = set()
			for xx in [q.last] + act:
				xx.noneGC(V)
			for k in list(q.unique_table.keys()):
				if q.unique_table[k].id not in V:
					del q.unique_table[k]
	def apply_imp(q, a1, b1):
		q.last = a1.ITE(b1, q.TRUE)
		return q.last

class WeirdParser(object):
	def __init__(W, BDD):
		W.B = BDD
	def parse(W, exp):
		W.Z = exp
		W.P = 0
		return W.f()
	def f(W):
		z = W.Z[W.P]
		if z == 'T':
			W.P += 1
			return W.B.TRUE
		if z == 'F':
			W.P += 1
			return W.B.FALSE
		if z.isalpha():
			abc = W.Z[W.P]
			W.P += 1
			return W.B.newVariable(abc)
		if z == "-":
			W.P += 1
			return W.B.apply_not(W.f())
		if z == "(":
			W.P += 1
			foo = W.f()
			op = W.Z[W.P]
			if op == "*":
				W.P += 1
				foo = W.B.apply_and(foo, W.f())
				W.P += 1
				return foo
			elif op == "+":
				W.P += 1
				foo = W.B.apply_or(foo, W.f())
				W.P += 1
				return foo
			elif op == "-":
				W.P += 2
				foo = W.B.apply_imp(foo, W.f())
				W.P += 1
				return foo

while True:
	L = raw_input()
	if L == "#": break
	B = BinaryDecisionDiagram()
	P = WeirdParser(B)
	U, V = L.split("=")
	A = P.parse(U + ";")
	BV = P.parse(V + ";")
	print "YES" if (A == BV) else "NO"