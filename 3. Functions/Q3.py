def max_min(l1):     #func() to return the max and min value of the tuple values inside the list
    max_val = max(l1,key=lambda item:item[1])[1]  #getting the max value from the lamda function
    min_val = min(l1,key=lambda item:item[1])[1]  #getting the min value from the lambda function
    return max_val, min_val       #returning the max and min value
    
l1 = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print("Initial list : ",end='')
print(l1)
print("Maximum and minimum values of the list of tuples : ",end='')
print(max_min(l1))     #printing the returned max and min value
