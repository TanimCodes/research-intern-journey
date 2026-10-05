# ================================
# Day 2 Practice — Python Operators
# Author: Tanim
# Date: 2026-10-06
# ================================

# ---------- Arithmetic ----------
a = int(input("First number: "))
b = int(input("Second number: "))

print("Sum =", a + b)
print("Diff =", a - b)
print("Product =", a * b)
print("Division =", a / b)
print("Floor =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b)

# ---------- Comparison ----------
print(f"{a} == {b} → {a == b}")
print(f"{a} != {b} → {a != b}")
print(f"{a} > {b} → {a > b}")
print(f"{a} < {b} → {a < b}")
print(f"{a} >= {b} → {a >= b}")
print(f"{a} <= {b} → {a <= b}")

# ---------- Logical ----------
print(f"({a} > 5) and ({b} > 5) → {(a > 5) and (b > 5)}")
print(f"({a} > 5) or ({b} > 5) → {(a > 5) or (b > 5)}")

# ---------- Simple Calculator ----------
x = float(input("First: "))
y = float(input("Second: "))
op = input("Operator (+, -, *, /): ")

if op == "+":
    print("Result =", x + y)
elif op == "-":
    print("Result =", x - y)
elif op == "*":
    print("Result =", x * y)
elif op == "/":
    if y != 0:
        print("Result =", x / y)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# ---------- Largest of Two ----------
p = int(input("First: "))
q = int(input("Second: "))
if p > q:
    print(p, "is larger")
elif q > p:
    print(q, "is larger")
else:
    print("Both equal")

# ---------- Leap Year ----------
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# ---------- Grade Calculator ----------
marks = int(input("Enter marks: "))
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("F")
