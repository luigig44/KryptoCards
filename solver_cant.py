from fractions import Fraction as frac
from solver import oper

def solve_rec_cant(l, r):
	if(len(l) == 1):
		if(l[0][0] == r):
			return 1
		else:
			return 0
	res = 0
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			for t in range(6):
				try:
					op = oper(t,l[i],l[j])
				except:
					continue
				else:
					nl = [op]+l[:i]+l[i+1:j]+l[j+1:]
					s = solve_rec_cant(nl, r)
					res += s
	return res
	
def solve_cant(l, r):
	nl = l.copy()
	for i in range(len(nl)):
		nl[i]=(frac(nl[i]),str(nl[i]))
	return solve_rec_cant(nl,frac(r))
