import sys
import os
import math

def solve_quadratic(a, b, c):
    if a == 0:
        print("Error. coefficient a cannot be 0")
        sys.exit(1)

    print(f"Equation is: {a}x^2 + {b}x + {c} = 0")

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2*a)
        print("There are 1 roots")
        print(f"x1 = {x}")
    else:
        print("There are 0 roots")

def interactive_mode():
    def get_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError as e:
                print(f"Error. Expected a valid real number, got {str(e).split(':')[-1].strip()} instead")

    a = get_float("a = ")
    b = get_float("b = ")
    c = get_float("c = ")
    solve_quadratic(a, b, c)

def file_mode(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"file {filename} does not exist")

        with open(filename, 'r') as f:
            parts = f.readline().strip().split()
            if len(parts) != 3:
                raise ValueError("invalid file format")

            a, b, c = map(float, parts)
            solve_quadratic(a, b, c)

    except (FileNotFoundError, ValueError) as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: python equation.py [filename]")
        sys.exit(1)
