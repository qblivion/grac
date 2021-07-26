from datetime import date

s = str(date.today())


class Person:

    def __init__(self, name, birthday, mail, gender):
        self.name = name
        self.birthday = birthday
        self.mail = mail
        self.gender = gender

    def is_anniversary(self):
        if (int(s[2:4]) - int(self.birthday[2:4])) % 5 == 0:
            return True
        else:
            return False


Ruslan_Sadykov = Person("Садыков Руслан Тимурович", "2003-06-18", "rsadykov944@gmail.com", "m")
Vera_Sadykova = Person("Садыкова Вера Сергеевна", "1977-12-01", "sadykova_09@mail.ru", "f")
Yubilyar = Person("1 2 3", "2016-01-10", "abc", "m")
