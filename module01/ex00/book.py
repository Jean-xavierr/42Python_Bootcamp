from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.creation_date = datetime.now().ctime()
        self.last_update = self.creation_date
        self.recipes_list = {'starter': [],
                             'lunch': [],
                             'dessert': []}

    def get_recipe_by_name(self, name) -> object:
        for lst_meal in self.recipes_list.values():
            for recipe in lst_meal:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Error: recipe doesn't exist.")
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list.keys():
            print('Error: send an existing recipe_type ["starter", "lunch", '
                  + '"dessert"]')
            return None
        lst_all_recipe = []
        for recipe in self.recipes_list[recipe_type]:
            lst_all_recipe.append(recipe)
        return lst_all_recipe

    def add_recipe(self, recipe) -> None:
        if not isinstance(recipe, Recipe):
            print('Error: send an instance of Recipe.')
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now().ctime()
