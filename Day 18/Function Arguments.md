# Function Arguments and return statement

<br>
There are four types of arguments that we can provide in a function:

- Default Arguments
- keyword Arguments
- Variable length Arguments
- Required Arguments

# Default Arguments

<br>
We can set a default value for a function's parameter. This way, if no value is provided for that parameter when the function is called, the function will use the default value.

## Example:

```
def name(fname mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
```

## Output

```
Hello, Amy Jhon Whatson
```

# Keyword arguments:

<br>
We can use key = value to pass arguments to a function. This way, the interpreter knows which argument belongs to which parameter by name, so the order of the arguments doesn't matter

## Example:

```
def name(fname, mname, lname):
    print("Hello", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
```

# Output:

```
Hello, Jade Peter Wesker
```

# Required Arguments:

<br>
If we don't use the key = value syntax, we must pass the arguments in the correct order, and the number of arguments must match the function's definition.

Example 1: when number of arguments passed does not match to the actual function defination.

```
def name(fname, mname, lname):
    print("Hello,",fname, mname, lname)

name("Peter","Quill")
```

# Variable-length arguments:

<br>
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable length arguments.

## There are two ways to achieve this:

<br>

### Arbitary Arguments:

While creating a function, pass a \* before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple

## Example:

```
def name(*name):
    print("Hello", name[0], name[1], name[2])

name("James","Buchanan","Barnes")
```

# keyword Arbitary Arguments:

While creating a function, pass a \* before the parameter name while defining the function. The function accesses the arguments by procesing them in the form of dictionary.

## Example:

```
def name(**name):
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "Bahadur", lname = "Karki", fname ="James")
```

## Output:

```
Hello James Bahadur Karki
```

# return Statement

<br>
The return statement is used to return the value of the expression back to the calling function.

```
def name(fname, mname, lname):
    return "hello," + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
```
