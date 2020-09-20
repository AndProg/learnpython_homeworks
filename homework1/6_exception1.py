"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  
  "и завершала работу при помощи оператора break" 
  Андрей: не совсем на данный момент понимаю, зачем пользоваться оператором Break, если 
    
"""

def ask_user(some_QA_dict):
  
    while True:
      try:
        user_reply = input('Ну что... поговорим? >>> ')
      except KeyboardInterrupt:
        print('  >>> Пока!')
        break

      if user_reply in some_QA_dict:
        print(some_QA_dict[user_reply])
        break
      else:
        print('Спросика что-нибудь еще')


if __name__ == "__main__":
  
  QA_dict_1 = {
    'Что делаешь?': 'слежу за тобой О_о', 
    'Зачем ты это делаешь?': 'Ты разве против О_О', 
    'Кто ты?': 'Это не важно -_-'
  }


  ask_user(QA_dict_1)

