from database import connect

class ProductZaki:
    def __init__(self):
        self.conn = connect()
        self.cursor = self.conn.cursor()
    
    def show_zaki(self):
        # Menampilkan data dari tabel product_zaki
        print("\n=== Produk dari Tabel product_zaki ===")
        sql = "SELECT * FROM product_zaki"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)

        # Menampilkan data dari tabel motorcycles_zaki
        print("\n=== Produk dari Tabel motorcycles_zaki ===")
        sql = "SELECT * FROM motorcycles_zaki"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)

        # Menampilkan data dari tabel electric_motorcycles_zaki
        print("\n=== Produk dari Tabel electric_motorcycles_zaki ===")
        sql = "SELECT * FROM electric_motorcycles_zaki"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)
