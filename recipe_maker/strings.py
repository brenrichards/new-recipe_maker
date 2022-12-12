from all_the_math import MathFunctions

class ParseAndEditStrings:
    def recipe_parsing(list_of_ingredients, list_number):
        select = list_of_ingredients[list_number]
        split_ingredient = select.split(" ")
        # Split_ingredient is a list of the components of an ingredient
        
        return split_ingredient
    
    def final_ingredient_string_maker(parsed_components, new_measurement_amount):
        unit = parsed_components[1]

        try:
            ingredient = parsed_components[2]
        except IndexError:
            ingredient = ""

        final_string = new_measurement_amount+" "+unit+" "+ingredient

        return final_string

    def main_loop_function(recipe_length, recipe_entered, recipe_multiplier, x):
        parsed_components = ParseAndEditStrings.recipe_parsing(recipe_entered, x)
        fraction_of_component = parsed_components[0]
        split_fraction = fraction_of_component.split("/")
        numerator = float(split_fraction[0])
        try:
            denominator = float(split_fraction[1])
        except IndexError:
            denominator = 1

        new_measurement_amount = MathFunctions.wacky_fraction_maker(numerator, denominator, recipe_multiplier)

        final_string = ParseAndEditStrings.final_ingredient_string_maker(parsed_components, new_measurement_amount)
        
        return final_string
