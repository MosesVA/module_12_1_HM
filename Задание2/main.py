from RecipeModel import RecipeModel
from View import RecipeView
from Controller import RecipeController


model = RecipeModel()
controller = RecipeController(model)
view = RecipeView(controller)

view.print_default_action()
view.print_names_list()
view.print_authors_list()
view.print_types_list()
view.print_cuisines_list()
print()
view.add_recipe('Спагетти Классик', 'Violonchelli', 'Второе',
                'Сварить спагетти в кастрюле, посыпать солью, слить воду', 'Соль, Спагетти',
                'Итальянская', 'recipes.json', 'is_stuff')
view.add_recipe('Пельмени', 'Богатырь', 'Второе',
                'Сварить пельмени в кастрюле, посыпать солью, слить воду', 'Соль, Пельмени',
                'Русская', 'recipes.json', 'is_stuff')
view.add_recipe('Яичница', 'Боровъ', 'Завтрак',
                'Пожарить яйцо на сковороде, посыпать солью', 'Соль, Яйцо',
                'Белорусская', 'recipes.json')
view.add_recipe('Салат Оливье', 'Оливер', 'Салат',
                'Нарезать кубиками все ингредиенты, заправить майонезом', 'Горох, Картошка, Колбаса, Яйцо',
                'Французская', 'recipes.json', 'is_stuff')
view.add_recipe('Торт Блинный', 'Блинский', 'Десерт',
                'Сделать торт из блинов, крема и фрукта на свой вкус', 'Блины, Фрукт на свой вкус, Крем',
                'Литовская', 'recipes.json', 'is_stuff')
print()
view.print_default_action()
view.print_names_list()
view.print_authors_list()
view.print_types_list()
view.print_cuisines_list()

