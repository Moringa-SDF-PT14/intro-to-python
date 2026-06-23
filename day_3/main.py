# import a specific function/variable from a module inside a package
from utils.strings import clean_email

# import full module
from utils import maths

user_email = input("What is your email address?")
n1 = input("First Number")
n2 = input("Second Number")

processed_email = clean_email(user_email)

summation = maths.sum(
    int(n1), int(n2)
)

print(f"Your clean email is {processed_email} and your sum is {summation}")