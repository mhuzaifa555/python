# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

# name = input("Enter your name: ")
# print(f"Good Afternoon ! {name}")

# 2.
# Write a program to fill in a letter template given below with name and date.
letter ='''
Dear <|Name|> ,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","huzaifa").replace("<|Date|>","29-08-2025"))