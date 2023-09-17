def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient_name = ingredient_info[0]
                ingredient_quantity = int(ingredient_info[1])
                ingredient_measure = ingredient_info[2]
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': ingredient_quantity,
                    'measure': ingredient_measure
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
    return cook_book

file_name = 'recipes.txt'
cook_book = read_recipes(file_name)
print(cook_book)



