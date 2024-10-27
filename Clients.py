#Выбрана сущность Clients

class Client:
    def __init__(self, client_id, company_name, contact_person, phone, email, passport):
        # Приватные поля, доступ к которым осуществляется через методы
        self.__client_id = client_id
        self.__company_name = company_name
        self.__contact_person = contact_person
        self.__phone = phone
        self.__email = email
        self.__passport = passport

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
        self.__company_name = company_name

    def set_contact_person(self, contact_person):
        self.__contact_person = contact_person

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def set_passport(self, passport):
        self.__passport = passport
