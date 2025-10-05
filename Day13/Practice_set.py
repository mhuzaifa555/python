# # 1. Write a program to print multiplication table of a given number using for loop.

# table = int(input("Enter a table no: "))

# for i in range (1,11):
#     print(f"{table}*{i} = {table*i}")
#     i+= 1

# 2. Write a program to great all the person names stored in a list 'I' and which starts with S.

I = ["Harry", "Soham", "Sachin", "Rahul"]

for name in I:
    if(name.startswith("S")):
       print(f"Hello {name}")