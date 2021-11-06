from fractions import Fraction as frac
from solver import oper

res = set()

def solve_list_rec(l):
	if(len(l) == 1 and l[0][0] not in res):
		res.add(l[0][0])
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			for t in range(6):
				try:
					op = oper(t,l[i],l[j])
				except:
					continue
				else:
					nl = [op]+l[:i]+l[i+1:j]+l[j+1:]
					solve_list_rec(nl)
	
def solve_list(l):
	res.clear()
	nl = l.copy()
	for i in range(len(nl)):
		nl[i]=(frac(nl[i]),str(nl[i]))
	solve_list_rec(nl)
	ls = list(res)
	ls.sort()
	return ls
