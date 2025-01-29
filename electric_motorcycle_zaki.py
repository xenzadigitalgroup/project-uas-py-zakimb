# class ProductZaki agar bisa digunakan sebagai parent class
from product_zaki import ProductZaki

# MotorCycleZaki mewarisi (inheritance) dari ProductZaki
class ElectricMotorCycleZaki(ProductZaki):
    # Memanggil konstruktor dari parent class (ProductZaki)
    def __init__(self):
        super().__init__()

    # Menggunakan atribut self.cursor dan self.conn yang diwarisi dari ProductZaki
    def add_zaki(self, id_product, name, price, battery, mileage):
        sql = "INSERT INTO electric_motorcycles_zaki (id_product, name, price, battery, mileage) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (id_product, name, price, battery, mileage))
        self.conn.commit()
