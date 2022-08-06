try: 
    mylist= [1,2,3,"4",5]
    sum=0
    for i in mylist:
        sum=sum+i
    print(sum)
    print(mylist[5])
except (TypeError,IndexError):
    print("Value Error or Index Error Occured.....!")
