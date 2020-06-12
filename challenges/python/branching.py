import sys

# Read the first second and third argument
# Convert to a int
# We don't read the first argument as that is the filename
first = int(sys.argv[1])
second = int(sys.argv[2])

# Equal or smaller than 0
if first + second <= 0:
    print("You have chosen the path of destitution")
# This is a simple way to get a list of ints of 1 through to 100
# [1,2,3,4...100]
elif first + second in list(range(1, 101)):
    print("You have chosen the path of plenty")
# If total bigger than 100
elif first + second > 100:
    print("You have chosen the path of excess")
