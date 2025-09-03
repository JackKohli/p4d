# def counter():
#     counter = 0
#     while True:
#         yield counter
#         counter += 1

# for x in counter():
#     if x > 10:
#         break
#     print(x)

# # Challenge 1: My First Python Function

# # MVP

# # Write a function called my_first_function.
# # Your function should take in a string as an argument.
# # It should print in the format: "I love {argument}!".
 
# def my_first_function(s):
#     print(f"I love {s}")
 

 

# # MVP

# # Write a function tripler().
# # It should take in a number and return the number × 3.
# # Print the results with three different arguments.
 
# def tripler(x):
#     return x*3
# for x in range(1,4):
#     print(tripler(x))
 

# # Challenge 3: Greeter

# # MVP

# # Write a function greet() that takes a name as a parameter.
# # It should return "Hello, {name}!".
 
# def greet(name):
#     return f"Hello, {name}!"
 

# # Challenge 4: Even or Odd?

# # MVP

# # Write a function is_even() that takes a number as input.
# # Return "Even" if the number is even, "Odd" if it’s odd.
 
# def is_even(x):
#     return("Even", "Odd")[x&1]

# for x in range(10):
#     print(x, is_even(x))


# # Challenge 5: Word Multiplier

# # MVP

# # Write a function repeat_word(word, times)
# # It should return the word repeated times number of times.

# def repeat_word(s, x):
#     return s*x


# # Challenge 6: Factorial (Stretch)

# # MVP

# # Write a function factorial(n) that calculates the factorial of n.
# # Example: factorial(5) → 5 * 4 * 3 * 2 * 1 = 120.

# def factorial(n):
#     if n < 0:
#         print("must be positive")
#         return
#     if n == 0:
#         return 1
#     out = 1
#     while n:
#         out *= n
#         n -= 1
#     return out

from math import pi, sqrt
circle_area = lambda r: pi * r ** 2
print(circle_area(10))

triangle_area = lambda a,b,c: sqrt(((a+b+c)/2) * ((a+b+c)/2-a) ((a+b+c)/2-b) * ((a+b+c)/2-c))


nums = [x for x in range(10)]
print(list(filter(lambda x: x%2, nums)))
print(list(filter(lambda x: not x%2, nums)))


from functools import reduce

nums = [x for x in range(100)]
print(reduce(lambda a, b: a+b, nums))

nums = [2, 5, 7, 32, 100, 9, 56, 74, 97, 22, 13, 80]
odds = list(filter(lambda x: x&1, nums))
odds3 = list(map(lambda x: x*3, odds))
out = reduce(lambda x, y: x+y, odds3)
print(out)

