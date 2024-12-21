import re


class ClientShort:
    def __init__(self, company_name, contact_person, phone):
        self.set_company_name(company_name)
        self.set_contact_person(contact_person)
        self.set_phone(phone)

    # Геттеры
    def get_company_name(self):
        return self.__company_name

    def get_contact_person(self):
        return self.__contact_person

    def get_phone(self):
        return self.__phone

    def set_company_name(self, company_name):
        if not self.is_valid_name(company_name):
            raise ValueError("Некорректное название компании")
        self.__company_name = company_name

    def set_contact_person(self, contact_person):
        if not self.is_valid_name(contact_person):
            raise ValueError("Некорректное контактное лицо")
        self.__contact_person = contact_person

    def set_phone(self, phone):
        if not self.is_valid_phone(phone):
            raise ValueError("Некорректный номер телефона")
        self.__phone = phone

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
