import math

def print_pi_digits(n=4):
    """
    Prints the first n digits of pi.
    Defaults to 4 digits if n is not provided.
    """
    print(f"The first {n} digits of pi are: {math.pi:.{n}f}")

if __name__ == "__main__":
    print_pi_digits()
