# Lambda is an anonymous function in Python. It is a small, unnamed function that can take any number of arguments but can only have one expression. The syntax for a lambda function is as follows:
# lambda arguments: expression

square = lambda x: x ** 2 # Not recommended to assign a lambda function to a variable, as it defeats the purpose of using a lambda function. It is better to use a regular function definition for this case.
print(square(5))  # Output: 25

# Lambda functions are often used in conjunction with higher-order functions like map(), filter(), and reduce(). For example, you can use a lambda function to square each element in a list using the map() function:
numbers = [1, 2, 3, 4, 5]   # Can be used for tuples and sets as well
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# You can also use a lambda function directly within the map() function without assigning it to a variable:
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Lambda functions can also be used with the filter() function to filter elements from a list. For example, you can use a lambda function to filter out even numbers from a list:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Can be used for tuples and sets as well
print(even_numbers)  # Output: [2, 4]

# Lambda functions can also be used with the reduce() function from the functools module to perform a cumulative operation on a list. For example, you can use a lambda function to calculate the product of all elements in a list:
from functools import reduce # Reduce is a function that applies a rolling computation to sequential pairs of values in a list. It is used to perform a cumulative operation on a list, such as summing or multiplying all elements.
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Lambda functions are also commonly used in situations where a function is required as an argument, such as in sorting or when working with data structures like lists and dictionaries. For example, you can use a lambda function to sort a list of tuples based on the second element:
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1]) # By default, sorted() sorts based on the first element of the tuple, but by using a lambda function as the key, we can specify that we want to sort based on the second element (the fruit name).
print(sorted_data)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]


def apply_function(x, func):
    return func(x)
result = apply_function(5, lambda x: x ** 3)
print(result)  # Output: 125


def calculate(a, b, operation):
    return operation(a, b)
print(calculate(10, 5, lambda x, y: x + y))  # Output: 15
print(calculate(10, 5, lambda x, y: x * y))  # Output: 50


def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result
numbers = [1, 2, 3, 4, 5]
squared_numbers = my_map(lambda x: x ** 2, numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# filter() with None - try filtering out falsy values from a list using filter() with None as the function argument. Falsy values include None, False, 0, empty strings, and empty collections.
values = [0, 1, False, 2, '', 3, None, 4, [], 5]
filtered_values = list(filter(None, values))
print(filtered_values)  # Output: [1, 2, 3, 4, 5]

# Multiple-argument lambda with map() - use a lambda function with multiple arguments in conjunction with the map() function to perform an operation on two lists. For example, you can add corresponding elements from two lists together.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed_lists = list(map(lambda x, y: x + y, list1, list2))
print(summed_lists)  # Output: [5, 7, 9]




# Question 1: Use a lambda function with filter() to extract all words longer than 4 characters from a list of words.
words = ['apple', 'banana', 'cat', 'dog', 'elephant']
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)  # Output: ['apple', 'banana', 'elephant']

# Question 2: Use a lambda with sorted() to sort a list of dictionaries based on a specific key.
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key = lambda x: x["age"])
print(sorted_people)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Question 3: Use a lambda function with reduce() to find the maximum value in a list of numbers.
import functools
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
maximum = functools.reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # Output: 9

# Question 4: Use map() with a lambda function to convert a list of temperatures from Celsius to Fahrenheit.
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda x: round((1.8 * x) + 32, 2), celsius))
print(fahrenheit)  # Output: [32.0, 68.0, 98.6, 212.0]

# Question 5: Use a lambda with sorted() to sort a list of tuples based on the second element in descending order.
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_data = sorted(data, key = lambda x: x[1], reverse = True)
print(sorted_data)  # Output: [(3, 'cherry'), (2, 'banana'), (1, 'apple')]