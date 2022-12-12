from get_inputs import get_input_functions
from all_the_math import math_functions
from strings import parse_and_edit_strings
from get_inputs import get_input_functions

def main():
    recipe_entered = get_input_functions.enter_ingredients()
    recipe_multiplier = get_input_functions.whole_numbers_only()
    doubling_statement = math_functions.multiplier_definer(recipe_multiplier)
    print(doubling_statement)
 
    recipe_length = len(recipe_entered)
 
    for x in range(0, recipe_length):
        final_string = parse_and_edit_strings.main_loop_function(recipe_length, recipe_entered, recipe_multiplier, x)
        print(final_string)

if __name__ == "__main__":
    main()