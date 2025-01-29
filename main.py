# Code build by ZAKI MUSHTHAFA BILLAH
# Email zakimb@technovagroupinc.com
# Kelas IF-1
# BP 23101152630041

from customer_zaki import CustomerZaki
from product_zaki import ProductZaki
from motorcycle_zaki import MotorCycleZaki
from electric_motorcycle_zaki import ElectricMotorCycleZaki
from order_zaki import OrderZaki
from prettytable import PrettyTable  # Import PrettyTable

COPYRIGHT = "© 2025 zakimb@technovagroupinc.com - All rights reserved."

def show_copyright():
    print("\n" + "-" * len(COPYRIGHT))
    print(COPYRIGHT)
    print("-" * len(COPYRIGHT))

def kelola_customer():
    customer = CustomerZaki()
    while True:
        show_copyright()
        print("\n=== Kelola Customer ===")
        print("1. Tambah Customer")
        print("2. Update Customer")
        print("3. Hapus Customer")
        print("4. Lihat Semua Customer")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                cus_id = int(input("Masukkan ID Customer: "))
                cus_name = input("Masukkan Nama Customer: ")
                customer.add_zaki(cus_id, cus_name)
                print("Customer berhasil ditambahkan!")
            elif pilihan == "2":
                cus_id = int(input("Masukkan ID Customer yang akan diupdate: "))
                cus_name = input("Masukkan Nama Baru: ")
                customer.update_zaki(cus_id, cus_name)
                print("Customer berhasil diupdate!")
            elif pilihan == "3":
                cus_id = int(input("Masukkan ID Customer yang akan dihapus: "))
                customer.delete_zaki(cus_id)
                print("Customer berhasil dihapus!")
            elif pilihan == "4":
                customer.show_zaki()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka untuk ID!")

def kelola_produk():
    product = ProductZaki()
    while True:
        show_copyright()
        print("\n=== Kelola Produk ===")
        print("1. Lihat Semua Produk")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            product.show_zaki()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")

def kelola_order():
    order = OrderZaki()
    while True:
        show_copyright()
        print("\n=== Kelola Order ===")
        print("1. Tambah Order")
        print("2. Update Order")
        print("3. Hapus Order")
        print("4. Lihat Semua Order")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                order_id = int(input("Masukkan ID Order: "))
                order_date = input("Masukkan Tanggal Order (YYYY-MM-DD): ")
                customer_id = int(input("Masukkan ID Customer: "))
                product_name = input("Masukkan Nama Produk: ")
                order.add_zaki(order_id, customer_id, product_name, order_date)
                print("Order berhasil ditambahkan!")
            elif pilihan == "2":
                order_id = int(input("Masukkan ID Order yang akan diupdate: "))
                order_date = input("Masukkan Tanggal Baru (YYYY-MM-DD): ")
                order.updateorder_zaki(order_id, order_date)
                print("Order berhasil diupdate!")
            elif pilihan == "3":
                order_id = int(input("Masukkan ID Order yang akan dihapus: "))
                order.delete_zaki(order_id)
                print("Order berhasil dihapus!")
            elif pilihan == "4":
                order.listorder_zaki()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka untuk ID!")

def main():
    while True:
        show_copyright()
        print("\n=== Menu Program Zaki ===")
        print("1. Kelola Customer")
        print("2. Kelola Produk")
        print("3. Kelola Order")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kelola_customer()
        elif pilihan == "2":
            kelola_produk()
        elif pilihan == "3":
            kelola_order()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
