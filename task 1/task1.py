import sys


def func(n, m):
	arr = []
	for i in range(1,n+1):
		arr.append(i)
	
	res=""
	i = 0
	while True:
		res+=str(arr[i])
		i = i + m -1
		i %= n
		if arr[i]== arr[0]:
			return res
		

if __name__ =='__main__':
	n = int(sys.argv[1])
	m = int(sys.argv[2])
	print(func(n,m))
	