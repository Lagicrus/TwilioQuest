# Create the function
# Which accepts a optional variable


def hail_friend(name: str = ""):
    # If name is still "empty" (first mission which needs this file)
    if len(name) == 0:
        # Print required text
        print("Hail, friend!")
    else:
        # Print text with name variable
        print(f"Hail, {name}")


# Declare a function which has 2 arguments which have no default value and are type hinted as integers
def add_numbers(first_int: int, second_int: int):
    # Return first plus second
    return first_int + second_int
