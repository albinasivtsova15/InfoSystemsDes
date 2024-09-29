class Clients:
    def __init__(self, id, name_company, contact_person, phone, email, passport, requisites):
        if self.validate_id(id) and self.validate_name_company(name_company) and \
           self.validate_contact_person(contact_person) and self.validate_phone(phone) and \
           self.validate_email(email) and self.validate_passport(passport) and \
           self.validate_requisites(requisites):
            # Если все данные валидны, сохраняем их
            self.__id = id
            self.__name_company = name_company
            self.__contact_person = contact_person
            self.__phone = phone
            self.__email = email
            self.__passport = passport
            self.__requisites = requisites
        else:
            raise ValueError("Одно или несколько полей содержат некорректные данные")

   
    @staticmethod
    def validate_id(id):
        return isinstance(id, int) and id > 0  # ID должен быть целым числом и больше 0

    @staticmethod
    def validate_name_company(name_company):
        return isinstance(name_company, str) and len(name_company) > 0  # Название компании не должно быть пустым

    @staticmethod
    def validate_contact_person(contact_person):
        return isinstance(contact_person, str) and len(contact_person) > 0  # Имя контактного лица не должно быть пустым

    @staticmethod
    def validate_phone(phone):
        return isinstance(phone, str) and phone.isdigit() and len(phone) >= 7  # Телефон должен содержать только цифры и быть не короче 7 символов

    @staticmethod
    def validate_email(email):
        return isinstance(email, str) and "@" in email and "." in email  # Email должен содержать @ и точку

    @staticmethod
    def validate_passport(passport):
        return isinstance(passport, str) and len(passport) == 11  # Паспорт должен содержать ровно 11 символов (пример: "1234 567890")

    @staticmethod
    def validate_requisites(requisites):
        return isinstance(requisites, str) and len(requisites) > 0  # Реквизиты не должны быть пустыми

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

    def get_requisites(self):
        return self.__requisites

    # Сеттеры с валидацией для изменения данных
    def set_id(self, id):
        if self.validate_id(id):
            self.__id = id
        else:
            raise ValueError("Некорректный ID")

    def set_name_company(self, name_company):
        if self.validate_name_company(name_company):
            self.__name_company = name_company
        else:
            raise ValueError("Некорректное название компании")

    def set_contact_person(self, contact_person):
        if self.validate_contact_person(contact_person):
            self.__contact_person = contact_person
        else:
            raise ValueError("Некорректное контактное лицо")

    def set_phone(self, phone):
        if self.validate_phone(phone):
            self.__phone = phone
        else:
            raise ValueError("Некорректный телефон")

    def set_email(self, email):
        if self.validate_email(email):
            self.__email = email
        else:
            raise ValueError("Некорректный email")

    def set_passport(self, passport):
        if self.validate_passport(passport):
            self.__passport = passport
        else:
            raise ValueError("Некорректные паспортные данные")

    def set_requisites(self, requisites):
        if self.validate_requisites(requisites):
            self.__requisites = requisites
        else:
            raise ValueError("Некорректные реквизиты")



