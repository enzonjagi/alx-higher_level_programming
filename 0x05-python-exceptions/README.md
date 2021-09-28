# 0x05. Python - Exceptions
## General Objectives
<p> Why Python programming is awesome
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception.</p>

## Tasks
## 0. Safe list printing
<p>
Write a function that prints x elements of a list.

Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()

GitHub repository: ```alx-higher_level_programming```
Directory: ```0x05-python-exceptions```
File: ```0-safe_print_list.py```
</p>

# 1. Safe printing of an integers list
<p>
Write a function that prints an integer with "{:d}".format().

Prototype: def safe_print_integer(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to import any module
You are not allowed to use type()

GitHub repository: ```alx-higher_level_programming```
Directory: ```0x05-python-exceptions```
File: ```1-safe_print_integer.py```
</p>