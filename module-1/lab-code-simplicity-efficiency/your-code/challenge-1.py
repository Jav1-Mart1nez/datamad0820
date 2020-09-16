"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')

dict = {"negative five": -5,
        "negative four": -4,
        "negative three": -3,
        "negative second": -2,
        "negative one": -1,
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
       }

def suma (num1, operator, num2):
    
    if num1 != "zero" and num1 != "one" and num1 !="two" and num1 != "three" and num1 != "four" and num1 != "five":
        print("I am not able to answer this question. Check your input.")
    elif num2 != "zero" and num2 != "one" and num2 !="two" and num2 != "three" and num2 != "four" and num2 != "five":
        print("I am not able to answer this question. Check your input.")
    else:
        return print(f"{num1} plus {num2} equals", (list(dict.keys())[list(dict.values()).index(dict[f"{num1}"]+dict[f"{num2}"])]))

def resta (num1, operator, num2):

    if num1 != "zero" and num1 != "one" and num1 !="two" and num1 != "three" and num1 != "four" and num1 != "five":
        print("I am not able to answer this question. Check your input.")
    elif num2 != "zero" and num2 != "one" and num2 !="two" and num2 != "three" and num2 != "four" and num2 != "five":
        print("I am not able to answer this question. Check your input.")
    else:
        return print(f"{num1} minus {num2} equals", (list(dict.keys())[list(dict.values()).index(dict[f"{num1}"]-dict[f"{num2}"])]))

num1 = input('Please choose your first number (zero to five): ')
operator = input('What do you want to do? plus or minus: ')
num2 = input('Please choose your second number (zero to five): ')

if operator=="plus":
    suma (num1, operator, num2)
elif operator=="minus":
    resta (num1, operator, num2)
else:
    print("I am not able to answer this question. Check your input.")

print("Thanks for using this calculator, goodbye :)")





