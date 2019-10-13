Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check( a, n): 
	m = 0
	if (a[0] > a[1]) : 
		a[0] = a[1] // 2
		m+=1
	for i in range ( 1, n - 1): 
		if ((a[i - 1] < a[i] and a[i + 1] < a[i]) or (a[i - 1] > a[i] and a[i + 1] > a[i])): 
			a[i] = (a[i - 1] + a[i + 1]) // 2
			if (a[i] == a[i - 1] or a[i] == a[i + 1]): 
				return False
			m+=1
	if (a[n - 1] < a[n - 2]): 
		m+=1
	if (m > 1): 
		return False

	return True
a = list(map(int,input().split()))
n = len(a) 
print(check(a,n))
SyntaxError: invalid syntax
>>> 
>>> 
