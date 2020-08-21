#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 




#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

list1=list(range(21))
square=[i**2 for i in list1]
print(square)


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

list2 = [2]
power_of_two=[i**50 for i in list2]
print(power_of_two)


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

list3=list(range(101))
sqrt=[i**.5 for i in list3]
print(sqrt)


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

list4=list(range(-10,1))
my_list=[i for i in list4]
print(my_list)


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

list5=list(range(1,101))
odds=[i for i in list5 if i%2==0]
print(odds)


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

list6=list(range(1,1000))
divisible_by_seven=[i for i in list6 if i%7==0]
print(divisible_by_seven)


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels=[i for i in teststring if not i=="a" if not i=="e" if not i=="i" if not i=="o" if not i=="u"]
print(non_vowels)


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

list8=list('The Quick Brown Fox Jumped Over The Lazy Dog')   
capital_letters=[i for i in list8 if i.isupper() == True]
print(capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

list9=list('The quick brown fox jumped over the lazy dog')   
consonants=[i for i in list9 if i!="a" if i!="e" if i!="i" if i!="o" if i!="u"]
print(consonants)


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

import os
files=[i for i in os.listdir("/Users/Javi/Ironhack/datamad0820")]
print(files)


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

import random
random_lists=[[random.randint(0, 101) for i in range(10)],[random.randint(0, 101) for i in range(10)],[random.randint(0, 101) for i in range(10)],[random.randint(0, 101) for i in range(10)]]
print (random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list=[i for sublist in list_of_lists for i in sublist]
print (flatten_list)


#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(i) for sub in list_of_lists for i in sub]
print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 

for i in ['a','b','c']:
    try:
        print (i**2)
    except Exception as e:
        print (e)


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print ("No puedes dividir entre 0")
finally:
    print ("All Done.")


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]

try:
    print(abc[3])
except IndexError:
    print ("Elemento fuera de rango en la lista")


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

def division (a,b):
    return a/b
try:
    a=int(input("introduzca el numero a: "))
    b=int(input("introduzca el numero b: "))
    print (division (a,b))
except ZeroDivisionError:
    print ("No puedes dividir entre 0")   
except ValueError:
    print ("debes introducir un número entero")


#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('testfile','r')
    print(f.write('Test write this'))
except Exception as e:
    print (e)
    print ("No existe el archivo indicado")


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
    line = f.readline()
except FileNotFoundError:  
    print("no se encuentra el archivo")
try:
    i = int(s.strip())
except NameError:
    print("s no ha sido definida")


#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
try:
    linux_interaction()    
    print('Doing something.')
except Exception as e:
    print (e)


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

while True:
    try:
        a=int(input("introduzca un número entero ="))
        sqr=a**2
        print(sqr)
        break
    except ValueError:
        print("el dato introducido no es correcto")


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results1=[]
divisibles_2=[i for i in range(1001) if i%2==0]
divisibles_3=[i for i in range(1001) if i%3==0]
divisibles_4=[i for i in range(1001) if i%4==0]
divisibles_5=[i for i in range(1001) if i%5==0]
divisibles_6=[i for i in range(1001) if i%6==0]
divisibles_7=[i for i in range(1001) if i%7==0]
divisibles_8=[i for i in range(1001) if i%8==0]
divisibles_9=[i for i in range(1001) if i%9==0]
results1.append(divisibles_2)
results1.append(divisibles_3)
results1.append(divisibles_4)
results1.append(divisibles_5)
results1.append(divisibles_6)
results1.append(divisibles_7)
results1.append(divisibles_8)
results1.append(divisibles_9)
results=[i for num in results1 for i in num]
print(list(set(results)))


# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

while True:
    Total_Marks=0
    Num_of_Sections=0
    try:
        Total_Marks = int(input("Enter Total Marks Scored: "))
        if Total_Marks>0:
            Num_of_Sections = int(input("Enter Num of Sections: "))
            if Num_of_Sections>2:
                break
    except Exception as e:
        print(e)

