from ShoesModel import ShoesModel
from View import ShoesView
from Controller import ShoesController


model = ShoesModel()
controller = ShoesController(model)
view = ShoesView(controller)

view.print_default_action()
view.print_types_list()
view.print_colors_list()
view.print_prices_list()
view.print_makers_list()
view.print_sizes_list()
print()
view.add_shoes('Муж', 'Кроссовки', 'Красный', 5000, 'Adidas', 43, 'shoes.json', 'is_stuff')
view.add_shoes('Жен', 'Сапоги', 'Синий', 6541, 'Vienna', 39, 'shoes.json', 'is_stuff')
view.add_shoes('Жен', 'Туфли', 'Зеленый', 1652, 'Gucci', 38, 'shoes.json')
view.add_shoes('Муж', 'Сандали', 'Коричневый', 564, 'Витязь', 44, 'shoes.json', 'is_stuff')
view.add_shoes('Жен', 'Туфли', 'Красный', 8416, 'Terranova', 39, 'shoes.json', 'is_stuff')
view.add_shoes('Муж', 'Кроссовки', 'Белый', 7412, 'Nike', 44, 'shoes.json', 'is_stuff')
print()
view.print_default_action()
view.print_types_list()
view.print_colors_list()
view.print_prices_list()
view.print_makers_list()
view.print_sizes_list()
