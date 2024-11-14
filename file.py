import sys


def main():
    filename = input("Enter file name:")
    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                line = line.strip()
                parts = line.split()
                if len(parts) != 2:
                    print(f"Error: Line {line_number} does not contain exactly two values.")
                else:
                    try:
                        num1 = float(parts[0])
                        num2 = float(parts[1])
                        print(f"Line {line_number} sum: {num1 + num2}")
                    except ValueError:
                        print(f"Error: Line {line_number} contains non-numeric values.")
                line_number += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' cannot be opened.")
        sys.exit(1)


if __name__ == "__main__":
    main()
