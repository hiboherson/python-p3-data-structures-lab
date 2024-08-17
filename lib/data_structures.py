def get_names(spicy_foods):
    """Retrieves names from a list of foods."""
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Returns foods with the highest heat level."""
    max_heat_level = max(food['heat_level'] for food in spicy_foods)
    return [food for food in spicy_foods if food['heat_level'] > 5]


def print_spicy_foods(spicy_foods):
    """Prints all foods with their names, cuisines, and heat levels formatted with 🌶 emojis."""
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        heat_level_emojis = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the food that matches the given cuisine."""
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None
def print_spiciest_foods(spicy_foods):
    """Prints foods with heat levels over 5 formatted with 🌶 emojis."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        heat_level_emojis = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_emojis}")



def get_average_heat_level(spicy_foods):
    """Calculates the average heat level of the foods."""
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    count = len(spicy_foods)
    return total_heat / count if count > 0 else 0

def create_spicy_food(spicy_foods, new_food):
    """Returns the original list of spicy foods with the new spicy food added."""
    spicy_foods.append(new_food)
    return spicy_foods
