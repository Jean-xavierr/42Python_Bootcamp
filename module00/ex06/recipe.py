import os


cookbook = {'sandwich': {
                'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                'meal': 'lunch',
                'prep_time': '10'},
            'cake': {
                'ingredients': ['flour', 'sugar', 'eggs'],
                'meal': 'dessert',
                'prep_time': '60'},
            'salad': {
                'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                'meal': 'lunch',
                'prep_time': '15'}}


def display_recipe(recipe_name: str) -> None:
    for recipe in cookbook.items():
        if recipe_name in recipe:
            print(f'''\nRecipe for {recipe[0]}:\n'''
                  f'''Ingredients list: {recipe[1]['ingredients']}\n'''
                  f'''To be eaten for {recipe[1]['meal']}.\n'''
                  f'''Takes {recipe[1]['prep_time']} minutes of cooking.''')


def delete_recipe(recipe_name: str) -> None:
    if recipe_name in cookbook.keys():
        del cookbook[recipe_name]
        print('\nDelete recipe in CookBook')
    else:
        print('\nThis recipe does not exist')


def add_new_recipe(name, ingredients, meal, prep_time) -> None:
    cookbook[name] = {'ingredients': ingredients,
                      'meal': meal,
                      'prep_time': prep_time}


def display_all_recipe() -> None:
    print('\nDisplay all recipe:')
    for recipe in cookbook.keys():
        display_recipe(recipe)


def cookbooks():
    run_programme = True
    while run_programme:
        print('Please select an option by typing the corresponding number:')
        print('1: Add a recipe\n'
              '2: Delete a recipe\n'
              '3: Print a recipe\n'
              '4: Print the cookbook\n'
              '5: Quit')
        input_user = input()
        if input_user == '1':
            recipe_name = input('\nPlease enter your recipe name:\n')
            ingredients = input('Please enter a list of ingredients'
                                ' in your recipe:\n').split()
            meal = input('Please enter the type of meal:\n')
            prep_time = input('Please enter the preparation'
                              ' time in minutes:\n')
            add_new_recipe(recipe_name, ingredients, meal, prep_time)
        elif input_user == '2':
            recipe_name = input('\nPlease enter the name of'
                                ' the recipe you want to delete:\n')
            delete_recipe(recipe_name)
        elif input_user == '3':
            recipe_name = input('\nPlease enter the recipe\'s'
                                ' name to get its details:\n')
            if recipe_name not in cookbook.keys():
                print('\nThis recipe does not exist')
            else:
                display_recipe(recipe_name)
        elif input_user == '4':
            display_all_recipe()
        elif input_user == '5':
            run_programme = False
            print('\nCookbook closed.')
            continue
        else:
            print('\nThis option does not exist,'
                  'please type the corresponding number.\n'
                  'To exit, enter 5')
        input('\nPress enter to return to the menu...')
        os.system('clear')


if __name__ == "__main__":
    cookbooks()
