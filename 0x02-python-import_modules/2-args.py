#!/usr/bin/python3
if __name__ == "__main__":
    import sys

# Print the number of arguments
    print(len(sys.argv) - 1, "arguments:")

# Print the list of arguments with numbers
    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, arg))
