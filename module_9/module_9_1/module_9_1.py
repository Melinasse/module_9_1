from typing import Union,List

def apply_all_func(int_list: List[Union[int, float]], *function):
    result = {}
    for func in function:
        result[func.__name__] = func(int_list)
        # print(result)
    return result

"""
Первый вариант это когда в парметр function передаю свои функции
"""
def minimum(int_list):
    return min(int_list)

def maximum(int_list):
    return max(int_list)

def lenght(int_list):
      return len(int_list)

def summa(int_list):
      return sum(int_list)

def sort(int_list):
       return sorted(int_list)


print(apply_all_func([11, 44, 7.5, 99, 0.31, 1000], maximum, minimum))
print(apply_all_func([11, 44, 7.5, 99, 0.31, 1000], lenght, summa, sort))
"""
Вариант согласно задаче. Применяются встроенные функции
"""
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))