import os

print('task 1')

#x=3.251
#y=0.325

try:
	x = float(input('input x: '))
	y = float(input('input y: '))
	z = 0.466 * y * (10 * x ** (4))

except ValueError:
	print('You should input numbers!')

print (z)
os.system("pause")