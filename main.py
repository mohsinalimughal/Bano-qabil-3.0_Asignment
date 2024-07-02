# 1. Calculate the Area of a Rectangle:


# length = int(input("Enter the length of the rectangle:"))
# width = int(input("Enter the width of the rectangle:"))
# area = length*width
# print(f"The area of the rectangle is: {area}")


# 2. Check if a Number is Even or Odd:


# number = int(input("Enter a number:"))
# reminder = number % 2
# if reminder is 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


#  3. Reverse a String:


# string = str(input("Enter string:"))
# reverse = string[::-1]
# print(reverse)

#  4. Find the Factorial of a Number:


# number = int(input("enter number"))
# def factorial(number):
#    if number == 1:
#        return 1
#    else:
#        return number*factorial(number-1)
# print(factorial(number))   


#  5. Check if a String is Palindrome or Not:


# string = str(input("enter string :"))
# def is_palindrome(s):
#     s1 = s.lower().replace(" ", "")
#     ss = s1[::-1]
#     return ss
 
# processed_string = is_palindrome(string)
# if processed_string == string:
#     print(f"{string} is palindrom")
# else:
#     print(f"{string} is not palindrom")

# 6. Generate Fibonacci Series up to n terms:


# n = int(input("Enter number"))
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# print(fibo(n))


#  7. Find the Largest Among Three Numbers:

# numbers = input("Enter numbers with space :")
# list1 = []

# newlist = numbers.split()
# newlist.sort( reverse=True )
# great_number = newlist[0]

# print(f"Greatest number in {numbers} is {great_number}")

#  8. Calculate Simple Interest:

# principal_amount = input("Enter the principal amount:")
# years = input("Enter the time in years:")
# interest_rate = input("Enter the interest rate:")

# total_interest = (principal_amount * years * interest_rate) / 100
# print("Simple intrest:", total_interest)


#  9. Convert Celsius to Fahrenheit:

# temp_in_cel = int(input("Enter temperature in Celsius:"))
# temp_in_fahren = (temp_in_cel * 9 / 5) + 32
# print("Temperature in Fahrenheit:", temp_in_fahren)


#  10. Check Leap Year:

# def is_leap_year_modulo(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# year_to_check = int(input("Enter a year:"))
# result_modulo = is_leap_year_modulo(year_to_check)
# if result_modulo == True:
#  print(f"{year_to_check} is a leap year:")
# else:
#    print(f"{year_to_check} is not a leap year:")


   
# ---------Programming Challenges----------------

# 1.Find the Median of Three Numbers:

numbers = ("Enter three numbers separated by space:")
list1 = numbers.split()
median = sum(list1)
print(median)



