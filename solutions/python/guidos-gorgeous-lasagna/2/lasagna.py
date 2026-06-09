"""Functions used in preparing Guido's gorgeous lasagna."""
#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time #calculating time remaining 
print(f"Bake time remaining: {bake_time_remaining(10)} minutes")

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers."""
    return PREPARATION_TIME * number_of_layers #calculating preparation time based on number of layers
print(f"Preparation time: {preparation_time_in_minutes(3)}minutes")

#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes based on the number of layers and the bake time already elapsed."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time #calculating total elapsed time
print(f"Elapsed time: {elapsed_time_in_minutes(3, 20)} minutes")


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
