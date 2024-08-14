from typing import List
from solver import ValuableObject, solve

def make_objects(hours: List[float], value: List[int]):
    return [ValuableObject(val, hour, idx+1) for idx, (hour, val) in enumerate(zip(hours, value))]

def print_result(names: List[str], result: List[ValuableObject]):
    print("Оптимальный маршрут:\n")
    for res_obj in result:
        print(f"{res_obj.id}. {names[res_obj.id]}")

def main():
    max_hours = 48 - 2*8
    hours = [5, 8, 3.5, 10, 9, 1, 4, 2, 7, 5.5,
             2, 5, 12, 2, 4, 1.5, 1, 3, 6, 7]
    value = [10, 11, 4, 7, 15, 17, 3, 9, 12, 6, 
             19, 8, 20, 13, 2, 5, 14, 18, 1, 16]
    names = ['Исаакиевский собор', 'Эрмитаж', 'Кунсткамера',
             'Петропавловская крепость', 'Ленинградский зоопарк',
             'Медный всадник', 'Казанский собор', 'Спас на Крови',
             'Зимний дворец Петра I', 'Зоологический музей', 'Музей обороны и блокады Ленинграда',
             'Русский музей', 'Навестить друзей', 'Музей восковых фигур',
              'Литературно-мемориальный музей Ф.М. Достоевского', 'Екатерининский дворец',
              'Петербургский музей кукол', 'Музей микроминиатюры «Русский Левша»',
              'Всероссийский музей А.С. Пушкина и филиалы', 'Музей современного искусства Эрарта']
    
    result = solve(make_objects(hours, value), max_hours)
    print_result(names, result)

if __name__ == "__main__":
    main()


