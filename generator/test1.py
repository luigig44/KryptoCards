from generator import gen_kryptos
from difficulty import diff, zero

l = gen_kryptos(100)

ra, rb = 0, 0

for i in range(len(l)):
	d = diff(l[i][1][0], l[i][1][1])
	if(zero(d[1])):
		ra += i
		print(i, d[1])
	l[i] = d[0], l[i][1]

l.sort()
		
for i in range(len(l)):
	d = diff(l[i][1][0], l[i][1][1])
	if(zero(d[1])):
		rb += i
		print(i, d[1])
		
print(ra, rb)
