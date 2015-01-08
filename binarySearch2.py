def search(l, x):
	for i in range(len(l)):
		index = len(l)/2
		print len(l), index
		if x > l[index]:
			l = l[:index]
		elif x < l[index]:
			l = l[index:]
		else:
			return True
	return False

def main():
	number = 7
	l = [0,1,2,3,5,6,7,9]
	value = search(l, number)
	print number
	print value

main()