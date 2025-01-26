import json
import os

class ClientRepJson:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Прочитать данные из JSON файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data
        return []

    def write(self, data):
        """Записать данные в JSON файл"""
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def add_entity(self, company_name, contact_person, phone, email, passport):
        """Добавить новый объект Client в список с новым ID"""
        # Чтение данных из файла
        data = self.read()
        
        # Генерация нового ID
        new_id = max([entry['client_id'] for entry in data], default=0) + 1
        
        # Создание нового объекта Client
        new_entity = {
            'client_id': new_id,
            'company_name': company_name,
            'contact_person': contact_person,
            'phone': phone,
            'email': email,
            'passport': passport
        }
     # Проверка на уникальность email
        if any(entry['email'] == email for entry in data):
            raise ValueError('Email должен быть уникальным!')
            
        # Добавляем нового клиента в список
        data.append(new_entity)
        
        # Записываем обновленные данные в файл
        self.write(data)

    def get_by_id(self, client_id):
        """Получить объект Client по ID"""
        data = self.read()
        for entry in data:
            if entry['client_id'] == client_id:
                return entry
        return None  # Если объект не найден

    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов (например, 2-20)"""
        data = self.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]

    def sort_by_field(self, field):
        """Сортировать элементы по выбранному полю"""
        data = self.read()
        if field in ["company_name", "contact_person", "phone", "email", "passport"]:
            data.sort(key=lambda x: x.get(field))
        return data

    def replace_by_id(self, client_id, company_name=None, contact_person=None, phone=None, email=None, passport=None):
        """Заменить объект Client по ID"""
        data = self.read()
        entity = self.get_by_id(client_id)
        if not entity:
            raise ValueError(f"Client с ID {client_id} не найден.")
        
        # Проверка на уникальность email, если он изменяется
        if email and email != entity['email'] and any(entry['email'] == email for entry in data):
            raise ValueError('Email должен быть уникальным!')
        
        # Обновляем данные, если переданы новые значения
        if company_name:
            entity['company_name'] = company_name
        if contact_person:
            entity['contact_person'] = contact_person
        if phone:
            entity['phone'] = phone
        if email:
            entity['email'] = email
        if passport:
            entity['passport'] = passport
        
        # Записываем обновленные данные в файл
        self.write(data)

    def delete_by_id(self, client_id):
        """Удалить объект Client по ID"""
        data = self.read()
        entity = self.get_by_id(client_id)
        if not entity:
            raise ValueError(f"Client с ID {client_id} не найден.")
        data.remove(entity)
        self.write(data)

    def get_count(self):
        """Получить количество объектов Client"""
        data = self.read()
        return len(data)
