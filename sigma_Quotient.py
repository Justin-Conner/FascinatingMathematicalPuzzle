def sigma(n):
    """Sum of all positive divisors of n."""
    if n <= 0:
        return 0
    s, i = 0, 1
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    return s

def f(n):
    """f(n) = σ(n-3) rounded to nearest 10."""
    raw = sigma(n - 3)
    return round(raw / 10) * 10

# Verify original examples still work
print("Verifying original examples:")
print(f"  f(30) = {f(30)}")
print(f"  f(27) = {f(27)}")

# Get user input
print()
while True:
    try:
        N = int(input("Enter a number between 1 and 1,000,000,000: "))
        if 1 <= N <= 1_000_000_000:
            break
        else:
            print("  Out of range. Please try again.")
    except ValueError:
        print("  Invalid input. Please enter a whole number.")

# Calculate and display
result   = f(N)
quotient = result // 10
last     = quotient % 10

print(f"\n  N              = {N:,}")
print(f"  σ(N-3) raw     = {sigma(N-3):,}")
print(f"  f(N) rounded   = {result:,}")
print(f"  f(N) // 10     = {quotient:,}")
print(f"  Last digit     = {last}")
print(f"\n  ✅ f({N:,}) = {result:,} always ends in 0")
print(f"     Third example: when n = {N:,}, f(n) = {result:,}")
