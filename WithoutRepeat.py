class Clients:
    def __init__(self, id, name_company, contact_person, phone, email, passport, requisites):
        self.__id = self.validate_and_set("id", id)
        self.__name_company = self.validate_and_set("name_company", name_company)
        self.__contact_person = self.validate_and_set("contact_person", contact_person)
        self.__phone = self.validate_and_set("phone", phone)
        self.__email = self.validate_and_set("email", email)
        self.__passport = self.validate_and_set("passport", passport)
        self.__requisites = self.validate_and_set("requisites", requisites)


    def validate_and_set(self, field_name, value):
        validators = {
            "id": lambda x: isinstance(x, int) and x > 0,
            "name_company": lambda x: isinstance(x, str) and len(x) > 0,
            "contact_person": lambda x: isinstance(x, str) and len(x) > 0,
            "phone": lambda x: isinstance(x, str) and x.isdigit() and len(x) >= 7,
            "email": lambda x: isinstance(x, str) and "@" in x and "." in x,
            "passport": lambda x: isinstance(x, str) and len(x) == 11,
            "requisites": lambda x: isinstance(x, str) and len(x) > 0
        }

        if field_name in validators and validators[field_name](value):
            return value
        else:
            raise ValueError(f"Некорректное значение для {field_name}")


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

    def set_id(self, id):
        self.__id = self.validate_and_set("id", id)

    def set_name_company(self, name_company):
        self.__name_company = self.validate_and_set("name_company", name_company)

    def set_contact_person(self, contact_person):
        self.__contact_person = self.validate_and_set("contact_person", contact_person)

    def set_phone(self, phone):
        self.__phone = self.validate_and_set("phone", phone)

    def set_email(self, email):
        self.__email = self.validate_and_set("email", email)

    def set_passport(self, passport):
        self.__passport = self.validate_and_set("passport", passport)

    def set_requisites(self, requisites):
        self.__requisites = self.validate_and_set("requisites", requisites)

