# hello.py
import numpy as np


def greet(name):
    return f"Hello, {name}! Welcome to Python with NumPy!"


def demonstrate_numpy():
    """Show basic numpy functionality"""
    # Create an array
    numbers = np.array([1, 2, 3, 4, 5])

    print(f"\nArray: {numbers}")
    print(f"Mean: {numbers.mean()}")
    print(f"Sum: {numbers.sum()}")
    print(f"Standard Deviation: {numbers.std():.2f}")

    # Create a 2D array
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\nMatrix:\n{matrix}")
    print(f"Matrix shape: {matrix.shape}")


def main():
    print("=== Python with NumPy ===")
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)

    demonstrate_numpy()

    # Do a simple calculation
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")


if __name__ == "__main__":
    main()
