from fractions import Fraction as frac

def oper(t,a,b):
	if(t == 0):
		return (a[0] + b[0], "(" + a[1] + "+" + b[1] + ")")
	elif(t == 1):
		return (a[0] - b[0], "(" + a[1] + "-" + b[1] + ")")
	elif(t == 2):
		return (b[0] - a[0], "(" + b[1] + "-" + a[1] + ")")
	elif(t == 3):
		return (a[0] * b[0], "(" + a[1] + "*" + b[1] + ")")
	elif(t == 4):
		return (a[0] / b[0], "(" + a[1] + "/" + b[1] + ")")
	elif(t == 5):
		return (b[0] / a[0], "(" + b[1] + "/" + a[1] + ")")
		
def solve_rec(l, r):
	if(len(l) == 1):
		if(l[0][0] == r):
			return l[0][1]
		else:
			return "IMPOSIBLE"
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			for t in range(6):
				try:
					op = oper(t,l[i],l[j])
				except:
					continue
				else:
					nl = [op]+l[:i]+l[i+1:j]+l[j+1:]
					s = solve_rec(nl, r)
					if(s != "IMPOSIBLE"):
						return s
	return "IMPOSIBLE"
	
def solve(l, r):
	nl = l.copy()
	for i in range(len(nl)):
		nl[i]=(frac(nl[i]),str(nl[i]))
	return solve_rec(nl,frac(r))
