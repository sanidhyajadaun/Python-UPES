s=input().split(' ') #taking input in string and splitting it and storing as a list
for i in range(len(s)-1):   #looping from 0 to len(s)-2 times
    print(s[i][0].upper(),".",sep='',end='')   #printing the first letter in uppercase with '.' 
print("",s[-1].capitalize())   #printing the last name capitalised 
