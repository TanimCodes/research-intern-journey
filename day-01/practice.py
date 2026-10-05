# ================================
# Day 1 Practice — Python Basics
# Author: Tanim
# Date: 2026-10-05
# ================================

# ---------- 1. print() ----------
print("Hello, World!")
print("My name is Tanim")
print("I am a CSE student at IIUC")
print(22)

# ---------- 2. Variable ----------
name = "Tanim"
age = 22
cgpa = 3.50
is_student = True
print(name, age, cgpa, is_student)

# ---------- 3. Data Types ----------
print(type(10))
print(type(3.14))
print(type("Hello"))
print(type(True))

# ---------- 4. input() ----------
your_name = input("Enter your name: ")
print("Hello,", your_name)

# ---------- 5. Type Conversion ----------
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print("Sum =", num1 + num2)
print("Average =", (num1 + num2) / 2)

# ---------- 6. Even / Odd ----------
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# ---------- 7. Area of Rectangle ----------
length = float(input("Length: "))
width = float(input("Width: "))
print("Area =", length * width)
