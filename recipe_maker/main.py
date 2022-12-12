from get_inputs import GetInputFunctions
from all_the_math import MathFunctions
from strings import ParseAndEditStrings

def main():
    recipe_entered = GetInputFunctions.enter_ingredients()
    recipe_multiplier = GetInputFunctions.whole_numbers_only()
    doubling_statement = MathFunctions.multiplier_definer(recipe_multiplier)
    print(doubling_statement)
 
    recipe_length = len(recipe_entered)
 
    for x in range(0, recipe_length):
        final_string = ParseAndEditStrings.main_loop_function(recipe_length, recipe_entered, recipe_multiplier, x)
        print(final_string)

if __name__ == "__main__":
    main()