import sys

# For every item in the arguments that were piped into the file
# Besides the FIRST as that is the file name
for item in sys.argv[1:]:
    # Convert to a int
    item = int(item)
    # If the reminder from doing MOD on 3 AND 5 is 0
    if item % 3 == 0 and item % 5 == 0:
        print("fizzbuzz")
    # If the reminder from doing MOD on 3 is 0
    # (elif is shorthand for else if)
    elif item % 3 == 0:
        print("fizz")
    # If the reminder from doing MOD on 5 is 0
    # (elif is shorthand for else if)
    elif item % 5 == 0:
        print("buzz")
    # Else nothing else
    else:
        print(item)
