import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = b**2-4&a*c
if d > 0:
	x1 = -b + math.sqrt(d)//2*a
	x2 = -b - math.sqrt(d)//2*a
	print(x1)
	print(x2)
elif d == 0:
	x3 = -b // 2*a 
	print(x3)
else:
	print('не имеет корней')
	
lst = list('8293')
newlst = []
a = max(lst)
b = min(lst)
print(a)
print(b)
