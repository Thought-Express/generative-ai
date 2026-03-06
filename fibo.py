def fibonacci_sequence(n):
    """Return the first n numbers in the Fibonacci sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def main():
    try:
        count = int(input("How many Fibonacci numbers should I generate? ").strip())
    except ValueError:
        print("Please enter a valid integer.")
        return

    sequence = fibonacci_sequence(count)
    print(sequence)


if __name__ == "__main__":
    main()
