# check whether a given number is prime or not
def isprime(n):
	i=2
	j=0
	if n in(0,1,2):
		print('Oops! please enter a number greater than 2')
		return
	while (i*i)<n:
		if n%i==0:
			print('not prime')
			j=1
			break
		else:
			i+=1
	if j==0:
		print('prime')
