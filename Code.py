# Для ЛР1-ЛР4 выбрана сущность Клиенты.

class Clients:
    def __init__(self, id, name_company, contact_person, phone, email, passport):
        self.__id = id
        self.__name_company = name_company
        self.__contact_person = contact_person
        self.__phone = phone
        self.__email = email
        self.__passport = passport

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

    def set_id(self, id):
        self.__id = id

    def set_name_company(self, name_company):
        self.__name_company = name_company

    def set_contact_person(self, contact_person):
        self.__contact_person = contact_person

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def set_passport(self, passport):
        self.__passport = passport



