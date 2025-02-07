import os
from ClientRepFileStrategy import ClientRepFileStrategy

# Класс, который использует стратегию для работы с файлами
class ClientRepFile:
    
    def __init__(self, strategy: ClientRepFileStrategy):
        self._data = []
        self._strategy = strategy
        
    def write_data_to_file(self):
        self._strategy.write(self._data)
        
    def read_data_from_file(self):
        self._data = self._strategy.read()

    def add_entity(self, first_name, last_name, email, gender, phone, disease):
        """Добавить нового клиента в список с новым id"""
    new_id = max([entry['id'] for entry in self._data], default=0) + 1  
        new_entity = {
            'client_id': new_id,
            'company_name': company_name,
            'contact_person': contact_person,
            'phone': phone,
            'email': email,
            'passport': passport
        }
        # Проверка на уникальность почты
       if any(entry['email'] == email for entry in self._data):
            raise ValueError('Email должен быть уникальным!')     
        # Добавляем нового клиента в список
          self._data.append(new_entity)
    
    def get_by_id(self, client_id):
        """Получить клиента по ID"""
           for entry in self._data:
            if entry['client_id'] == client_id:
                return entry
        return None  # Если объект не найден
    
    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов"""
        start = (n - 1) * k
        end = start + k
        return self._data[start:end]
    
    def sort_by_field(self, field):
        """Сортировать элементы по выбранному полю"""
        if field in ["company_name", "contact_person", "phone", "email", "passport"]:
        self._data.sort(key=lambda x: x.get(field))
        return self._data
    
    def replace_by_id(self, client_id, company_name, contact_person, phone, email, passport):
        """Заменить данные клиента по ID"""
        entity = self.get_by_id(client_id)
        if not entity:
            raise ValueError(f"Клиент с ID {client_id} не найден.")
        # Проверка на уникальность почты
        if email and email != entity['email'] and any(entry['email'] == email for entry in self._data):
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
      
    
    def delete_by_id(self, client_id):
        """Удалить клиента по ID"""
        entity = self.get_by_id(client_id)
        if not entity:
            raise ValueError(f"Клиент с ID {client_id} не найден.")
       self._data.remove(entity)
    
    def get_count(self):
        """Получить количество клиентов"""
        return len(self._data)
    

