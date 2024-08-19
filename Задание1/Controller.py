class ShoesController:
    def __init__(self, model):
        self.model = model

    def default_action(self):
        if self.model.get_shoes():
            return self.model.get_shoes()
        else:
            return 'Нет данных!'

    def only_types_list(self):
        type_shoes = []
        data = self.model.get_shoes()
        if data:
            for element in data:
                type_shoes.append(element['type_shoes'])
        else:
            return 'Типов нет!'
        return type_shoes

    def only_makers_list(self):
        makers = []
        data = self.model.get_shoes()
        if data:
            for element in data:
                makers.append(element['maker'])
        else:
            return 'Производителей нет!'
        return makers

    def only_colors_list(self):
        colors = []
        data = self.model.get_shoes()
        if data:
            for element in data:
                colors.append(element['color'])
        else:
            return 'Цветов нет!'
        return colors

    def only_sizes_list(self):
        sizes = []
        data = self.model.get_shoes()
        if data:
            for element in data:
                sizes.append(element['size'])
        else:
            return 'Размеров нет!'
        return sizes

    def only_prices_list(self):
        prices = []
        data = self.model.get_shoes()
        if data:
            for element in data:
                prices.append(element['price'])
        else:
            return 'Цен нет!'
        return prices

    def add_shoes(self, sex, type_shoes, color, price, maker, size, filename, validation):
        if validation in ['is_superuser', 'is_stuff']:
            self.model.add_shoes(sex, type_shoes, color, price, maker, size, filename)
            return 'Обувь успешно добавлена!'
        else:
            return 'Нет доступа!'
