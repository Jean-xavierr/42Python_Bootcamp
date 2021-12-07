from book import Book
from recipe import Recipe


#error recipe
cooki_error = Recipe("cooki", 0, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
cooki_error2 = Recipe("cooki", 1.5, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
cooki_error3 = Recipe("cooki", 1, 10, [], "deliciousness incarnate", "dessert")

#no error
Recipe("cooki", 1, 10, ["dough", "sugar", "love"], "deliciousness incarnate", "dessert")
print("Congratulations you finally made sime delicous cookies")


# recipe = Recipe('Icecream', '4', '60', ['milk', 'sugar', 'berry'], "", "dessert")
# # print(recipe)

# recipe2 = Recipe('salad', '4', '60', ['milk', 'sugar', 'berry'], "", "dessert")
# # print(recipe)

print()
b = Book("My seductive recipes")
print(b.creation_date)
# should be the current date and time
print(b.last_update)
# should be the same as the creation date or None

#------------------------------

crumble = Recipe("Crumble", 1, 25, ["apples", "flour", "sugar"], "delicious", "dessert")
b.add_recipe(crumble)
print(b.last_update)

# error give string
txt = 'hello'
b.add_recipe(txt)

print()
b.get_recipe_by_name("Crumble")
# should print the recipe
# AND
# <Recipe object at x>

b.get_recipe_by_name("Liver Icecream")
# The recipe does not exist
# The error must be handled in a justifiable manner
# such as returning None, [], or printing an error message


print(b.get_recipes_by_types("dessert")[0])
# Should print the Crumble recipe
b.get_recipes_by_types("asdasd")
# The recipe type does not exist, error must be handled in a justifiable manner
# such as returning None, [], or printing an error message
print(b.get_recipes_by_types("starter"))
print(b.last_update)
