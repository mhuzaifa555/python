# Q1: # Create a set with the numbers {1, 2, 3}.  Add the number 4 to the set.  Remove the number 2. 
#  Print the final set.

# set1 = {1,2,3}
# set1.add(4)
# set1.remove(2)
# print(set1)

# Find the union of both sets. Find the intersection of both sets.Find the difference a - b.
# a = {"apple", "banana", "cherry"} 
# b = {"banana", "kiwi", "mango"}   

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# Q3: Remove duplicates from this list using a set:  
# numbers = [1, 2, 2, 3, 4, 4, 5]
# print(set(numbers))

# Q4 (Slightly Harder): You are given two sets of students:

science_students = {"Ali", "Omer", "Huzaifa", "Sara"}
math_students = {"Sara", "Bilal", "Huzaifa", "Zain"}

# Tasks:

# Find students who study both Science and Math.
# Find students who study only Science.
# Find students who study only Math.
# Find students who study Science or Math (or both) (all unique names).

# print(science_students.union(math_students))
# print(science_students.difference(math_students))
# print(math_students.difference(science_students))
# print(science_students.intersection(math_students))

# MORE QUESTIONS For Dictionary and Sets

# 1. Write a program to create a dictionary of Urdu Animals with values as their English
#translation. Provide user with an option to look it up!

# dictionary = {
#     "kutta" : "Dog",
#     "billi" : "Cat",
#     "magarmach" : "Crocodile",
#     "sher" : "Lion",
#     "hathi" : "Elephant",
#     "bandar" : "Monkey"
# }

# words = input("Urdu mein naam likhien janwar ka aur uska english matlab janye: ")
# print(dictionary[words])

# 2. Write a program to input eight numbers from the user and display the unique numbers (once).
# num = set()
# ab = input("Enter Number 1: ")
# num.add(int(ab))
# ab = input("Enter Number 2: ")
# num.add(int(ab))
# ab = input("Enter Number 3: ")
# num.add(int(ab))
# ab = input("Enter Number 4: ")
# num.add(int(ab))
# ab = input("Enter Number 5: ")
# num.add(int(ab))
# ab = input("Enter Number 6: ")
# num.add(int(ab))
# ab = input("Enter Number 7: ")
# num.add(int(ab))
# ab = input("Enter Number 8: ")
# num.add(int(ab))
# print(num)

num = set()
inp = input("enter a number: ")
num.add(inp)
inp = input("enter a number: ")
num.add(int(inp))
print(num)