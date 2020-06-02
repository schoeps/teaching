import sys

# read input
try:
    n = int(sys.argv[1])
except ValueError:
    print("Input is not an integer")
    exit

# Gauss' formula
gauss = 1

# print result
print(int(gauss))
