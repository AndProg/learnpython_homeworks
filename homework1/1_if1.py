"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

"""
1_if1.py (замечания Алисы)

1. Давай называть функции более осмысленно, по их назначению)

2. Использовать age.isnumeric()  было хитрым решением, но что будет, если я положу 
в переменную age символ 'Ⅻ'? 
// можно вызывать функцию, конвертирующую римские числа в арабские :/ .. есть и готове модули для этого 

3. Есть ли смысл каждый раз писать int(age)? Может, лучше где-нибудь написать это один 
раз и запомнить в переменную?

4. По условиям задания мы должны положить результат работы функции в переменную и 
только потом вывести ее на экран.
"""




import roman # импортирую модуль-конвертер из арабских чисел в римские и обратно 

def arab_num_validator(age_input):
    validator = True
    for symbol in str(age_input):
      if symbol in ['1', '2', '3', '4' ,'5' ,'6', '7', '8', '9', '0']:
        validator = validator * True
      else:
        validator = validator * False
    return(validator)
    
    
def roman_num_validator(age_input):
    validator = True
    for symbol in str(age_input):
      if symbol.upper() in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
        validator = validator * True
      else:
        validator = validator * False
    return(validator)


def age_and_activity_separator(age_input):
      age_input = int(age_input)
      # по факту проверка 'age<0' не нужна, потому что отрицательные значения отлавливает arab_num_validator
      if age_input < 0: 
        return('Введите положительное целое число арабскими цифрами') 
      elif 0 < age_input <= 7:
        return('Вам место в детском саду')
      elif 7 < age_input <= 17:
        return('Вам самое место в школе')
      elif 17 < age_input <= 24:
        return('Вы должны учиться в университете')
      elif 24 < age_input <= 67:
        return('Работать!')
      else:
        return('Время чиллить ;)')


def age_differentiator(age):      
  
    if arab_num_validator(age) == True:
      result = age_and_activity_separator(age)
      return(result)

    elif roman_num_validator(age) == True:     
      converted_age = roman.fromRoman(age.upper())
      result = age_and_activity_separator(converted_age)
      return(result)

    else:
      return('Недопустимый ввод, попробуйте еще раз')

    

if __name__ == "__main__":

  user_age = input('Введите ваш возраст: ')

  result = age_differentiator(user_age)

  print(result)
