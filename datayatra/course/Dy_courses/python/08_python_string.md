# 🧵 Python Strings

## 🧬 Python String Essentials
Strings in Python are sequences of characters enclosed in either single quotes `'` or double quotes `"`. They are used to represent text and are one of the most commonly used data types in Python.

## 🧠 Creating Strings
You can create a string by simply assigning text to a variable using quotes.

> Example

>```python
>name = "Python"
>greeting = 'Hello, World!'
>```
## 🔁 Multiline Strings
Use triple quotes ''' or """ to create strings that span multiple lines.

> Example

>```python
> message = """This is
>a multiline
>string."""
>```
## 🔤 String Indexing
Each character in a string has an index, starting from 0.
> Example

>```python
>text = "Python"
>print(text[0])  # Output: P
>print(text[3])  # Output: h
>```
## ✂️ String Slicing
You can extract parts of a string using slicing.
> Example

>```python
>text = "Python"
>print(text[0:4])  # Output: Pyth
>print(text[:3])   # Output: Pyt
>print(text[2:])   # Output: thon
>```
## 🛠️ String Method
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `lower()`   | Converts all characters to lowercase |
| `upper()`   | Converts all characters to uppercase |
| `strip()`   | Removes whitespace from both ends    |
| `replace()` | Replaces a substring                 |
| `split()`   | Splits string into a list            |

> Example

>```python
>text = " Hello, Python! "
>print(text.strip())       # Output: Hello, Python!
>print(text.lower())       # Output:  hello, python!
>print(text.replace("Python", "World"))  # Output: Hello, World!
>```
## ➕ String Concatenation
Use the + operator to join strings.
>Example

>```python
>first = "Hello"
>second = "World"
>print(first + " " + second)  # Output: Hello World
>```

## 🧮 String Formatting
Python provides several ways to format strings.

>Example

>```python
>name = "Alice"
>age = 25
># Using f-strings (recommended)
>print(f"My name is {name} and I am {age} years old.")
># Using format() method
>print("My name is {} and I am {} years old.".format(name, age))
>```

## 🎥 Youtube
![youtube]()

