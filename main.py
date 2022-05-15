from datetime import datetime, timedelta
from unicodedata import name


def get_birthdays_per_week(users: list) -> dict:
    result = {}
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    date_now = datetime.now()
    for i in users:
        birthday = i.get("birthday", None)
        birt = datetime.strptime(birthday, "%Y-%m-%d")
        other_birt = birt.replace(year=date_now.year)
        difference = other_birt.date() - date_now.date()
        if timedelta(-1) <= difference <= timedelta(7):
            d = datetime.weekday(other_birt)
            if d == 0 or d == 5 or d == 6:
                n = "Monday"
            if d == 1:
                n = "Tuesday"
            if d == 2:
                n = "Wednesday"
            if d == 3:
                n = "Thursday"
            if d == 4:
                n = "Friday"
            for k, v in i.items():
                if v == i.get("name") and n == "Monday":
                    l1.append(v)
                    result.update({n: l1})
                    continue
                if v == i.get("name") and n == "Tuesday":
                    l2.append(v)
                    result.update({n: l2})
                    continue
                if v == i.get("name") and n == "Wednesday":
                    l3.append(v)
                    result.update({n: l3})
                    continue
                if v == i.get("name") and n == "Thursday":
                    l4.append(v)
                    result.update({n: l4})
                    continue
                if v == i.get("name") and n == "Friday":
                    l5.append(v)
                    result.update({n: l5})
                    continue
    return result


def result_birthday(birthday_dict):
    for k, v in birthday_dict.items():
        print(k, ":", ", ".join(v))


users = [
    {"name": "Bill", "birthday": "2000-05-15"},
    {"name": "Till", "birthday": "1995-05-20"},
    {"name": "Alyona", "birthday": "2004-05-14"},
]

if __name__ == "__main__":
    result_birthday(get_birthdays_per_week(users))
