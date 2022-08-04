def sum_n() :    #function definition of function sum_n()
    n=int(input("Enter the number till where you want to get the sum : "))
    sum_of_all=0
    for i in range(1,n+1):
        sum_of_all+=i     #calculating the sum of n numbers
    print("Sum of all the numbers upto {} is {}".format(n,sum_of_all))

def fibonacci():    #function definition of function fibonacci()
    n=int(input("Enter how many fibonacci numbers you want to print : "))
    x=0
    y=1
    print("Fibonacci series : ",x,y,end=" ")
    for i in range(2,n):
        z=x+y
        print(z,end=" ")   #printing the n fibonacci numbers 
        x=y
        y=z
        
        
sum_n()     #function call of function sum_n()
fibonacci()    #function call of function fibonacci()
