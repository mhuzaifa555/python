# # 1. Write a program to print multiplication table of a given number using for loop.

# table = int(input("Enter a table no: "))

# for i in range (1,11):
#     print(f"{table}*{i} = {table*i}")
#     i+= 1

# 2. Write a program to great all the person names stored in a list 'I' and which starts with S.

# I = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in I:
#     if(name.startswith("S")):
#        print(f"Hello {name}")

# 3. check prime number
    # n = int(input("Enter a no: "))
    # for i in range(2,n):
    #     if(n%i)==0:
    #         print("Not prime!")
    #         break;
    # else:
    #     print("Prime")

# 4. Write a program to print multiplication table of a given number using while loop.
# table = int(input("Enter a table no: "))
# i=1
# while(i<= 10):
#     print(f"{table} X {i} = {table*i}")
#     i+= 1

# 5. Write a program to calculate the sum of first natural numbers

# n = int(input("Enter a no: "))
# i=1
# sum=0
# while(i<=n):
#     sum = sum+i
#     i+= 1
# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.

# n = int(input("Enter a no: "))
# if (n==0):
#     n=1
# cal1= 1
# for i in range (1, n+1):
#     cal1 = cal1 * i
# print(f"The factorial of {n} is {cal1}")