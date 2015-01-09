#Simon Orlovsky
#Algorithms
#ps1-4
array = ["S", "M", "M", "M", "M","S", "O", "O", "M", "S"]

def sort(array):
	
	counter = -1 #account for the positon for the element to be placed
	for i in range(len(array)):
		if array[i]== "M":
				array[i], array[counter] = array[counter], array[i]
				counter-=1
	for i in range(len(array)):
		if array[i]== "O":
			array[i], array[counter] = array[counter], array[i]
			counter-=1
