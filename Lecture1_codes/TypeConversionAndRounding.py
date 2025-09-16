# TypeConversionAndRounding.py
import math

print("=== Implicit Type Conversion (Type Promotion) ===")
x = 5
y = 2.0
z = x + y
print("5 + 2.0 =", z, " (type:", type(z), ")")

c = 2 + 3j
print("5 + (2+3j) =", 5 + c, " (type:", type(5 + c), ")")
print()

print("=== Explicit Type Conversion (Casting) ===")
print("int(3.9) =", int(3.9))
print("float(7) =", float(7))
print("str(123) =", str(123))
print()

print("=== Rounding with round() ===")
print("round(3.456) =", round(3.456))
print("round(3.456, 2) =", round(3.456, 2))
print("round(2.5) =", round(2.5))
print("round(3.5) =", round(3.5))
print()

print("=== math.floor() and math.ceil() ===")
print("math.floor(3.9) =", math.floor(3.9))
print("math.ceil(3.1) =", math.ceil(3.1))
print()

print("=== Truncation with int() ===")
print("int(3.9) =", int(3.9))
print("int(-3.9) =", int(-3.9))