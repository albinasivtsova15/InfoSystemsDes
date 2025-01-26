import os
from ClientRepFileStrategy import ClientRepFileStrategy

# Класс, который использует стратегию для работы с файлами
class ClientRepFile:
    
    def __init__(self, strategy: ClientRepFileStrategy):
        self.strategy = strategy
    
    def get_all(self):
        """Получить все элементы"""
        return self.strategy.read()
    
    def add_entity(self, company_name, contact_person, phone, email, passport):      
        """Добавить нового клиента в список с новым ID"""
        # Чтение данных из файла
        data = self.strategy.read()
        # Генерация нового ID
        new_id = max([entry['client_id'] for entry in data], default=0) + 1   
        new_entity = {
            'client_id': new_id,
            'company_name': company_name,
            'contact_person': contact_person,
            'phone': phone,
            'email': email,
            'passport': passport
        }
        # Проверка на уникальность почты
        if any(entry['email'] == email for entry in data):
            raise ValueError('Email должен быть уникальным!')       
        # Добавляем нового клиента в список
        data.append(new_entity)      
        # Записываем обновленные данные в файл
        self.strategy.write(data)
    
    def get_by_id(self, client_id):
        """Получить клиента по ID"""
        data = self.strategy.read()
        for entry in data:
            if entry['client_id'] == client_id:
                return entry
        return None  # Если объект не найден
    
    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов"""
        data = self.strategy.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]
    
    def sort_by_field(self, field):
        """Сортировать элементы по выбранному полю"""
        data = self.strategy.read()
        if field in ["company_name", "contact_person", "phone", "email", "passport"]:
            data.sort(key=lambda x: x.get(field))
        return data
    
    def replace_by_id(self, client_id, company_name, contact_person, phone, email, passport):
        """Заменить данные клиента по ID"""
        data = self.strategy.read()
        entity = self.get_by_id(client_id)
        if not entity:
            raise ValueError(f"Клиент с ID {client_id} не найден.")
        # Проверка на уникальность почты
        if email and email != entity['email'] and any(entry['email'] == email for entry in data):
            raise ValueError('Email должен быть уникальным!')
        # Обновляем данные
        if company_name:
            entity['company_name'] = company_name
        if contact_person:
            entity['contact_person'] = contact_person
        if email is not None:
            entity['email'] = email
        if phone:
            entity['phone'] = phone
        if passport:
            entity['passport'] = passport
        # Записываем обновленные данные в файл
        self.strategy.write(data)
    
    def delete_by_id(self, client_id):
        """Удалить клиента по ID"""
        data = self.strategy.read()
        entity = self.get_by_id(client_id)
        if not entity:
            raise ValueError(f"Клиент с ID {client_id} не найден.")
        data.remove(entity)
        self.strategy.write(data)
    
    def get_count(self):
        """Получить количество клиентов"""
        data = self.strategy.read()
        return len(data)
