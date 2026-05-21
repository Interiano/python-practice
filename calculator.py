"""
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

#prints z to 2 decimal places
print(f"{z:.2f}")
"""

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
    