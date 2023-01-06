#!/usr/bin/python3
if __name__ == "__main__":

    import sys
# Initialize the sum to 0
    sum = 0
# Iterate over the arguments and add them to the sum
    for arg in sys.argv[1:]:
        sum += int(arg)
# Print the sum
    print("{}".format(sum))
