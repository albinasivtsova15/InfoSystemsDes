#Выбрана сущность Clients

import re
class Client:
    def __init__(self, client_id, company_name, contact_person, phone, email, passport):
        # Приватные поля, доступ к которым осуществляется через методы
        self.__client_id = client_id
        self.set_company_name(company_name)
        self.set_contact_person(contact_person)
        self.set_phone(phone)
        self.set_email(email)
        self.set_passport(passport)

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

    # Методы для изменения значений полей (сеттеры)
    def set_company_name(self, company_name):
        if self.is_valid_company_name(company_name):
            self.__company_name = company_name
        else:
            print("Некорректное название компании. Название не обновлено.")

    def set_contact_person(self, contact_person):
        if self.is_valid_contact_person(contact_person):
            self.__contact_person = contact_person
        else:
            print("Некорректное контактное лицо. Данные не обновлены.")

    def set_phone(self, phone):
        if self.is_valid_phone(phone):
            self.__phone = phone
        else:
            print("Некорректный номер телефона. Телефон не обновлен.")

    def set_email(self, email):
        if self.is_valid_email(email):
            self.__email = email
        else:
            print("Некорректный email. Email не обновлен.")

    def set_passport(self, passport):
        if self.is_valid_passport(passport):
            self.__passport = passport
        else:
            print("Некорректные паспортные данные. Данные не обновлены.")

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

