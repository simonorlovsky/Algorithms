# ps01

YES = [0,1,1,2,2,3,3,9,9]
EW = [0,1,1,1,4,4,4,5,5,5,8]

def pre(yes, ew):
	YESready = []
	EWready = []
	for i in range(max(yes)):
		YESready.append(0)
	for i in range(max(ew)):
		EWready.append(0)

	for i in range(len(YES)):
		YESready[YES[i]-1] = YESready[YES[i]-1] + 1

	for i in range(len(EW)):
		EWready[EW[i]-1] = EWready[EW[i]-1] + 1


	return YESready, EWready

def post(YESready, EWready):
	return TRUE

def main():
	YESready, EWready = pre(YES, EW)
	print YESready
	print EWready

main()