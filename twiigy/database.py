from tinydb import TinyDB
from tinydb.table import Document

class Database:
    def __init__(self):
        self.db = TinyDB("twiigy.db.json")

    def insert(self, table, data):
        table = self.db.table(table)
        table.insert(data)

    def insert_with_id(self, table, document):
        table = self.db.table(table)
        table.insert(document)

    def get(self, table, query):
        table = self.db.table(table)
        return table.search(query)

    def update(self, table, query, data):
        table = self.db.table(table)
        table.update(data, query)

    def delete(self, table, query):
        table = self.db.table(table)
        table.remove(query)

    def all(self, table):
        table = self.db.table(table)
        return table.all()

class PulseDatabase(Database):
    def __init__(self):
        super().__init__()
        self.table = "pulse"

    def insert_pulse(self, data):
        document = Document(data, doc_id = data["id"])
        self.insert_with_id(self.table, document)

    def get_pulse(self, query):
        return self.get(self.table, query)

    def update_pulse(self, query, data):
        self.update(self.table, query, data)

    def delete_pulse(self, query):
        self.delete(self.table, query)

    def all_pulse(self):
        return self.all(self.table)