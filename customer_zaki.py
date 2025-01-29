from database import connect
from prettytable import PrettyTable  # Import PrettyTable

class CustomerZaki:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()

    def add_zaki(self, cus_id, cus_name):
        sql = "INSERT INTO customers_zaki (cus_id, cus_name) VALUES (%s, %s)"
        self.cursor.execute(sql, (cus_id, cus_name))
        self.conn.commit()

    def update_zaki(self, cus_id, cus_name):
        sql = "UPDATE customers_zaki SET cus_name = %s WHERE cus_id = %s"
        self.cursor.execute(sql, (cus_name, cus_id))
        self.conn.commit()

    def delete_zaki(self, cus_id):
        sql = "DELETE FROM customers_zaki WHERE cus_id = %s"
        self.cursor.execute(sql, (cus_id,))
        self.conn.commit()

    def show_zaki(self):
        sql = "SELECT * FROM customers_zaki"
        self.cursor.execute(sql)

        # Membuat objek tabel
        table = PrettyTable()
        table.field_names = ["ID Customer", "Nama Customer"]

        # Menambahkan baris data ke dalam tabel
        for row in self.cursor.fetchall():
            table.add_row(row)

        # Menampilkan tabel
        print(table)
