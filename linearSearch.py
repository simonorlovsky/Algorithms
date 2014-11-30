def search(l, x):
	for i in range(len(l)):
		if l[i]==x:
			return i
	return "not found"

def main():
	number = 5
	l = [0,1,3,4,2,4,2]
	value = search(l, number)
	print number
	print value

main()