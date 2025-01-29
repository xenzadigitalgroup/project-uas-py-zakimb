from product_zaki import ProductZaki

class MotorCycleZaki(ProductZaki):
    def __init__(self):
        super().__init__()

    def add_zaki(self, id_product, name, price, cylinder, tank_capacity):
        sql = "INSERT INTO product_zaki (id_product, name, price, cylinder, tank_capacity) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (id_product, name, price, cylinder, tank_capacity))
        self.conn.commit()