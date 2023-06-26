# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.

# def keyword is used to create a function with function name 
# Syntax:--
# def func_name():
#   statement
#   return statement

def odd_n():
    li = []
    for i in range(1,25):
        if i % 2 != 0:
            li.append(i)
        
    return li

odd_n()

# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to
# demonstrate their use.

#The *args and **kwargs syntax in Python is used to handle a variable number of arguments in functions.

#The *args parameter allows a function to accept any number of positional arguments. 
#It collects these arguments into a tuple, which can be iterated over or accessed individually within the function.

def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

calculate_sum(5)
