f=open('city.txt','r')      #opening file city.txt in reading mode
print('Displaying details of all cities'.center(70,'-'))  
for line in f:
    print(line, end='')     #displaying the details of the city

f.seek(0)     #reaching at the beginning of the file

print('\n' + 'Displaying city names with population more than 10 Lakhs'.center(70,'-'))
l = f.readlines()       #getting the list of the content of the file in l
data = []
for i in range(5):
    data.append(l[i].rstrip('\n').split(' '))     #storing the data of readline() to the data[] in nested list format

for i in data:
    if(float(i[1])>10):
        print(i[0])       #displaying city names having population greater than 10 lakhs

print('\n' + 'Displaying sum of areas of all cities'.center(70,'-'))
sum = 0.0
for i in data:
    x = float(i[2])
    sum = sum + x       #calculating the sum of the areas of all cities
print('Sum of areas of all cities = {} sq Km'.format(sum))

f.close()   #closing the file
