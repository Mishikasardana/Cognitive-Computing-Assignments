#ques.1 :  Write a Python program to print "Anything You find cool."
print("Anything you find cool")

#ques2: Add Numbers and Concatenate Strings
#2.1 : Write a program to add two numbers and print the result.
a = 10
b = 5
a = a + b
print(a)
#2.2 :  Write a program to concatenate two strings and print the result.
print("Hello " + "World")
#2.3 : Write a program to concatenate a string and a number and print the result.
message = "Hello World"
number = 12
result = message + str(number)
print(result)

#ques3 : If-Else Statements
#3.1 :  Write a Python program to check if a number is positive, negative, or zero using an if-else statement.
a = int(input("Enter a number : "))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else :
    print("Invalid")

#3.2 : Write a program to check if a given number is odd or even.
a = int(input("Enter a number"))
if a%2 == 0 :
    print("even")
elif a%2 != 0:
    print("odd")
else :
    print("invalid")

#ques4 : Loops
#4.1 :  Write a program to print numbers from 1 to 10 using a for loop.
for i in range (1,11) :
    print(i)
#4.2 :  Write a program to print numbers from 1 to 10 using a while loop
i = 1
while i <= 10 :
    print(i)
    i = i + 1
#4.3 : Write a program to calculate the sum of numbers from 1 to 100 using a loop.
i = 1
sum = 0
while i <= 100 :
    sum += i
    i = i + 1
print(sum)

#ques5. Data Structures
#5.1 : Create a list of 5 numbers. Write a program to find the largest and smallest numbers in the list.
abc = [1,4,2,5]
abc.sort()
print(abc)
print("Min : ")
print(abc[0])
print("Max: ")
print(abc[3])

#5.2 :  Create a dictionary with at least 3 key-value pairs. Write a program to retrieve the value of a given key.
my_dictionary = {
    "apple": "a fruit",
    "car": "a vehicle",
    "book": "a collection of pages"
}
def get_value(key):
    return my_dictionary.get(key, "Key not found")
key = input("Enter the key: ")
value = get_value(key)
print("The value for the key '{}' is: {}".format(key, value))

#5.3 : Write a program to sort a list of numbers in ascending and descending order.
def sort_ascending(lst):
    return sorted(lst)
def sort_descending(lst):
    return sorted(lst, reverse=True)
numbers = [5, 2, 9, 1, 5, 6]
ascending_order = sort_ascending(numbers)
print("Ascending Order:", ascending_order)
descending_order = sort_descending(numbers)
print("Descending Order:", descending_order)

#5.4 : Write a program to merge two dictionaries into one.
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2) 
    return merged_dict
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
merged_dict = merge_dicts(dict1, dict2)
print("Merged Dictionary:", merged_dict)

#ques.6 : Strings
#6.1 :  Write a program to count the number of vowels in a given string.
def count_vowels(input_string):
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

input_string = "Hello World!"
print(f"The number of vowels in '{input_string}' is: {count_vowels(input_string)}")

#6.2 : Write a program to reverse a string and print it
def reverse_string(input_string):
    reversed_string = input_string[::-1] 
    return reversed_string 

input_string = "Hello, World!"
print(f"The reversed string is: '{reverse_string(input_string)}'")

#6.3 : Write a program to check if a string is a palindrome

def reverse_string(input_string):
    reversed_string = input_string[::-1] 
    return reversed_string 
def is_palindrome(input_string):
    reversed_string = reverse_string(input_string)
    return input_string == reversed_string

input_string = "naman"
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")


#ques7 : File Handling
#7.1 :  Write a program to create a text file, write some text into it, and then read and print the content.
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")

with open("sample.txt", "r") as file:
    content = file.read()

print("Content of the file:")
print(content)

#7.2 :  Write a program to append text to an existing file and print the updated content.
with open("sample.txt", "a") as file:
    file.write("This text is appended to the file.\n")
with open("sample.txt", "r") as file:
    content = file.read()

print("Updated content of the file:")
print(content)

#7.3 : Write a program to count the number of lines in a text file.
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)
filename = "sample.txt"
number_of_lines = count_lines(filename)
print(f"The number of lines in '{filename}' is: {number_of_lines}")

#ques 8: Exceptional Handelling
#8.1 :  Write a program to handle division by zero using a try-except block.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

num1 = 5
num2 = 0
result = divide_numbers(num1, num2)
print(result)

#8.2 : Write a program to handle invalid input (e.g., when the user enters a string instead of a number).
def get_number_from_user():
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input.")
number = get_number_from_user()
print(f"You entered the number: {number}")

#8.3 : Write a program to demonstrate the use of 
finally in exception handling.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    finally:
        print("This block is always executed.")
    return result
num1 = 5
num2 = 0
result = divide_numbers(num1, num2)
if result is not None:
    print(f"The result of {num1} divided by {num2} is: {result}")

#ques9 : Random Numbers
#9.1 : Write a program to generate 5 random numbers between 1 and 100 and print them.
import random
def generate_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    return random_numbers
random_numbers = generate_random_numbers()
print("Generated random numbers:", random_numbers)

#9.2 :  Write a program to generate a random number and check if it is prime.
import random

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
random_number = random.randint(1, 100)
if is_prime(random_number):
    print(f"The generated number {random_number} is prime.")
else:
    print(f"The generated number {random_number} is not prime.")

#9.3 : Write a program to simulate rolling a six-sided die.
import random
def roll_die():
    return random.randint(1, 6)

result = roll_die()
print(f"You rolled a {result}.")

#9.4 : Write a program to shuffle a list of numbers
import random
def shuffle_list(numbers):
    random.shuffle(numbers)
    return numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)
shuffled_numbers = shuffle_list(numbers)
print("Shuffled list:", shuffled_numbers)

#9.5 : Write a program to randomly select an item from a list.
import random
def select_random_item(numbers):
    return random.choice(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selected_number = select_random_item(numbers)
print(f"The randomly selected number is: {selected_number}")

#9.6 :  Write a program to generate a random password of given length.
import random
import string
def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
length = 8
random_password = generate_random_password(length)
print(f"Generated password: {random_password}")

#9.7: Write a program to pick a random card from a standard deck of 52 cards
import random

def pick_random_card():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    rank = random.choice(ranks)
    suit = random.choice(suits)
    return f"{rank} of {suit}"
random_card = pick_random_card()
print(f"The randomly picked card is: {random_card}")

#ques10: Command Line Argument
#10.1 :  Write a program to accept two numbers as command-line arguments, add them, and print the result
import sys
if len(sys.argv) != 3:
    print("Usage: python script_name.py <number1> <number2>")
    sys.exit(1) 
number1 = float(sys.argv[1])
number2 = float(sys.argv[2])
result = number1 + number2
print(f"The sum of {number1} and {number2} is: {result}")

#10.2 :  Write a program to accept a string as a command-line argument and print its length
import sys
if len(sys.argv) != 2:
    print("Usage: python script_name.py <string>")
    sys.exit(1) 
input_string = sys.argv[1] 
string_length = len(input_string)
print(f"The length of the string '{input_string}' is: {string_length}")

#ques11 : Use Of Libraries
#11.1 :  Write a program to use the math library to calculate the square root of a given number.

import math
def calculate_square_root(number):
    return math.sqrt(number)
number = 9
square_root = calculate_square_root(number)
print(f"The square root of {number} is: {square_root}")

#11.2 : Write a program to use the datetime library to print the current date and time
import datetime

def print_current_datetime():
    current_datetime = datetime.datetime.now()
    print(f"The current date and time is: {current_datetime}")
print_current_datetime()

#11.3 :  Write a program to use the os library to list all files in the current directory.
import os

def list_files_in_current_directory():
    files = os.listdir('.')
    return files
files = list_files_in_current_directory()
print("Files in the current directory:")
for file in files:
    print(file)









