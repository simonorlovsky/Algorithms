def search(l):
	index = len(l)/2
	for i in range(len(l)):
		print l[index]
		if (l[index-1] < l[index]) and (l[index] > l[index+1]):
			print "hello", l[index]
			return l[index]
		else:
			if l[index-1] > l[index]:
				l = l[:index]
				index = len(l)/2 
			else:
				l = l[index:]
				index = len(l)/2