print("Welcome to VSCode")

# Boolean Variable
isTall = True
isShort = False

# This is a comment.
# I will not be executed by the interpreter

# Conditional Statements
# if - elif
# age = int(input("What is your age: "))
age = 17
if age >= 18:
    print("You need to go to register as a voter")
elif age == 17:
    print("Don't worry if your birthday is before March, you will get a chance to register")
else:
    print("You will need to wait until 2032 elections")

print("Finished check")

# Operations
## Numbers (int, float, complex)

### Arithmetic Operations
a = 6 + 8
b = 9.12 - 2
c = 9 / 3
d = 10 * 6j
e = 6 // 3

### Comparison Operations
# a > b
# b < c
# c >= d
# d <= e

## Strings
### Formatting ~ Interpolation
formatted_message = f"I am {age} years old. {a} "
print(formatted_message)


## More Conditional Statements
### Loops

#### While
it = 1

while it <= 10:
    print(it)
    it += 1

scores = [ 23, 34, 45, 56, 67, 78, 89, 90 ]
#### For
for i in scores:
    print(i)


# Functions
def sum(a, b = 10):
    print(f"Sum of a and b is {a + b}")
    return a + b

h = sum(30, 22)
print(h)

def subtraction(a, b):
    b - a
    print("")
    return b - a

def xyz(a, b):
  b - a
  return b - a

xyz(6,7)