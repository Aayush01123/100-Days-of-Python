# break statement
<br>
The break statment enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

## Example:

```
for i in range(1,101,1):
    print(i, end=" ")
    if (i == 50):
        break
    else:
        print(Mississippi)
print("Thankyou")
```

## Output
```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
6 Mississippi
7 Mississippi
8 Mississippi
9 Mississippi
10 Mississippi
11 Mississippi
12 Mississippi
13 Mississippi
14 Mississippi
15 Mississippi
16 Mississippi
17 Mississippi
18 Mississippi
19 Mississippi
20 Mississippi
21 Mississippi
22 Mississippi
23 Mississippi
24 Mississippi
25 Mississippi
26 Mississippi
27 Mississippi
28 Mississippi
29 Mississippi
30 Mississippi
31 Mississippi
32 Mississippi
33 Mississippi
34 Mississippi
35 Mississippi
36 Mississippi
37 Mississippi
38 Mississippi
39 Mississippi
40 Mississippi
41 Mississippi
42 Mississippi
43 Mississippi
44 Mississippi
45 Mississippi
46 Mississippi
47 Mississippi
48 Mississippi
49 Mississippi
50 Thankyou
```


# Continue Statement
<br>
The continue statement skips the rest of the loop statemenrs and causes the next iteration to occur.

# Example:

```
for i in [2,3,4,8,0]:
    if (i%2!=0)
        continue
    print(i)
```

## Output
```
2
4
6
8
0
```

