"""Making Decision in Python
Alex Minnich
4.12.2026
Purpose: This code will determine if a student has passed or failed the class."""
print("Welcome to SDEV 120 class!")
name = input("Please enter your name:") #This will acquire the user's name
grade = int(input("Please enter your grade:")) #This will acquire the user's grade
if grade >= 60:
    print(f"Hello {name}, you passed this class.") #Statement saying the student passed the class
elif grade < 60:
    print(f"Hello {name}, you failed this class.") #Statement saying the student failed the class
