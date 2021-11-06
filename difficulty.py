from fractions import Fraction as frac
from solver_all import solve_all

def cont(s, c):
	res = 0
	for i in s:
		res += (i == c)
	return res

def esq(s):
	res = ""
	for i in s:
		if i in "+-*/()":
			res += i
	return res
	
def zero(s):
	if(esq(s) != "(((-)*)+)"):
		return 0
	res = ""
	va = 0
	for i in s:
		if(i == "("):
			va += 1
		if(i == ")"):
			va -= 1
		if(va == 3 and i != "("):
			res += i
	return res[0:len(res)//2] == res[len(res)//2+1:len(res)]

def difs(s):
	d = 0
	d += 10 * cont(s, "+")
	d += 5 * cont(s, "-")
	d += 5 * cont(s, "*")
	d += 15 * (cont(s, "+") + cont(s, "-") == 3)
	d += 25 * zero(s)
	return d

def diff(l, r):
	sol = solve_all(l, r)
	d = len(sol)
	solf = (0, "")
	for s in sol:
		solf = max(solf, (difs(s), s))
	d += solf[0]
	return (d, solf[1])
