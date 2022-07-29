n=int(input("Enter the value of n : "))   #taking the input n and casting it to int type
record={}                    #creating an empty dictionary
for i in range(0,n):         #looping from o to n-1
    temp=input().split(' ')  #splitting the student record
    record[temp[0]]=[temp[1],temp[2],temp[3]]    #storing the student record in dictionary

for i in record:          #traversing through the dictionary
    total=0
    for j in record[i]:
        total+=int(j)         #calculating the total value
    print(round(total/3,2))   #printing the average marks of each student

