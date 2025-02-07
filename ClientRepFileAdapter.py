import ClientRepFile

class ClientRepFileAdapter:
    
    def __init__(self, client_rep_file: ClientRepFile):
        client_rep_file.read_data_from_file()
        self._client_rep_file = client_rep_file
    
    def get_k_n_short_list(self, k, n):
        return self._client_rep_file.get_k_n_short_list(k, n)
    
    def get_by_id(self, client_id):
        return self._client_rep_file.get_by_id(client_id)
    
    def delete_by_id(self, client_id):
        self._client_rep_file.delete_by_id(client_id)
        self._client_rep_file.write_data_to_file()
    
     def update_by_id(self, client_id, company_name, contact_person, email, phone, passport):
        self._client_rep_file.replace_by_id(client_id, company_name, contact_person, email, phone, passport)
        self._client_rep_file.write_data_to_file()
    
   def add(self, company_name, contact_person, email, phone, passport):
        self._client_rep_file.add_entity(company_name, contact_person, email, phone, passport)
        self._client_rep_file.write_data_to_file()
    
    def get_count(self):
        return self._client_rep_file.get_count()
