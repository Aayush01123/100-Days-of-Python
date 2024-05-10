# Day3 - Comments, Escape sequence & Print in Python
<br>
Welcome to Day3 of 100 Days of Code. Today we will talk about Comments, Escape Sequences and little bit more about print statement in Python. We will also throw some light on Escape Sequence.

# Python Comments
<br>
A comments is a part of the coding file that the programmer does not want to execute, rather the programmer uses to either explain a block of code or to avoid the execution of a specific part of code while testing.

# Single-Line Comments:
<br>

To write a command just add a "#" at the start of the line.

Example 1

```
#This is a 'Single-Line Comments'
print("This is a print statement)
```

Output:
```
This is a print statement
```

# Multi-Line Comments:
To write multi-line comments you can use '#' at each line or you can use the multiline string

```
''''
Hey Aayush, Please Dont remove this line
'''
```

# Escape Sequence Characters
<br>
To insert characters that cannot to directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash ```\ ``` followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
```
print("This doesnt "execute")
print("This will \" execute")
```

# More on Print statement
The syntax of a print statement looks something like this:

```
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

# Other Parameters of Print Statement

1. object(s): Any object and as many as you like. Will be converted to strings before printed

2. sep='separator': Specify how to separate the objects, if there is more than one. Default is''

3. end='end':Specify what to print at the end. Default is '\n' (line feed)

4. file: An object with a write method. default is sys.stdout

### Parameters 2 to 4 are optional



