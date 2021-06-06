num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # boolean
string = 'Hello World' # string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list,
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) # type check
print(pizza_toppings[1]) # list, access value at index 1
pizza_toppings.append('Mushrooms') # list, add value
print(person['name']) # dictionary, access value
person['name'] = 'George' # dictionary, change value
person['eye_color'] = 'blue' # dictionary, add value
print(fruit[2]) # tuple, access value at index 2

# conditional
if num1 > 45: # if
    print("It's greater")
else: # else 
    print("It's lower")

if len(string) < 5: # if 
    print("It's a short word!")
elif len(string) > 15: # else if
    print("It's a long word!")
else: # else 
    print("Just right!")

# for loop, range()
for x in range(5):
    print(x)
for x in range(2,5): # range from 2-5 but 5 is not included
    print(x)
for x in range(2,10,3): # range from 2-10, increment by 3 (10 is not included)
    print(x)

# while loop
x = 0
while(x < 5):
    print(x)
    x += 1 # increment 

pizza_toppings.pop() # pop method removes the spcified index
pizza_toppings.pop(1) # remove item at index 1 from the list

print(person)
person.pop('eye_color') # pop method removes the item with specified key name
print(person)

# for loop
for topping in pizza_toppings: # start
    if topping == 'Pepperoni': 
        continue # continue 
    print('After 1st if statement')
    if topping == 'Olives':
        break # break

# function 
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # function, parameter 
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # fuction call
print_hello_x_or_ten_times(4) # function call with argument


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'