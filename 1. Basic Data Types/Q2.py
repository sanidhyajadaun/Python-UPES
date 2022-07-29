n=int(input("Enter the value of n : "))  #taking the input n and type casting it to int type
sample_list=[]                    #empty list
for i in range(0,n):              #looping from 0 to n-1
    sample_list.append(int(input())) #appending the input scores to the list in integer format
z=max(sample_list)                       #assigning z the max element of the list
while max(sample_list)==z:           #removing the max element stored in the z using whle loop
    sample_list.remove(max(sample_list)) 

print("Score of the Runner up : ",max(sample_list))   #printing the runner up score
