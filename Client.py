#Выбрана сущность Clients

import json
import re
from ClientShort import ClientShort

class Client(ClientShort):
    def __init__(self, client_id, company_name, contact_person, phone, email, passport):
        super().__init__(company_name, contact_person, phone)  # Инициализация базового класса
        self.__client_id = client_id
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
    def is_valid_email(email):
        return re.fullmatch(r'(.+)@(.+)\.(.+)', email) is not None

    @staticmethod
    def is_valid_passport(passport):
        return re.fullmatch(r'\d{4} \d{6}', passport) is not None


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
        
    def __str__(self):
        short_info = super().__str__()
        return (
            f"Client ID: {self.__client_id}\n"
            f"{short_info}\n"
            f"Email: {self.__email}\n"
            f"Passport: {self.__passport}"
        )
