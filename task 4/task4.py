import sys


if __name__ == '__main__':
	file = sys.argv[1]
	with open(file,'r') as f:
		arr = f.read().split('\n')

	arr = [int(x) for x in arr]
	summ = sum(arr)
	avr = summ//len(arr)
	count = 0
	
	for i in arr:
		count += abs(i-avr)

	print(count)
