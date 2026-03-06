import math

def print_pi_digits(n=4):
    """
    Prints the first n digits of pi.
    By default, it prints the first 4 digits.
    """
    if not isinstance(n, int) or n <= 0:
        print("Please provide a positive integer for the number of digits.")
        return

    # Get pi as a string with enough precision.
    # We add 2 to n to account for "3." and the decimal point itself.
    # For example, if n=4, we want "3.1415". The length of this string is 6.
    # So, precision should be n+1 to get 'n' digits after the decimal point
    # or n+2 if we count the initial '3' and '.'
    # A format like f"{math.pi:.{n}f}" would give n digits after the decimal point.
    # Let's try to construct the string properly.

    pi_str = str(math.pi)

    if n == 1:
        print(pi_str[0])
    elif n > 1:
        # We want '3' + 'n' digits after the decimal point
        # pi_str[0] is '3'
        # pi_str[1] is '.'
        # pi_str[2:2+n] will give n digits after the decimal point
        if len(pi_str) >= 2 + n:
            print(pi_str[0] + pi_str[2:2+n])
        else:
            # If the string representation of math.pi is not long enough for n digits,
            # we can try to use f-string formatting with higher precision.
            # This is safer to ensure we get enough digits.
            # For n digits, we need '3.' followed by n digits. So total n+2 characters.
            # The precision in f-string is for digits after decimal.
            # So, f"{math.pi:.{n}f}" will give 'n' digits after the decimal point.
            formatted_pi = f"{math.pi:.{n}f}"
            print(formatted_pi[0] + formatted_pi[2:])
    else:
        print("Please provide a positive integer for the number of digits.")


if __name__ == "__main__":
    print("First 4 digits of pi (default):")
    print_pi_digits()

    print("\nFirst 10 digits of pi:")
    print_pi_digits(10)

    print("\nFirst 1 digit of pi:")
    print_pi_digits(1)

    print("\nFirst 0 digits of pi (should show error):")
    print_pi_digits(0)

    print("\nFirst -5 digits of pi (should show error):")
    print_pi_digits(-5)

    print("\nFirst 'a' digits of pi (should show error):")
    print_pi_digits('a')
