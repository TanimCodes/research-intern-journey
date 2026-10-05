# ================================
# Day 4 Practice — for loop, while loop
# Author: Tanim
# Date: 2026-10-08
# ================================

# ---------- 1. 1 থেকে 10 print ----------
print("--- 1 to 10 ---")
for i in range(1, 11):
    print(i)


# ---------- 2. জোড় সংখ্যা ----------
print("\n--- Even numbers 1-20 ---")
for i in range(2, 21, 2):
    print(i)


# ---------- 3. যোগফল ----------
print("\n--- Sum 1 to 100 ---")
total = 0
for i in range(1, 101):
    total = total + i
print("Sum =", total)


# ---------- 4. Factorial ----------
print("\n--- Factorial ---")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial =", fact)


# ---------- 5. Multiplication Table ----------
print("\n--- Multiplication Table ---")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# ---------- Extra: while loop ----------
print("\n--- While loop: 5 to 1 ---")
i = 5
while i >= 1:
    print(i)
    i = i - 1


# ---------- Extra: break ----------
print("\n--- Break at 5 ---")
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# ---------- Extra: continue ----------
print("\n--- Skip 3 ---")
for i in range(1, 7):
    if i == 3:
        continue
    print(i)
