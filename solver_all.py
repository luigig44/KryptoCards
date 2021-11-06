from fractions import Fraction as frac
from solver import oper

res = []

def solve_all_rec(l, r):
	if(len(l) == 1):
		if(l[0][0] == r):
			res.append(l[0][1])
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			for t in range(6):
				try:
					op = oper(t,l[i],l[j])
				except:
					continue
				else:
					nl = [op]+l[:i]+l[i+1:j]+l[j+1:]
					solve_all_rec(nl, r)
	
def solve_all(l, r):
	res.clear()
	nl = l.copy()
	for i in range(len(nl)):
		nl[i]=(frac(nl[i]),str(nl[i]))
	solve_all_rec(nl,frac(r))
	return res
