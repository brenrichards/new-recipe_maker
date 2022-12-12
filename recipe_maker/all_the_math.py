class math_functions:
    def multiplier_definer(recipe_multiplier):
        if recipe_multiplier == 2:
            mult_string = "Recipe Doubled"
            return mult_string
        if recipe_multiplier == 3:
            mult_string = "Recipe Tripled"
            return mult_string
        if recipe_multiplier != 2 and recipe_multiplier != 3:
            str_recipe_mult = str(recipe_multiplier)
            mult_string = str_recipe_mult+"x "+"Recipe"
        return mult_string

    def wacky_fraction_maker(numerator, denominator, recipe_multiplier):
        new_numerator = recipe_multiplier * numerator

        if new_numerator < denominator:
            string_numerator = str(new_numerator)
            string_denominator = str(denominator)
            split_string_numerator = string_numerator.split(".")
            left_split_string_numerator = split_string_numerator[0]
            split_string_denominator = string_denominator.split(".")
            right_split_string_denominator = split_string_denominator[0]
            slash = "/"
            total = left_split_string_numerator+slash+right_split_string_denominator

        if new_numerator == denominator:
            total = "1"

        if new_numerator > denominator:
            float_number = new_numerator / denominator
            string_number = str(float_number)
            split_string_number = string_number.split(".")
            whole_number = split_string_number[0]
            decimal = split_string_number[1]
            remainder = ""
            # not very pretty, buuuuuut it works
            if decimal == "3333333333333333":
                remainder = "1/3"
            if decimal == "5":
                remainder = "1/2"           
            if decimal == "6666666666666666":
                remainder = "2/3"
            if decimal == "":
                remainder == ""
            if decimal == "0":
                remainder == ""
            
            if denominator == 1:
                remainder = ""
                total = whole_number
            else:
                total = whole_number+" "+remainder
            
        return total