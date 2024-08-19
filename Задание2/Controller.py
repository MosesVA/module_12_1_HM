class RecipeController:
    def __init__(self, model):
        self.model = model

    def default_action(self):
        if self.model.get_recipes():
            return self.model.get_recipes()
        else:
            return 'Нет данных!'

    def only_names_list(self):
        names = []
        data = self.model.get_recipes()
        if data:
            for element in data:
                names.append(element['name'])
        else:
            return 'Названий нет!'
        return names

    def only_authors_list(self):
        authors = []
        data = self.model.get_recipes()
        if data:
            for element in data:
                authors.append(element['author'])
        else:
            return 'Авторов нет!'
        return authors

    def only_types_list(self):
        types = []
        data = self.model.get_recipes()
        if data:
            for element in data:
                types.append(element['type_recipe'])
        else:
            return 'Типов нет!'
        return types

    def only_cuisines_list(self):
        cuisines = []
        data = self.model.get_recipes()
        if data:
            for element in data:
                cuisines.append(element['cuisine'])
        else:
            return 'Кухонь нет!'
        return cuisines

    def add_recipe(self, name, author, type_recipe, text, ingredients, cuisine, filename, validation):
        if validation in ['is_superuser', 'is_stuff']:
            self.model.add_recipe(name, author, type_recipe, text, ingredients, cuisine, filename)
            return 'Рецепт успешно добавлен!'
        else:
            return 'Нет доступа!'
