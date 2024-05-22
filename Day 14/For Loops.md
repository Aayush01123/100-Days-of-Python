# loops in python
<br>
Sometimes a programmer wants to create a group of statement a certain number of times. This can be done using loops. 

Based on this loops are further classified into following types: 

1. For Loop
2. while Loop
3. nested loops

# The For Loop
<br>
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# Example: iterating over a string

```
name = "Aayush"
for i in name:
    print(i, end=", ")
```

## Output

```
A,b,h,i,s,h,e,k
```

## Example: iterating over a list:

```
colors = ["Red","Green","Blue","Yellow"]
for x in colors:
    print(x)
```

## Output

```
Red
Green
Blue
Yellow
```

Similarly, we can loops for lists, sets and dictionaries.

# range():
<br>
What if we do not want iterate over a sequence?

What if we want to use for loop for a specific number of times?

## Example:

```
for k in range(5):
    print(k)
```

# Output
```
0
1
2
3
4
```

## Quick Quiz
Explore about third parameter of range 9i.e range(x,y,x)