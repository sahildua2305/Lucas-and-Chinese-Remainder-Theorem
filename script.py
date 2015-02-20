from math import sqrt,factorial

# Function copied from https://github.com/sigh/Python-Math
def extended_gcd(a, b):
    """Return (r, s, d) where a*r + b*s = d and d = gcd(a,b)"""
    x,y = 0, 1
    lastx, lasty = 1, 0

    while b:
        a, (q, b) = b, divmod(a,b)
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y

    return (lastx, lasty, a)

def factors(n):
	fac=[]
	while(n%2==0):
		fac.append(2)
		n/=2
	for i in range(3,int(sqrt(n))+1,2):
		while(n%i==0):
			fac.append(i)
			n/=i
	if(n>2):
		fac.append(n)
	return fac

def convertBase(n, b):
	ans = []
	while(n!=0):
		rem = n%b
		ans.append(rem)
		n/=b
	return ans[::-1]

def nCr(n,r):
	if n<r:
		return 0;
	return factorial(n)/(factorial(r)*factorial(n-r))

# Function copied from https://github.com/sigh/Python-Math
def chinese_remainder_theorem(items):
	# Determine N, the product of all n_i
	N = 1
	for a, n in items:
		N *= n
	# Find the solution (mod N)
	result = 0
	for a, n in items:
		m = N//n
		r, s, d = extended_gcd(n, m)
		result += a*s*m
	# Make sure we return the canonical solution.
	return result % N

def calculate(N,R,M):
	crt = []
	facs = factors(M)
	for fac in facs:
		n = convertBase(N,fac)
		r = convertBase(R,fac)
		l = len(n)
		while(len(r)<l):
			r = [0]+r
		prod=1
		for i in range(l):
			prod *= nCr(n[i],r[i])
		crt.append((prod,fac))
	return chinese_remainder_theorem(crt)

for i in range(int(raw_input())):
	N,R,M = map(int, raw_input().split())
	print calculate(N,R,M)
