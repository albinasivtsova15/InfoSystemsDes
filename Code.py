# Для ЛР1-ЛР4 выбрана сущность Клиенты.

class Clients:
    def __init__(self, id, name_company, contact_person, phone, email, passport):
        #Проверка
        if self.check_id(id) and self.check_name_company(name_company) and self.check_contact_person(contact_person) and 
           self.check_phone(phone) and self.check_email(email) and self.check_passport(passport):
                self.__id = id
                self.__name_company = name_company
                self.__contact_person = contact_person
                self.__phone = phone
                self.__email = email
                self.__passport = passport
       else:
                raise ValueError("Некорректные данные для клиента")
#Валидация 
    @staticmethod
    def check_id(id):
        return isinstance(id, int) and id > 0
        
    @staticmethod
    def check_name_company(name_company):
        return isinstance(name_company, str) and len(name_company) > 0

    @staticmethod
    def check_contact_person(contact_person):
        return isinstance(contact_person, str) and len(contact_person) > 0

    @staticmethod
    def check_phone(phone):
        return isinstance(phone, str) and phone.isdigit() and len(phone) >= 7 #isdigit - встроенный метод строки (состоит ли из цифр)

    @staticmethod
    def check_email(email):
        return isinstance(email, str) and "@" in email and "." in email

    @staticmethod
    def check_passport(passport):
        return isinstance(passport, str) and len(passport) == 11
        
#Геттеры    
    def get_id(self):
        return self.__id

    def get_name_company(self):
        return self.__name_company

    def get_contact_person(self):
        return self.__contact_person

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_passport(self):
        return self.__passport

#Сеттеры
   def set_id(self, id):
        if self.check_id(id):
            self.__id = id
        else:
            raise ValueError("Некорректный ID")

    def set_name_company(self, name_company):
        if self.check_name_company(name_company):
            self.__name_company = name_company
        else:
            raise ValueError("Некорректное название компании")

    def set_contact_person(self, contact_person):
        if self.check_contact_person(contact_person):
            self.__contact_person = contact_person
        else:
            raise ValueError("Некорректное контактное лицо")

    def set_phone(self, phone):
        if self.check_phone(phone):
            self.__phone = phone
        else:
            raise ValueError("Некорректный телефон")

    def set_email(self, email):
        if self.check_email(email):
            self.__email = email
        else:
            raise ValueError("Некорректный email")

    def set_passport(self, passport):
        if self.check_passport(passport):
            self.__passport = passport
        else:
            raise ValueError("Некорректные паспортные данные")

 



