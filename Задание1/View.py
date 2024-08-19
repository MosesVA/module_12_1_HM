class ShoesView:
    def __init__(self, controller):
        self.controller = controller

    def print_default_action(self):
        print(self.controller.default_action())

    def print_types_list(self):
        print(self.controller.only_types_list())

    def print_makers_list(self):
        print(self.controller.only_makers_list())

    def print_colors_list(self):
        print(self.controller.only_colors_list())

    def print_sizes_list(self):
        print(self.controller.only_sizes_list())

    def print_prices_list(self):
        print(self.controller.only_prices_list())

    def add_shoes(self, sex, type_shoes, color, price, maker, size, filename, validation='user'):
        print(self.controller.add_shoes(sex, type_shoes, color, price, maker, size, filename, validation))
