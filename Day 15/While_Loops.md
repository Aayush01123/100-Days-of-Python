# Python while Loop

<br>
As the name suggests while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes of the while loop.

## Example:
<br>

```
count = 5 
while (count > 0):
    print(count)
    count = count - 1
```

## Output
<br>

```
5
4
3
2
1
```
Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the count variable (the variable count, in our case) or the loop will continue forever.

# Else with While Loop 
<br>
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

## Example:

```
x = 5
while (x > 0):
    print(x)
    x = x -1
else:
    print("I am inside else")
```

## Output:

```
5
4
3
2
1
I am inside else
```