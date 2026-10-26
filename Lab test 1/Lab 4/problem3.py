base = float(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

print("Using ** operator:", base ** exp)

# Using a loop (for non-negative exponents)
result = 1
for _ in range(exp):
    result *= base
print("Using loop:", result)
