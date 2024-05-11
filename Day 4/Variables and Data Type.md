# Day 6 - Variables and Data Types
<br>

# What is variable?
<br>
Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc. Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing.

```
a =1
b = True
c = "Harry"
d = None
```
These are four variables of different data types.

# What is a Data Type?
<br>
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the ype of any operator using type function:
```
a = 1
print(type(a))
b = "1"
print(type(b))
```

# 1 Numeric data: int, float, complex
<br>
- int: 3, -8,, 0
- float: 7.349, -9.0, 0.0000001
- complex: 6 + 2i

# 2. Text data: str
<br>
str: "Hello World", "Python Programming"

# 3. Boolean Data:
<br>
Boolean data consists of values True or False.

# 4. Sequenced data: list,tuple
<br>
**list**: A list is an ordered collection of data with elements seperated by a comma and enclosed within square brackets. List are mutable and can be modified after creation

**Example**
```
list1 = [8, 2,3, [-4, 5], ["aaple", "banana"]]
print(list1)
```
**Output**
```
[8, 2,3, [-4, 5], ["aaple", "banana"]]
```
**Tuple**: A tuple is an ordered collection of data with elements seperated by a comma and enclosed with parentheses. Tuples are immutable and can not be modified after creation.
**Example**

```
tuple1 = (("parrot","sparrow"), ("Lion", "Tiger))
print(tuple1)
```
**Output**
```
(("parrot","sparrow"), ("Lion", "Tiger))
```

# 5. Mapped data: dict
**dict**: A dictionary is an unorderd collection of data containing a key: value pair. The key: value paris are enclosed within curly brackets.

**Example:**
```
dict1 = {"name":"Aayush", "age":20, "canVote": True}
print(dict1)







