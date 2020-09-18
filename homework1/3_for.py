"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
'''
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":

'''
"""
3_for.py (Замечания Алисы)

1. А что будет, если количество оценок в разных классах будет разным? 
Будет ли программа работать правильно? 
// Да, программа работает корректно.. добавил счетчик учеников

2. Можно ли сделать все то же самое одним проходом по словарю?
// добавил второй, альтернативный набор счетчиков

"""


school_register = [
  {'studying_class': '4a', 'scores': [3,4,4,5,2,2,2,2,2,2]},
  {'studying_class': '5a', 'scores': [3,2,4,4,2]},
  {'studying_class': '6a', 'scores': [5,5,2,3,4]},
  {'studying_class': '7a', 'scores': [3,4,2,5,5]},
]

print('------')
# набор счеткиков_ вариант №1
''' 
for school_class in school_register:
    score_sum = 0
    num_of_students = 0
    for score in school_class['scores']:
      score_sum += score
      num_of_students += 1
'''
# набор счетчиков_ вариант №2
for school_class in school_register:
    score_sum = sum(school_class['scores'])
    num_of_students = len(school_class['scores'])


    current_class = school_class['studying_class']
    average_score = score_sum/len(school_class['scores'])

    print(f'Средняя оценка в классе {current_class}, где {num_of_students} учеников : {average_score}')
    
    school_class['class_average_score'] = average_score

score_sum = 0
for school_class in school_register:
  score_sum += school_class['class_average_score']

school_average_score = score_sum/len(school_register)

print('------')
print(f'Средняя оценка по школе: {round(school_average_score,2)}')
print('------')
