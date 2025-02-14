import psycopg2
from uuid import uuid4

class DatabaseConnection:
    """Класс для управления подключением к базе данных (Singleton)."""
    _instance = None
    
    def __new__(cls, db_config):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize(db_config)
        return cls._instance
    
    def _initialize(self, db_config):
        self.connection = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        self.connection.autocommit = True
        self.ensure_table_exists()
    
    def get_cursor(self):
        return self.connection.cursor()
    
    def table_exists(self, table_name):
        """Проверяет, существует ли таблица в базе данных."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM pg_catalog.pg_tables
                    WHERE tablename = %s
                );
            """, (table_name,))
            result = cursor.fetchone()
        return result[0]
    
    def ensure_table_exists(self):
        """Убеждается, что таблица client существует, и создает её при необходимости."""
        if not self.table_exists("client"):
            with self.get_cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE client (
                        client_id UUID PRIMARY KEY,
                        company_name VARCHAR(255) NOT NULL,
                        contact_person VARCHAR(255) NOT NULL,
                        phone VARCHAR(15) NOT NULL,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        passport VARCHAR(255) NOT NULL
                    );
                """)
                print("Таблица 'client' успешно создана.")
        else:
            print("Таблица 'client' уже существует.")

    def add_client(self, company_name, contact_person, phone, email, passport):
        """Добавляет нового клиента в таблицу."""
        client_id = str(uuid4())  # Генерация уникального UUID
        with self.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO client (client_id, company_name, contact_person, phone, email, passport)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (client_id, company_name, contact_person, phone, email, passport))
            print(f"Клиент {company_name} успешно добавлен.")

    def get_client_by_id(self, client_id):
        """Получает клиента по ID."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT * FROM client WHERE client_id = %s;
            """, (client_id,))
            result = cursor.fetchone()
        return result

    def update_client(self, client_id, company_name=None, contact_person=None, phone=None, email=None, passport=None):
        """Обновляет данные клиента."""
        updates = []
        params = []
        if company_name:
            updates.append("company_name = %s")
            params.append(company_name)
        if contact_person:
            updates.append("contact_person = %s")
            params.append(contact_person)
        if phone:
            updates.append("phone = %s")
            params.append(phone)
        if email:
            updates.append("email = %s")
            params.append(email)
        if passport:
            updates.append("passport = %s")
            params.append(passport)
        
        if updates:
            query = f"UPDATE client SET {', '.join(updates)} WHERE client_id = %s;"
            params.append(client_id)
            with self.get_cursor() as cursor:
                cursor.execute(query, tuple(params))
                print(f"Данные клиента {client_id} обновлены.")

    def delete_client(self, client_id):
        """Удаляет клиента по ID."""
        with self.get_cursor() as cursor:
            cursor.execute("""
                DELETE FROM client WHERE client_id = %s;
            """, (client_id,))
            print(f"Клиент {client_id} удален.")
