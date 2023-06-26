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

calculate_sum(1,2,3)

#On the other hand, **kwargs stands for "keyword arguments" and allows a function to accept any number of keyword arguments in the form of key-value pairs. 
# These arguments are collected into a dictionary within the function.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(a=1,b="ashir")


#Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
#used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,
#18, 20].

l=[2,4,6,8,10, 12, 14, 16,18, 20]
print("In Python, an iterator is an object that allows us to traverse a collection of elements,\n such as a list, tuple, or dictionary. It provides a way to access elements sequentially without \nthe need to know the underlying structure of the collection.")
print("To initialize an iterator object, you can use the iter() function. This function takes an iterable object as an argument and returns an iterator object.")
print("To iterate over the elements of the iterator, you can use the next() function. It retrieves the next element from the iterator. By calling next() repeatedly, you can iterate through all the elements of the iterator.")

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iterator = iter(my_list)

for _ in range(5):
    element = next(my_iterator)
    print(element)

#Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
#    function.

print("In Python, a generator function is a special type of function that generates a sequence of values using the yield keyword.")
print("he yield keyword is used within a generator function to indicate the value to be generated and returned to the caller.")


def fibo_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator object
fib_gen = fibo_generator()

# Generate and print the first 10 Fibonacci numbers
for _ in range(10):
    fibonacci_number = next(fib_gen)
    print(fibonacci_number)

#Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
#    first 20 prime numbers.

def prime_generator():
    primes = []
    num = 2
    while True:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
            if prime * prime > num:
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1

prime_gen = prime_generator()

for _ in range(20):
    prime_number = next(prime_gen)
    print(prime_number)
