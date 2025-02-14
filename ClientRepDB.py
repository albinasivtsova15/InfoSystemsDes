import uuid
from DatabaseConnection import DatabaseConnection

class ClientRepDB:
    """Класс для управления сущностью patient."""
    def __init__(self, db_config):
     self.db = DatabaseConnection(db_config)
    
    def get_by_id(self, client_id):
        """Получить клиента по ID."""
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM client WHERE id = %s", (client_id,))
            result = cursor.fetchone()
        return result
    
    def get_k_n_short_list(self, k, n):
        """Получить список из k клиентов, начиная с n-го блока."""
        with self.db.get_cursor() as cursor:
            offset = k * (n - 1)
            cursor.execute("""
                SELECT id, company_name, contact_person, phone, email, passport 
                FROM client
                ORDER BY id LIMIT %s OFFSET %s
            """, (k, offset))
            result = cursor.fetchall()
        return result
    
    def add(self, company_name, contact_person, email, phone, passport):
        """Добавить нового клиента."""
        new_id = str(uuid.uuid4())
         with self.db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO client (id, company_name, contact_person, email, phone, passport)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (new_id, company_name, contact_person, email, phone, passport))
        return new_id
   
    def update_by_id(self, client_id, company_name=None, contact_person=None, email=None, phone=None, passport=None):
        """Обновить данные клиента по ID."""
        fields = []
        values = []
        if company_name is not None:
            fields.append("company_name = %s")
            values.append(company_name)
        if contact_person is not None:
            fields.append("contact_person = %s")
            values.append(contact_person)
        if email is not None:
            fields.append("email = %s")
            values.append(email)
        if phone is not None:
            fields.append("phone = %s")
            values.append(phone)
        if passport is not None:
            fields.append("passport = %s")
            values.append(passport)
        
        if not fields:
            return  # Если нечего обновлять
        
        values.append(client_id)
           with self.db.get_cursor() as cursor:
            cursor.execute(f"""
                UPDATE client
                SET {', '.join(fields)}
                WHERE id = %s
            """, tuple(values))
    
    def delete_by_id(self, client_id):
        """Удалить клиента по ID."""
       with self.db.get_cursor() as cursor:
            cursor.execute("DELETE FROM client WHERE id = %s", (client_id,))
    
    def get_count(self):
        """Получить количество клиентов."""
        with self.db.get_cursor() as cursor:       
            cursor.execute("SELECT COUNT(*) FROM client")
            result = cursor.fetchone()
        return result[0]
