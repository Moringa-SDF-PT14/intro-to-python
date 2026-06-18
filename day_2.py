# Lists => mutable collection/sequence(ordering) of elements

## List Literal
tech_stack = [ 'React', 'NodeJS', 'Flask' ]

## list constructor => list(iterable)
scores = list((1, 2, 3))
letters = list("hello") 

## list comprehension technique => apply a function (generate numbers) to a loop
numbers = [1,2,3,4,5]
squares = [ x*x  for x in numbers ]

## multiplication => repeat elements using * operator
ones = [1] * 10

# print(tech_stack)
# print(scores)
# print(letters)
# print(squares)
# print(ones)

## List Methods

### Add Items to lists

#### .append(i) => adds item at the end of the list
tech_stack.append("PostgreSQL")
# print(tech_stack)

tech_stack[4:] = ["Docker", "Kubernetes"]
# print(tech_stack)

# TODO: Given x in arr[a:x] explain the role of x
tech_stack[3:4] = ["AWS", "AI", "Azure"]
# print(tech_stack)

#### .extend([i]) => add an iterable at the end of list
scores.extend([20,21,22])

#### .insert(index, [value]) => add an item to the specific position
scores.insert(4, 20)

#### .remove(value) => remove first item that matches the value / raise an error
# print(scores)
scores.remove(20)
# print(scores)

#### .pop(index) => remove an item from a given position (if index == -1 or missing it will remove last item)
scores.pop(-1)
# print(scores)


#### .clear() => remove all items in the list
# scores.clear()
# print(scores)

# del tech_stack[:]
# print(tech_stack)


#### .index(value) => finds the zero-based index of the first occurrence of a value. If not found raises an error 
# scores.append([21])
index_of_21 = scores.index(21)
# print(index_of_21)

#### .sort(reverse=False) => sorting of items, by default is in ascending orders. Done `in place` ==> mutates the original list
scores.sort(reverse=True)
# print(scores)
## TODO: Check docs for `sorted`

#### .reverse() => reverse the order in a list
# print(tech_stack)
tech_stack.reverse()
# print(tech_stack)

#### .copy() => creates a copy (shallow)
scores_2 = scores.copy()
# print(scores)
# print(scores_2)



## Tuples => Immutable collection of elements / Read Only
server_config = ( "http://10.0.0.1", 1234 )
# print(server_config)

hello = "hello"
summation = (hello,) + ("20",)
# print(summation)

port = server_config.index(1234)
# print(f"Port is {port}")


#### enumerate(iterable) => cycles through an array returning a tuple containing an index and its value

odd_squares = []
for index, number in enumerate(numbers):
    p = index + 1
    if (p % 2) != 0:
        odd_squares.append(p**2)

print(odd_squares)

#### Squares
squares_2 = [ number**2 for index, number in enumerate(numbers) ]
print(squares_2)

## TODO: In class use comprehension to find odd number squares


#### Functions
## lambda functions => anonymous function (misses naming) restricted to singular expressions

multiplier = lambda num, index: num * index
print(f"10 x 19 = { multiplier(10, 19) }")

# ternary => condition ? true : false

# true if condition else false

odd_multiplier = lambda index, number: number ** 2 if ((index+1) % 2) != 0 else -1
squares_3 = [ odd_multiplier(index, number) for index, number in enumerate(numbers) ]
print(squares_3)

# to remain with real squares, apply filter/pop to remove all occurrences of -1


## Dictionaries -> Key-value pair store
user = {
    "name": "Johnson",
    "age": 35,
    "height": 173.5,
    -1: "hello world",
    True: "home"
}

print(user[-1]) # if not found , app crashes
print(user.get("height")) # retrieve item, if not found will return None

print(type(user))

# dict([key, value]) constructor =>
water_drunk = [ ("Mon", 2), ("Tue", 4), ("Wed", 3), ("Thur", 2), ("Fri", 2) ]
water = dict(water_drunk)
print(water)

heights = dict(mercy=180, million=177, alma=170, stephen=191)
print(heights)

# dictionary comprehension
squares_4 = { i:n**2  for i, n in enumerate(numbers) }
print(squares_4)

## add items
heights["ian"] = 150
print(heights)

## delete item
del heights["ian"]
print(heights)

print(list(heights))

for k, v in heights.items():
    print(k, v)

for k, v in enumerate(heights):
    print(k, v)


## Set -> unordered collection of unique items

basket = { "milk", "eggs", "bread", "milk", "banana", "fresh juice" }
print(basket)

hello_set = set("hello world")
print(hello_set)

moringa_set = { x for x in "welcome to moringa" }
print(moringa_set)

## Mathematical Operations

x1 = { 2, 6, 9, 12, 18, 8 }
x2 = { 1, 3, 9, 13, 12, 4 }

## values in x1 not in x2 [] -
print(x1 - x2)

## values in x1, x2, or both [Union] |
print(x1|x2)

## values in both x1 and x2 [Intersection] &
print(x1&x2)

## values in x1, x2 but not both [] ^
print(x1^x2)


## Strings Method
handwriting_test = "The quick brown fox jumped over a lazy dog"

### Concatenate +
print(handwriting_test + " Herehereere")

### Slicing ==> Index operator []
print(handwriting_test[0])

# end item -1 index
print(handwriting_test[-1])

## to get items from position a -> n use arr[a:n+1]
print(handwriting_test[3:9])

# total items in an iterable len(iterable)
print(len(handwriting_test))

# repetition *
print(handwriting_test * 2)

## `in` as a membership check
print("the" in handwriting_test)

## case formatting => .upper() .lower()
print(handwriting_test.upper())

## trimming / strip => .strip()
print(handwriting_test.strip("g"))

## replace(old, new) => swaps substrings
print(handwriting_test.replace("The", "Ule"))

## split(delim) text into a list of substrings
split_words = handwriting_test.split(" ")
print(split_words)

## join iterables using a string
joined = "___***___".join(split_words)
print(joined)