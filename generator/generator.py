from fractions import Fraction as frac
from solver import solve
from solver_cant import solve_cant
from difficulty import diff
from random import randint
import json
import webbrowser
import base64

def gen_kryptos(cant):
	l = []
	while(1):
		a = randint(1,5)
		b = randint(1,10)
		c = randint(1,15)
		d = randint(1,20)
		e = randint(1,25)
		l.append((solve_cant([a,b,c,d],e),([a,b,c,d],e)))
		if(l[-1][0]==0):
			l=l[:-1]
		if(len(l) == cant):
			break
	l.sort()
	return l

def gen_cant(rondas):
	l = gen_kryptos(20 * rondas)
	juego = []
	for i in range(rondas):
		juego.append(l[randint(20*i,20*(i+1)-1)])
	for i in juego[::-1]:
		print(i)
		
def gen_diff(rondas, valormagico=20):
	l = gen_kryptos(20 * rondas)
	for i in range(len(l)):
		d = diff(l[i][1][0], l[i][1][1])
		l[i] = d[0], l[i][1], d[1]
	l.sort()
	if valormagico <= 20:
		l = l[::-1]
		juego = []
		for i in range(rondas):
			juego.append(l[randint(valormagico*i,valormagico*(i+1)-1)])
		return juego
	elif valormagico <= 39:
		valormagico = 40 - valormagico
		juego = []
		for i in range(rondas):
			juego.append(l[randint(valormagico*i,valormagico*(i+1)-1)])
		return juego[::-1]
	else: return []
		
		
def gen_url(rondas, openbrowser=True, valormagico=20):
	results = gen_diff(rondas,valormagico)
	# url = 'https://luigig44.github.io/KryptoCards/?data='
	url = 'file:///home/luigi/KryptoCards/index.html?data='
	url += base64.b64encode(json.dumps(results).encode('ascii')).decode('ascii')
	print(url)
	if openbrowser:
		webbrowser.open(url)
			
