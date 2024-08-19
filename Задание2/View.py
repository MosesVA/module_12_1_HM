class RecipeView:
    def __init__(self, controller):
        self.controller = controller

    def print_default_action(self):
        print(self.controller.default_action())

    def print_names_list(self):
        print(self.controller.only_names_list())

    def print_authors_list(self):
        print(self.controller.only_authors_list())

    def print_types_list(self):
        print(self.controller.only_types_list())

    def print_cuisines_list(self):
        print(self.controller.only_cuisines_list())

    def add_recipe(self, name, author, type_recipe, text, ingredients, cuisine, filename, validation='user'):
        print(self.controller.add_recipe(name, author, type_recipe, text, ingredients, cuisine, filename, validation))
