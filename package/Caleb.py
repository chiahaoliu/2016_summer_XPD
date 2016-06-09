#This is to practice making a module for further work

def caleb1(x):
	if (x*1.0).is_integer():
		if x % 2 == 0:
			print 'Yes, even'
		else:
			print "No, try again"
	else:
		print "Please input integer"


def caleb2(x):
	k = 3*x
	l = 4-x

	return 7*l + k
