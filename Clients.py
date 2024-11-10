#Выбрана сущность Clients

import json
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

    @classmethod
    def from_json(cls, json_data):
        try:
            data = json.loads(json_data)  # Парсинг JSON
        except json.JSONDecodeError:
            print("Ошибка: неверный формат JSON.")
            return None  
        
        required_fields = ['client_id', 'company_name', 'contact_person', 'phone', 'email', 'passport']
        for field in required_fields:
            if field not in data:
                print(f"Ошибка: отсутствует необходимое поле: {field}")
                return None  

        return cls(
            client_id=data['client_id'],
            company_name=data['company_name'],
            contact_person=data['contact_person'],
            phone=data['phone'],
            email=data['email'],
            passport=data['passport'],
        )
        
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

    #Полная и краткая форма. Сравнение объектов.
    
    def __str__(self):
        return (
            f"Client ID: {self.__client_id}\n"
            f"Company Name: {self.__company_name}\n"
            f"Contact Person: {self.__contact_person}\n"
            f"Phone: {self.__phone}\n"
            f"Email: {self.__email}\n"
            f"Passport: {self.__passport}"
        )

    def get_short_info(self):
        return f"{self.__company_name}, {self.__contact_person}, {self.__phone}"

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return (
            self.__client_id == other.__client_id and
            self.__company_name == other.__company_name and
            self.__contact_person == other.__contact_person and
            self.__phone == other.__phone and
            self.__email == other.__email and
            self.__passport == other.__passport
        )
