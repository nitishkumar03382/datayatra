# 📘 Python Data Types

## 📘 What are Data Types?
In Python, every value has a data type. A data type defines the kind of data a variable can hold, such as numbers, text, or lists. Understanding data types is essential for writing correct and efficient Python code.

---

## 🔢 Built-in Data Types in Python

Python has several built-in data types, which are categorized as follows:

### 🔣 Text Type
- **`str`** – A string, or sequence of Unicode characters.

> Example

>```python
>name = "Alice"     # "Alice"= string
>```

### 🔢 Numeric Types
- `int` – Integer numbers (whole numbers)

- `float` – Decimal numbers

- `complex` – Complex numbers (with imaginary part)
> Example

>```python 
>age = 25        # This is int
>price = 49.99   # This is float
>z = 3 + 5j      # This is complex
>```
### 🔘 Boolean Type
- `bool` – Represents `True` or `False`
> Example

>```python
>is_active = True  #This is bool
>```
### 📦 Sequence Types
- `list` – An ordered, changeable collection

- `tuple` – An ordered, unchangeable collection

- `range` – A sequence of numbers
> Example

>```python
>fruits = ["apple", "banana", "cherry"] # This is list
>coordinates = (10, 20)    # This is tuple
>numbers = range(5)        # This is range
>```
### 🗂️ Mapping Type
- `dict` – A collection of key-value pairs
>Example

>```python
>person = {"name": "Alice", "age": 25} # Thi is dict
>```
### 📚 Set Types
- `set` – An unordered collection of unique items

- `frozenset` – An immutable set

>Example

>```python
>colors = {"red", "green", "blue"} # This is set
>frozenset({"red", "green", "blue"}) # This is frozenset
>```
### 💾 Binary Types
- `bytes`

- `bytearray`

- `memoryview`
>Example

>```python
>data = b"Hello"  # This is bytes
>x = bytearray(5) # This is bytearray
>y = memoryview(bytes(5))  # This is memoryview
>```
### 🔄 casting type
- **int()** - Converts compatible values to an integer.
- **float()** - Transforms values into floating-point numbers.
- **str()** - Converts any data type into a string.
> Example

>```python
>a = "20"  # Initially a string
>b = int(a)  # Cast string to integer
>
>print(b)       
>print(type(b)) 
>```

**Output**

>```
> 20
> <class 'int'>
>```
### 🔍 Check Data Type
You can use the `type()` function to check the data type of a value.
>Example

>```python
>x = 10
>print(type(x)) 
> 
>name="data"
>print(type(name)) 
>
>y = 6.4
>print(type(y))  
>```

**Output**

>```
> <class 'int'>
> <class 'str'>
> <class 'float'>
>```

## 📺 Youtube
![youtube]()



