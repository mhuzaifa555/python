# # 1. Write a program to find the greatest of four numbers entered by the user.

# a = int(input("enter no 1: "))
# b = int(input("enter no 2: "))
# c = int(input("enter no 3: "))
# d = int(input("enter no 4: "))

# if(a>b and a>c and a>d):
#     print("No 1 is the greatest: ",a)
# elif(b>a and b>c and b>d):
#     print("No 2 is the greatest: ",b)
# elif(c>b and c>a and c>d):
#     print("No 3 is the greatest: ",c)
# elif(d>b and d>c and d>a):
#     print("No 4 is the greatest: ",d)

# 2. write a progrem to find out whether a student failed if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.

# Maths = float(input("Enter Subject 1 marks: "))
# English = float(input("Enter Subject 2 marks: "))
# Computer = float(input("Enter Subject 3 marks: "))

# marks = (300/Maths+English+Computer)*100

# if(marks >=40 and Maths >=33 and English >=33 and Computer >=33):
#     print("Passed!")
# else:
#     print("Failed!")

# 3. A spam comment is defined as a text containing following keywords: 
# "Make a lot of money", "buy now". "subscribe this". "click this". Write a program to detect these spams.

# comment = input("Write a comment: ")
# spam1 = "Make a lot of money"
# spam2 = "buy now"
# spam3 = "subscribe this"
# spam4 =  "click this"
# if(spam1 in  comment or spam2 in comment or spam3 in comment or spam4 in comment):
#     print("Its a spam comment!")
# else:
#     print("Not a Spam Comment")

# 4. Write a program to find whether a gwen username contains lgss than 10 characters or not.
# user = input("Create a username: ")
# if(len(user)< 10):
#     print("Username is less than 10 characters")
# else:
#     print("Username have more than 10 characters")

# 5. Write a program which finds out whether a given name is present in a list or not.

# name = input("Enter a name please: ")
# names = [
#     "Huzaifa", "Ali", "Ahmed", "Omar", "Usman", "Hamza", "Yusuf", "Ibrahim",
#     "Ismail", "Bilal", "Salman", "Zaid", "Hassan", "Hussain", "Imran", "Amir",
#     "Faisal", "Khalid", "Suleman", "Tariq", "Noman", "Adnan", "Farhan", "Saad",
#     "Talha", "Rayyan", "Shahbaz", "Ayan", "Ehsan", "Danish", "Shahzad", "Junaid",
#     "Mazhar", "Aslam", "Rizwan", "Nouman", "Haroon", "Shahid", "Sami", "Sameer",
#     "Zubair", "Shahrukh", "Arsalan", "Muneeb", "Ammar", "Zeeshan", "Azlan",
#     "Shafqat", "Basit", "Shakeel", "Naveed"
# ]

# if(name in names):
#     print("Name found!")
# else:
#     print("name not found! Try another.")