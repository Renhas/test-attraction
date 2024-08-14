from typing import List
from copy import copy

class ValuableObject:
    """
    Один из объектов в задаче о ранце

    Args:
        value (float): Ценность (значимость) объекта
        weight (float): Вес (стоимость) объекта
        id (int): Номер объекта
    """
    def __init__(self, value: float, weight: float, id: int) -> None:
        self.__value = value
        self.__weight = weight
        self.__id = id
    
    @property
    def value(self) -> float:
        """float: Ценность (значимость) объекта"""
        return self.__value
    
    @property
    def weight(self) -> float:
        """float: Вес (стоимость) объекта"""
        return self.__weight
    
    @property
    def id(self) -> int:
        """int: Номер объекта"""
        return self.__id
    
    def __str__(self) -> str:
        return f"Object #{self.id}:\n\tValue: {self.value}, Weight: {self.weight}"

class ReccurentSolver:
    """Алгоритм решения задачи о ранце с помощью рекуррентных соотношений"""
    @staticmethod
    def solve(objects: List[ValuableObject], current_max_weight: int) -> List[ValuableObject]:
        """
        Основной метод алгоритма

        Args: 
            objects: Список текущих объектов
            current_max_weight: Текущий максимальный вес ранца
        
        Returns:
            Список объектов, попавших в ранец на текущем этапе, или пустой список, если допустимых объектов нет
        """
        good_objs = [obj for obj in objects if obj.weight <= current_max_weight]
        if len(good_objs) != 0:
            return ReccurentSolver.__inner_step(good_objs, current_max_weight) 
        return []

    @staticmethod
    def __inner_step(good_objs: List[ValuableObject], current_max_weight: int) -> List[ValuableObject]:
        """
        Внутренний шаг алгоритма, осуществляет выбор оптимального варианта, исходя из рекурретных соотношений
        
        Args:
            good_objs: Список объектов, вмещающихся в ранец на текущем этапе
            current_max_weight: Текущий максимальный вес ранца

        Returns:
            Список объектов, попавших в ранец на текущем этапе
        """
        best_value = 0
        solution = []
        for obj in good_objs:
            new_objects = copy(good_objs)
            new_objects.remove(obj)
            current_solution = ReccurentSolver.solve(new_objects, current_max_weight-obj.weight)
            current_solution.append(obj)
            current_value = sum(n_obj.value for n_obj in current_solution)
            if current_value > best_value:
                best_value = current_value
                solution = copy(current_solution)
        return solution 

def solve(objects: List[ValuableObject], max_weight: int) -> List[ValuableObject]:
    """
    Метод, осуществляющий решение задачи о ранце. Приводит задачу к релаксированному виду для дальнейшего решения.

    Args:
        objects: Список исходных объектов задачи
        max_weight: Исходное ограничение веса ранца

    Returns:
        Список объектов, попавших в ранец
    """
    sorted_objects = sorted(objects,
                     key=lambda obj: obj.value / obj.weight,
                     reverse=True)
    result_objects = ReccurentSolver.solve(sorted_objects, max_weight)
    return result_objects