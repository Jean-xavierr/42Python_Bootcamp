class Recipe:
    def __init__(self, name, cooking_lvl,
                 cooking_time, ingredients, description, recipe_type) -> None:
        if self.check_data(name, cooking_lvl, cooking_time, ingredients,
                           description, recipe_type):
            return None

        self.name:          str = name
        self.cooking_lvl:   int = cooking_lvl
        self.cooking_time:  int = cooking_time
        self.ingredients:   list = ingredients
        self.description:   str = description
        self.recipe_type:   str = recipe_type

    def check_data(self, name, cooking_lvl, cooking_time,
                   ingredients, description, recipe_type) -> None:
        error = True
        list_recipe_type = ['starter', 'lunch', 'dessert']
        if (not isinstance(cooking_lvl, int) or not
           isinstance(cooking_time, int)):
            print("Error: cooking_lvl or" +
                  "cooking_time isn't a positive number.")
        elif cooking_lvl < 1 or cooking_lvl > 5:
            print("Error: cooking_lvl isn't in range 1 to 5.")
        elif int(cooking_time) < 1:
            print("Error: cooking_time >= 1min.")
        elif not ingredients:
            print("Error: ingredients can't empty.")
        elif recipe_type not in list_recipe_type:
            print("Error: recipe_type isn't a starter, lunch or dessert.")
        else:
            error = False
        return error

    def __str__(self):
        txt = (f"Recipe name:  {self.name}\n"
               f"Cooking lvl:  {self.cooking_lvl}\n"
               f"Cooking time: {self.cooking_time}\n"
               f"Ingredients:  {self.ingredients}\n"
               f"Description:  {self.description}\n"
               f"Recipe type:  {self.recipe_type}")
        return txt
