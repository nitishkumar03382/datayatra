# 🔀 Conditional Statements in Python

## 🧠 What are Conditional Statements?

Conditional statements in Python allow you to execute certain pieces of code based on whether a condition is **True** or **False**. These statements help your program make decisions.

---

## 🧩 Types of Conditional Statements

### 1. ✅ `if` Statement

The `if` statement runs a block of code **only if** the condition is true.

> Example

>```python
>age = 18
>
>if age >= 18:
>   print("You are eligible to vote.") 
>```

**Output**

>```
> You are eligible to vote
>```
### 🔁 if...else Statement 
The `if...else` statement runs one block if the condition is true, another if it’s false.

> Example

>```python
>age = 16
>
>if age >= 18:
>    print("You are eligible to vote.")
>
>else:
>    print("You are not eligible to vote.")    
>```

**Output**

>```
> You are not eligible to vote
>```
### 🔄 if...elif...else Statement
Use `elif` (else if) to check multiple conditions in order.

> example

>```python
>marks = 75
>
>if marks >= 90:
>    print("Grade: A")
>elif marks >= 75:
>    print("Grade: B")
>elif marks >= 60:
>    print("Grade: C")
>else:
>    print("Grade: D")  
>```

**Output**

>```
> Grade: B
>```
### 🔁 Nested if Statement
You can put one `if` inside another.

> Example

>```python
>x = 20
>
>if x > 10:
>    if x < 30:
>        print("x is between 10 and 30")
>```

**Output**

>```
> x is between 10 and 30
>```

## 🎥 YouTube

![youtube]()

