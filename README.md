# ***HW8*** :mortar_board:
___
## **Критерії прийому:**
* get_birthdays_per_week выводит именинников в формате:

  Monday: Bill, Jil
  
  Friday: Kim, Jan

* Пользователей, у которых день рождения был на выходных, надо поздравить в понедельник
* Для отладки удобно создать тестовый список users и заполнить его самостоятельно
* Функция выводит пользователей с днями рождения на неделю вперед от текущего дня
* Неделя начинается с понедельника

1. Створюємо функцію `get_birthdays_per_week()` для обробки і збирання результатів у словник:
```python
def get_birthdays_per_week(users: list) -> dict:
    date_now = datetime.now()
    for i in users:
        birthday = i.get("birthday", None)
        birt = datetime.strptime(birthday, '%Y-%m-%d')
        other_birt = birt.replace(year=date_now.year)
        difference = other_birt - date_now
        if timedelta(-1) <= difference <= timedelta(7):
            d = datetime.weekday(other_birt)
            if d == 0:
                d = "Monday"
            if d == 1:
                d = "Tuesday"
            if d == 2:
                d = "Wednesday"
            if d == 3:
                d = "Thursday"
            if d == 4:
                d = "Friday"
            if d == 5 or d == 6:
                d = "Monday"
            result.update({d: i.get('name')})
    return result
```

2. Створюємо функцію `result_birthday()` для виведення результату на екран:
