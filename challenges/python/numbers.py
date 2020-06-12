import sys

# This code reads in arguments and converts those inputs to decimal numbers
# We start at 1 as 0 is the file
first_number = float(sys.argv[1])
second_number = float(sys.argv[2])

# Add the two together
result_sum = first_number + second_number
# Take the second from the first
result_difference = first_number - second_number
# Multiply first by the second
result_product = first_number * second_number
# Divide the first by the second
result_quotient = first_number / second_number
