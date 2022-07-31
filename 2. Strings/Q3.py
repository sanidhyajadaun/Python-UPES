string= input("Enter the string : ")   #taking the string as input
string= string.upper()        #converting string to uppercase()
s = set()            #definig s as set
count = []           #empty set count 
for i in string: 
    s.add(i)         #adding each letter of string to the set
for i in s:
    count.append(string.count(i))    #storing the count of elements of s in string
letters=list(s)               #converting s to list and storing it to the a variable letters
for i in range(len(letters)):
    print(count[i],letters[i])   #printing the count and the particular letter
