f1=open("rhyth.txt","r")   #opening rhyth.tx in reading mode
f2=open("jinglecount.txt","w")  #opening jinglecount.txt in writing mode

l=f1.readlines()       #getting the content of the file in nested list format having '\n' at the end
data=[]       
for i in range(len(l)):
    data.append(l[i].rstrip('\n').split(' '))   #appending the elements of l in data

s=set()     #empty set
samplecount=[]   #empty list
for i in data:
    for j in i:
        s.add(j)    #adding the data to the set 
        samplecount.append(j)   #converting the list to normal list from nested list

count=[]
for i in s:
    count.append(samplecount.count(i))   #storing the count of each element in the list count

dictionary_record={}
j=0
for i in s:
    dictionary_record[i]=count[j]    #creating a dictionary of the set elements and their respective counts
    j=j+1

total_count=0
for x,y in dictionary_record.items():
    total_count+=int(y)

f2.write(f'Total count of the words by using dictionary : {total_count}\n')    #writing the total count into the file jinglecount.txt
f2.write(f'{dictionary_record}')       #writing the dictionary of unique elements with their respective counts in the jinglecount.txt

#printing the output on the terminal what we have write into the file
print("Total count of the words by using dictionary : ",total_count)    
print(dictionary_record)

#closing both the files
f1.close()
f2.close()
