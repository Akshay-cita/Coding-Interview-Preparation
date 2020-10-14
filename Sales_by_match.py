import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	if len(ar)==n:
		ar.sort()
		print("sorted array:\n",ar)
		i=0
		cnt=0
		while i< (n-1):
			if ar[i]==ar[i+1]:
				cnt+=1
				i=i+2
			else:
				i+=1
	print(cnt)
			

if __name__ == '__main__':
	n = int(input())
	ar =[]
	for i in range(0,n):
		num=random.randint(1,n)
		ar.append(num)
	print(ar)
	result = sockMerchant(n, ar)
	print(result)
	