import json


class ShoesModel:
    def __init__(self):
        self.shoes = []

    def get_shoes(self):
        return self.shoes

    def add_shoes(self, sex, type_shoes, color, price, maker, size, filename):
        data = {}
        data['sex'] = sex
        data['type_shoes'] = type_shoes
        data['color'] = color
        data['price'] = price
        data['maker'] = maker
        data['size'] = size
        self.shoes.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.shoes, fp, ensure_ascii=False, indent=2)
