[11:44 PM, 10/13/2019] Alok Kr. Singh: def subArraySum(arr, n, sum): 
	l=list()
	for i in range(n): 
		curr_sum = arr[i] 
		j = i+1
		while j <= n: 
			if curr_sum == sum: 
				for k in range(i,j):
				    l.append(arr[k])
				print(l)
				return 1
			if curr_sum > sum or j == n: 
				break
			curr_sum = curr_sum + arr[j] 
			j += 1

	print ("No subarray found") 
	return 0
a = list(map(int,input().split()))
n = len(a)
sum=int(input())
subArraySum(a, n, sum)
