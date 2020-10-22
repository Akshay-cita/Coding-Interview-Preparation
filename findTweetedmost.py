from collections import Counter


def names_from_Tweet(tweets): #splitting Name from the list
	names=[]
	for pref_name in tweets:
		names.append(pref_name.split()[0])
	return names

Test_case=int(input("Enter the Test sample count to take : \n"))
Test_count=0
tweets=[]

while Test_count<Test_case:
	num=int(input("Enter the tweet counts : \n"))
	count=0
	while count<num:
		item=str(input("Enter the name and tweet_id : \n"))
		tweets.append(item)
		count+=1
	Test_count+=1

a=Counter(names_from_Tweet(tweets))
print(a)
value_set=a.values()
print(value_set)

list_1=[]
list_2=[]
for i in set(value_set):
	list_1 = ([(k, v) for k,v in sorted(a.items()) if v == i])

	if len(list_1) > 1:
		for (k, v) in list_1:
			print ("{} {}".format(k,v))

	max_value = max(a.values())

	list_2 = [(k, v) for k, v in sorted(a.items()) if v == max_value]


	if list_2 != list_1:
		for (k,v) in list_2:
			print("{} {}".format(k,v))