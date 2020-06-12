import sys

# For every item in the arguments that were piped into the file
# Besides the FIRST as that is the file name
# Start at 1 in the count (otherwise it is 0)
for index, item in enumerate(sys.argv[1:], start=1):
    # Print the index and item from above in a formatted string
    print(f"{index}. {item}")
