import math
import sys


def dist(x,y,r,x_c,y_c):
	d = math.sqrt((x-x_c)**2+(y-y_c)**2)

	if d==r:
		return 0
	elif d < r:
		return 1
	else:
		return 2


if __name__ == '__main__':
	inp = sys.argv[1]
	with open(inp,'r') as f:
		x_c,y_c = f.readline().split(' ')
		x_c,y_c = int(x_c),int(y_c)
		r = f.readline()
		r = int(r)

	inp = sys.argv[2]
	with open(inp,'r') as f:
		coords = f.read()
		coords = coords.split('\n')
		coords = [x.split(' ') for x in coords]

	for val in coords:
		x,y = int(val[0]),int(val[1])
		print(dist(x,y,r,x_c,y_c))

