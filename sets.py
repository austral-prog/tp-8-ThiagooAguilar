def clean_ingredients(dish_name, dish_ingredients):
    ingredients = set(dish_ingredients)
    return dish_name, ingredients


def check_drinks(drink_name, drink_ingredients):
    alcohols = {"whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch", "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco", "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur", "almond liqueur", "champagne", "orange curacao", "rum"}
    ingredients = set(drink_ingredients)
    intereseccion = ingredients.intersection(alcohols)
    if len(intereseccion) == 0:
        return f"{drink_name} Mocktail"
    else:
        return f"{drink_name} Cocktail"
