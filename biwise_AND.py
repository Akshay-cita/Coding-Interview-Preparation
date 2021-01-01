
def bitwise_AND(k,test_list):
    cnt=0
    for i in range(0,len(test_list)):
        for j in range(i+1,len(test_list)):
            if test_list[i] & test_list[j] > k:
                print("The pairs are:",(str(test_list[i]),str(test_list[j])))
                cnt+=1
    return cnt



new_list=[]

number_of_test=int(input())
list_test=input().split()
if len(list_test)==number_of_test:
    #print(list_test)
    for i in range(0,len(list_test)):
        new_list.append(int(list_test[i]))

ref_val=int(input())

res=bitwise_AND(ref_val,new_list)
print(res)
        


