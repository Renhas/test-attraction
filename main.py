from typing import List
from copy import copy

class ValuableObject:
    def __init__(self, value: int, weight: int, id: int) -> None:
        self.__value = value
        self.__weight = weight
        self.__id = id
    
    @property
    def value(self):
        return self.__value
    
    @property
    def weight(self):
        return self.__weight
    
    @property
    def id(self):
        return self.__id
    
    def __str__(self) -> str:
        return f"Object #{self.id}:\n\tValue: {self.value}, Weight: {self.weight}"

def recurrent_solver(objects: List[ValuableObject], current_max_weight: int) -> List[ValuableObject]:
    good_objs = [obj for obj in objects if obj.weight <= current_max_weight]
    solution = []
    if len(good_objs) == 0:
        return solution
    
    best_value = 0
    for obj in good_objs:
        new_objects = copy(good_objs)
        new_objects.remove(obj)
        current_solution = recurrent_solver(new_objects, current_max_weight-obj.weight)
        current_solution.append(obj)
        current_value = sum(n_obj.value for n_obj in current_solution)
        if current_value > best_value:
            best_value = current_value
            solution = copy(current_solution)
    return solution
    

def solve(objects: List[ValuableObject], max_weight: int) -> List[ValuableObject]:
    sorted_objects = sorted(objects,
                     key=lambda obj: obj.value / obj.weight,
                     reverse=True)
    result_objects = recurrent_solver(sorted_objects, max_weight)
    return result_objects

def main():
    test_obj = [
        ValuableObject(value=3, weight=2, id=1),
        ValuableObject(value=4, weight=2, id=2),
        ValuableObject(value=7, weight=6, id=3),
        ValuableObject(value=3, weight=5, id=4)
    ]
    res = solve(test_obj, 8)
    for obj in res:
        print(obj)

if __name__ == "__main__":
    main()


