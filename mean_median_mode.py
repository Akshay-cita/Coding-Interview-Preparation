
import collections


def mean(x,lg):
	sum=0
	for i in x:
		sum+=i
	resultMean=float(sum/n)
	return resultMean


def median(y,lg):
	j=0
	if lg%2==0:
		c=int(lg//2)
		#print(c)
		j=c
		return ((y[j]+y[j-1])/2)
	else:
		c=int(lg//2)
		#print(c)
		j=c
		return y[j]

def mode(z,lg):
	cnt=collections.Counter(z)
	get_mode_data=dict(cnt)
	mode=[]
	for k,v in get_mode_data.items():
		if v==max(cnt.values()):
			mode.append(k)
	return mode
			



		
	
	# cntList=[]
	# z.sort()
	# while i< (lg-1):

	# 	if z[i]==z[i+1]:
	# 		cnt+=1
	# 		cntList.append(cnt)
	# 		i=i+1
	# 	else:
	# 		i+=1
	# print(cntList)
	# print(max(cntList))
	# for i in range(0,lg+1):
	# 	cnt=z[i].count()

	# 	print("The count of {} is {}".format(z[i],cnt))

	







n=int(input("Enter the maximum length of an array:\n"))
list=[]
while len(list)<n:
	list.append(float(input()))

Result_mean=mean(list,n)
Result_median=median(list,n)
Result_mode=mode(list,n)
print("The mean is: {}".format(Result_mean))
print("The median is: {}".format(Result_median))
print("The mode is: {}".format(Result_mode))


