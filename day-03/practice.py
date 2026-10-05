# ================================
# Day 3 Practice — if, elif, else
# Author: Tanim
# Date: 2026-10-07
# ================================

# ---------- 1. Positive / Negative / Zero ----------
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# ---------- 2. Largest of Three ----------
a = int(input("\nFirst number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")


# ---------- 3. Vowel or Consonant ----------
ch = input("\nEnter a letter: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


# ---------- 4. Login Check ----------
username = input("\nUsername: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Wrong credentials")


# ---------- 5. BMI Category ----------
weight = float(input("\nWeight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)
print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# ---------- 6. Nested if — Entry Check ----------
age = int(input("\nEnter your age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("Bring your ID")
else:
    print("Too young")


# ---------- 7. Weekend Check ----------
day = input("\nEnter day name: ")

if day == "Friday" or day == "Saturday":
    print("Weekend")
else:
    print("Weekday")


# ---------- 8. Working Age Check ----------
age = int(input("\nEnter your age: "))

if age >= 18 and age <= 60:
    print("Working age")
else:
    print("Not working age")
