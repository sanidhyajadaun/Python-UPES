# **Python-UPES**
 
In this repository. I am adding Python lab work of UPES. It is being covered from the basics, hopefully it will help the beginners.

#

## **1. Basic Data Types**

Q1. WAP to read the record of n students in a dictionary containing key/value pairs of name: [marks]. Print the average of the marks obtained by the particular student correct to 2 decimal places. <br>
Input Format <br>
The first line contains the integer n, the number of student’s records. The next n lines contain the names and marks obtained by a student, each value separated by a space.<br>
Sample Input<br>
3 <br>
Krishna 67 68 69 <br>
Arjun 70 98 63 <br>
Malika 52 56 60 <br>
Sample Output <br>
56.00 <br>

Q2. WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.<br>
Sample Input <br>
N = 5 <br>
Scores= 2 3 6 6 5 <br>
Sample output <br>
5 <br>


Q3. Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of country stamps. Find the total number of distinct country stamps using a suitable data type. 

#

## **2. Strings**


Q1.  WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.<br>
Sample Input<br>
ABCDCDC<br>
CDC<br>
Sample Output<br>
2<br>


Q2. WAP to input the first name, middle and last name of a person. Your task is to print the initials of the first and middle name separated by a dot (.) <br>
The last name should be followed by a dot and a space where the first letter is capital. <br>
Sample Input <br>
Mohandas KaramChand Gandhi <br>
Sample Output <br>
M.K. Gandhi <br>


Q3. Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same. <br>
Sample Input <br>
ABaBCbGc <br>
Sample Output <br>
2A <br>
3B <br>
2C <br>
1G 

#

## **3. Functions**

Q1. Using functions, re-write and execute Python program to: <br>
1. Add natural numbers up to n where n is taken as an input from user.<br>
2. Print Fibonacci series till nth term (Take input from user).<br>


Q2. At an airport, a traveler is allowed entry into the ﬂight only if he clears the following checks:<br>
1. Baggage Check <br>
2. Immigration Check<br>
3. Security Check <br>
The logic for the check methods are given below:<br>
check_baggage (baggage_weight)<br>
•	returns True if baggage_weight is greater than or equal to 0 and less than or equal to 40. Otherwise returns False. <br>
check_immigration (expiry_year) <br>
•	returns True if expiry_year is greater than or equal to 2030 and less than or equal to 2050. Otherwise returns False. <br>
check_security(noc_status) <br>
•	returns True if noc_status is 'valid' or 'VALID', for all other values return False.
traveler() <br>
•	Initialize the traveler Id and traveler name and invoke the functions check_baggage(), check_immigration() and check_security() by passing required arguments. <br>
Refer the table below for values of arguments. <br>

Variable        ||          Value   <br>
traveler ID                 1001    <br>
traveler name               Jim     <br>
baggage weight              39      <br>
expiry year                 2019    <br>
noc_status                  VALID   <br>

•	If all values of check_baggage(), check_immigration() and check_security() are true, 
-	display traveler_id and traveler_name
-	display "Allow Traveler to ﬂy!"
Otherwise,
-	display traveler_id and traveler_name
-	display "Detain Traveler for Re-checking!
Invoke the traveler() function. Modify the values of diﬀerent variables in traveler() function and observe the output.


Q3. Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.<br>
Original list with tuples: <br>
[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]   <br>
Output- <br>
Maximum and minimum values of the said list of tuples: <br>
(74, 62) <br>

#

## **4. Files**

Q1. Write a Python program to: <br>
1. read a ﬁle.      <br>
2. add backslash (\) before every double quote in the ﬁle contents. <br>
3. write it to another ﬁle in the same folder. <br>
4. print the contents of both the ﬁles. <br>
For example: <br>
If the ﬁrst ﬁle is 'TestFile1.txt' with text as: <br>
Jack said, "Hello Pune". <br>
The output of the ﬁle 'TestFile2.txt' should be:<br>
Jack said,\"Hello Pune\".<br>

Q2. Consider a ﬁle 'rhyme.txt' in D Drive with following text:
 
Jingle bells jingle bells <br>
jingle all the way <br>
oh what fun is to ride <br>
In a one horse open sleigh <br>
Jingle bells jingle bells <br>
Jingle all the way <br>

Write a Python program to count the words in the ﬁle using a dictionary (use space as a delimiter). Find unique words and the count of their occurrences (ignoring case). Write the output in another ﬁle "words.txt" at the same location.

Q3. Assume a file city.txt with details of 5 cities in given format (city name population(in lakhs) area(in sq KM) ): <br>
Example: <br>
Dehradun 5.78 308.20 <br>
Delhi 190 1484 <br>
…………… <br>
Open file city.txt and read to: <br>
a.	Display details of all cities  <br>
b.	Display city names with population more than 10Lakhs<br> 
c.	Display sum of areas of all cities <br>

# 

## **5. Exceptional Handling**

Q1. Input two values from user where the first line contains N, the number of test cases.<br>
The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Print the error code in the case of ZeroDivisionError or ValueError.<br>
Sample input<br>
1 0<br>
2 $<br>
3 1<br>
Sample Output<br>
Error Code: integer division or modulo by zero<br>
Error Code: invalid literal for int() with base 10: '$'<br>
3<br>

Q2. Assume the following Python code- <br>
Rewrite the code to handle the exceptions raised. Print appropriate error messages wherever applicable <br>

mylist = [1,2,3,"4",5] <br>
sum = 0 <br>
for i in mylist :<br>
    sum = sum + i<br>
print(sum)<br>
print(mylist[5])<br>

Q3. You have already created a Python program to implement the following in ﬁle handling section: 
1. Read a ﬁle.<br>
2. Add backslash (\) before every double quote in the ﬁle contents. <br>
3. Write it to another ﬁle in the same folder. <br>
4. Print the contents of both the ﬁles. <br>
For example: <br>
If the ﬁrst ﬁle is 'TestFile1.txt' with text as:<br>
Jack said, "Hello Pune". <br>
The output of the ﬁle 'TestFile2.txt' should be:<br>
Jack said,\"Hello Pune\". <br>
Modify your code to implement Exception handling. Print appropriate error messages wherever applicable <br>



#

## **6. OOPS**

Q1. 
- Create a class employee with the follwoing properties
•	First Name 
•	Last Name
•	Pay
•	Email : should be automatically generated as
	Firstname+'.'+Lastname+"@company.com"

- Test the code with the following information ofan employee :
•	First name is : Mohandas
•	Last name is : Gandhi
•	Pay is : 50000

