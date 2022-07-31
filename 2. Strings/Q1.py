string1=input()       #taking the string as input
substring=input()     #taking the substring as input
count=0               #int variable assigned to 0
for i in range(len(string1)-len(substring)+1):    #looping from index 0 to lentgh of string-length of substring
    if(string1[i:i+len(substring)]==substring):   #comparing each pair of string to the substring
        count=count+1                #getting the count if the condition is true
print(count)         #printing the total number of occurences
