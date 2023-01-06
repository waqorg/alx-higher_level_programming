#!/usr/bin/python3
if __name__ == "__main__":
    import sys

# Print the number of arguments
    print("{:d} arguments:", len(sys.argv) - 1)

# Print the list of arguments with numbers
    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, arg))
