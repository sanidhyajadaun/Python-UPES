n= int(input('Enter Number of Stamps : '))   #taking the input n and type casting it to int type
stamps_set = {''}                 #empty set
for i in range(0,n):              #looping from 0 to n-1 times
    stamps_set.add(input('Enter name of the country : '))  #adding the name of the country to the set
c=-1
for i in stamps_set:
    c=c+1               #counting the number of values in set
print("Unique Stamps = ", c)  #printing the number of unique stamps
