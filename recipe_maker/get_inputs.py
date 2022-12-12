class GetInputFunctions:
    def enter_ingredients():
        print(f"Please enter your first ingredient")
        print(f"Enter Ingredients in the form '1/2 cup flour' or '2 tbsp oil'")
        print(f"To stop adding ingredients, enter END")
        repeat = "true"
        list_of_ingredients = []
        fakelist = []
        fakelist2 = []
        check_if_valid_fraction = "true"
        check_if_valid_number = "true"
        while repeat == "true":
                ingredient = input("").lower()

                if ingredient.lower() == "end":
                    break
                
                list_of_ingredients.append(ingredient)
        return list_of_ingredients


    def whole_numbers_only():
        while True:
            try:
                recipe_multiplier = int(input("What would you like to multiply this recipe by? "))
            except ValueError:
                print(f"Please Enter a Whole Number")
                continue
            else:
                return recipe_multiplier
                break