# Functions in Python
<br>
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing function that make the program flow organized and neat.

### There are two types of functions:
<br>

1. Built-in functions
2. user-defined functions

## Built-in functions:

<br>
These functions are defined and pre-coded in python. Some example of built-in function are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

## User-defined functions:

<br>
We can create functions to perform specific tasks as per needs. Such functions are called user defined functions.

## Syntax:

```
def function_name(parameters):
    pass
    # Code and Statements
```

- Create a function using the def keyword, followed by a function name, followed by a paranthesis (0) and a colon(:)
- Any parameters and arguments should be placed within the parantheses.
- Rules to naming function are similar to that of naming variables.
- Any statements and other code within the function should be indented.

## Calling a function:

<br>

We call a function by giving the function name, followed by parameter (if any) in the parenthesis.

### Example:

```
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
```

### Output

```
Hello, San Wilson
```
