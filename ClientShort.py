import re


class ClientShort:
    def __init__(self, company_name, contact_person, phone):
        self.__company_name = self.set_value(company_name, self.is_valid_name)
        self.__contact_person = self.set_value(contact_person, self.is_valid_name)
        self.__phone = self.set_value(phone, self.is_valid_phone)

    # Геттеры
    def get_company_name(self):
        return self.__company_name

    def get_contact_person(self):
        return self.__contact_person

    def get_phone(self):
        return self.__phone

    # Универсальный метод для проверки и записи
    def set_value(self, value, validator):
        if validator(value):
            return value
        raise ValueError(f"Некорректное значение: {value}")

    # Статические методы для валидации
    @staticmethod
    def is_valid_name(name):
        return bool(name.strip())

    @staticmethod
    def is_valid_phone(phone):
        return re.fullmatch(r'\+?\d{10,15}', phone) is not None

    # Метод сравнения
    def __eq__(self, other):
        if not isinstance(other, ClientShort):
            return False
        return (
            self.__company_name == other.__company_name and
            self.__contact_person == other.__contact_person and
            self.__phone == other.__phone
        )

    # Метод строкового представления
    def __str__(self):
        return (
            f"Company Name: {self.__company_name}\n"
            f"Contact Person: {self.__contact_person}\n"
            f"Phone: {self.__phone}"
        )
