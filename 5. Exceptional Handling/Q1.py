n=int(input("Enter the number of test cases : "))
l=[]
for i in range(n):
    s=input()
    l.append(s.split(' '))
for i in l:
    try:
        num=int(i[0])/int(i[1])
        print(num)
    except ZeroDivisionError :
        print("Error Code : integer division or module by zero")
    except ValueError :
        print("Error Code : invalid literal for int() with base 10 : '$'")
