try:
    f=open("TestFile1.txt","r+")    #opening TestFile1.txt in r+ mode
    f2=open("TestFile2.txt","w")   #opening TestFle2.txt in writing mode
    for i in f:
        for j in i:
            if(j=='"'):
                f2.write(f'\\{j}')    #writing into the file test1.txt
            else:
                f2.write(f'{j}')       #writing into the file test1.txt
    f.close()    #closing the TestFile1.txt file
    f2.close()   #closing the TestFile2.txt file

    f2=open("TestFile1.txt","r")      #opening TestFile1.txt in reading mode
    f=open("TestFile2.txt","w")        #opening TestFile2.txt in writing mode
    for i in f2: 
        f.write(i)     #writing  the content of the file test1.txt
        print(i)

    f.close() #closing both the files
    f2.close()
except FileNotFoundError :
    print("File not found.....!")
except IOError:
    print("IO error found.....!\nCheck the logic again!") 
except:
    print("An Error Occured...Revisit your code!")
finally:
    f.close()
    f2.close()

