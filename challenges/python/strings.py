import sys

# Grab the first input which is not the filename
first_arg = sys.argv[1]
# Convert string to UPPER CASE
first_arg = first_arg.upper()
# Append 3 exclamation points
first_arg = first_arg + "!!!"

print(first_arg)
