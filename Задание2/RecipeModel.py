import json


class RecipeModel:
    def __init__(self):
        self.recipes = []

    def get_recipes(self):
        return self.recipes

    def add_recipe(self, name, author, type_recipe, text, ingredients, cuisine, filename):
        data = {}
        data['name'] = name
        data['author'] = author
        data['type_recipe'] = type_recipe
        data['text'] = text
        data['ingredients'] = ingredients
        data['cuisine'] = cuisine
        self.recipes.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.recipes, fp, ensure_ascii=False, indent=2)
