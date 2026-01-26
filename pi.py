import math

def print_pi_digits(n=4):
    """
    Prints the first n digits of pi.
    By default, it prints the first 4 digits after the decimal point.
    """
    if not isinstance(n, int) or n < 0:
        print("Please provide a non-negative integer for the number of digits.")
        return

    # Print pi formatted to n decimal places
    print(f"Pi to {n} digits: {{:.{n}f}}".format(math.pi))

if __name__ == "__main__":
    print_pi_digits()
