from datetime import datetime


class Geburtstag:
    def __init__(self, name, tag, monat, jahr):
        self.name = name
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    def get_age(self):
        today = datetime.now()
        return today.year - self.jahr - ((today.month, today.day) <
                                         (self.monat, self.tag))

    def print(self):
        print(f"{self.name}:")
        print(f"{self.tag}.{self.monat}.{self.jahr}")


class GeburtstagSpeicher:
    def __init__(self):
        self.__list = []

    def auto_new(self, name):
        current_date = datetime.now()
        self.__list.append(Geburtstag(name,
                                      current_date.day,
                                      current_date.month,
                                      current_date.year))

    def manual_new(self, name, tag, monat, jahr):
        self.__list.append(Geburtstag(name, tag, monat, jahr))

    def get_birthdays(self):
        return self.__list

    def get_birthday_from_name(self, name):
        for bd in self.__list:
            if bd.name == name:
                return bd
        return 0

    def get_birthdays_in_month(self, month):
        bds = []
        for bd in self.__list:
            if bd.monat == month:
                bds.append(bd)
        return bds

    def birthdays_today(self):
        today = datetime.today()
        bds = []
        for bd in self.__list:
            # unnecessarily verbose
            if bd.tag == today.day and bd.monat == today.month:
                bds.append(bd)
        return bds

    def print_birthdays(self):
        for bd in self.__list:
            print(bd.name)
            print(f"{bd.tag}.{bd.monat}.{bd.jahr}")
            print(bd.calculate_age())


s = GeburtstagSpeicher()
s.manual_new("Frederik", 2, 6, 2006)
s.manual_new("Test", 1, 6, 2000)
s.manual_new("Test2", 2, 11, 2010)
s.auto_new("Test4")
s.manual_new("Test18",5,11,2005)
bds = s.get_birthdays_in_month(11)
if bds != []:
    for bd in bds:
        bd.print()

# s.auto_new("Test3")

# bd = s.get_birthday_from_name("Frederik")
# if bd != 0:
#     bd.print()

# bds = s.get_birthdays_in_month(6)
# for bd in bds:

# s.get_birthday_from_name("Test3").print()

bds = s.birthdays_today()
if bds != []:
    print("Birthdays today")
