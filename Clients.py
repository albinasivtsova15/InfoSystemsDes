#Выбрана сущность Clients

import re
class Client:
    def __init__(self, client_id, company_name, contact_person, phone, email, passport):
        # Приватные поля, доступ к которым осуществляется через методы
        self.__client_id = client_id
        self.__company_name = self.set_value(company_name, self.is_valid_company_name)
        self.__contact_person = self.set_value(contact_person, self.is_valid_contact_person)
        self.__phone = self.set_value(phone, self.is_valid_phone)
        self.__email = self.set_value(email, self.is_valid_email)
        self.__passport = self.set_value(passport, self.is_valid_passport)

    # Методы для получения значений полей (геттеры)
    def get_client_id(self):
        return self.__client_id

    def get_company_name(self):
        return self.__company_name

    def get_contact_person(self):
        return self.__contact_person

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_passport(self):
        return self.__passport

    # Универсальный метод для установки значений с проверкой валидности
    def set_value(self, value, validator):
        if validator(value):
            return value
        else:
            raise ValueError(f"Некорректное значение: {value}")

   # Методы для проверки валидности данных (статические)
    @staticmethod
    def is_valid_company_name(company_name):
        return bool(company_name)

    @staticmethod
    def is_valid_contact_person(contact_person):
        return bool(contact_person)

    @staticmethod
    def is_valid_phone(phone):
        return re.fullmatch(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}', phone) is not None

    @staticmethod
    def is_valid_email(email):
        return re.fullmatch(r'(.+)@(.+)\.(.+)', email) is not None

    @staticmethod
    def is_valid_passport(passport):
        return re.fullmatch(r'\d{4} \d{6}', passport) is not None

