# Nested if statements
<br>
We can use if-else, elif statement inside other if statementas well

## Example:

```
num = 18
num = 0
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10") 
    elif (num > 10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")  
```

