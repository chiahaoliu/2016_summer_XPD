from pylab import plot, show

#This just makes some lists to plot
def get_lists(a):
	x = []
	y = []
	
	for b in range(0,a):
		x.append(b)
		y.append(3*b - 7)

	return x,y
	

#This initializes the program and gives the final plot
def main(a):
	x,y = get_lists(a)
	plot(x,y)
	show()

main(12)
