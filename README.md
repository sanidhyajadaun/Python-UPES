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
