import os

# Data barang
barang_toko = [
    {"id": "BRG001", "nama": "Sabun Mandi", "kategori": "Kebutuhan Sehari-hari", "harga": 5000, "jumlah terjual": 20},
    {"id": "BRG002", "nama": "Beras 5kg", "kategori": "Makanan", "harga": 60000, "jumlah terjual": 10}
]

# Kategori yang diperbolehkan
kategori_tersedia = ["Kebutuhan Sehari-hari", "Pakaian", "Makanan", "Lainnya"]

users = {"admin": "admin123", "kasir": "kasir123"}
current_user = None

# Login
def login():
    global current_user
    attempts = 5
    while attempts > 0:
        username = input("Masukkan username Anda: ")
        password = input("Masukkan password: ")
        if username in users and users[username] == password:
            current_user = username
            print(f"Login berhasil! Selamat datang, {username}\n")
            return True
        else:
            attempts -= 1
            print(f"Login gagal! Periksa username dan password. Sisa percobaan: {attempts}\n")
    print("Anda telah gagal login sebanyak 5 kali. Aplikasi akan keluar.\n")
    exit()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Read
def tampilkan_barang():
    """ Menampilkan seluruh barang yang tersedia """
    clear_screen()
    print("\nDaftar Barang di Toko:\n")
    print("ID       Nama              Kategori                 Harga       Jumlah Terjual")
    print("-" * 60)
    for barang in barang_toko:
        print(f"{barang['id']:8} {barang['nama']:18} {barang['kategori']:20} Rp{barang['harga']:8}  {barang['jumlah terjual']:5}")
    input("\nTekan Enter untuk kembali...")

# Create
def tambah_barang():
    """ Menambahkan barang baru ke dalam daftar """
    clear_screen()
    print("Tambah Barang Baru")
    id_barang = input("Masukkan ID Barang: ")
    nama = input("Masukkan Nama Barang: ")
    
    print("Kategori yang tersedia:")
    for i, kategori in enumerate(kategori_tersedia, 1):
        print(f"{i}. {kategori}")
    kategori_index = int(input("Pilih kategori (1-{}): ".format(len(kategori_tersedia))))
    kategori = kategori_tersedia[kategori_index - 1]
    
    harga = int(input("Masukkan Harga Barang: "))
    jumlah_terjual = int(input("Masukkan Jumlah Barang Terjual: "))
    
    barang_toko.append({"id": id_barang, "nama": nama, "kategori": kategori, "harga": harga, "jumlah terjual": jumlah_terjual})
    print("\nBarang berhasil ditambahkan!")
    input("\nTekan Enter untuk kembali...")

# Update
def update_barang():
    """ Memperbarui informasi barang berdasarkan ID """
    clear_screen()
    id_barang = input("Masukkan ID Barang yang ingin diupdate: ")
    for barang in barang_toko:
        if barang["id"] == id_barang:
            barang["harga"] = int(input(f"Masukkan Harga Baru (Saat ini: {barang['harga']}): "))
            barang["jumlah terjual"] = int(input(f"Masukkan Jumlah Terjual Baru (Saat ini: {barang['jumlah terjual']}): "))
            print("\nData barang berhasil diperbarui!")
            input("\nTekan Enter untuk kembali...")
            return
    print("Barang dengan ID tersebut tidak ditemukan!")
    input("\nTekan Enter untuk kembali...")

# Delete
def hapus_barang():
    """ Menghapus barang berdasarkan ID """
    clear_screen()
    id_barang = input("Masukkan ID Barang yang ingin dihapus: ")
    for barang in barang_toko:
        if barang["id"] == id_barang:
            barang_toko.remove(barang)
            print("\nBarang berhasil dihapus!")
            input("\nTekan Enter untuk kembali...")
            return
    print("Barang dengan ID tersebut tidak ditemukan!")
    input("\nTekan Enter untuk kembali...")

def cari_barang():
    """ Mencari barang berdasarkan ID atau nama """
    clear_screen()
    kata_kunci = input("Masukkan ID atau Nama Barang: ").lower()
    print("\nHasil Pencarian:\n")
    print("ID       Nama              Kategori                 Harga       Jumlah Terjual")
    print("-" * 60)
    ditemukan = False
    for barang in barang_toko:
        if kata_kunci in barang["id"].lower() or kata_kunci in barang["nama"].lower():
            print(f"{barang['id']:8} {barang['nama']:18} {barang['kategori']:20} Rp{barang['harga']:8}  {barang['jumlah terjual']:5}")
            ditemukan = True
    if not ditemukan:
        print("Tidak ada barang yang cocok dengan pencarian!")
    input("\nTekan Enter untuk kembali...")

def menu():
    login()
    while True:
        clear_screen()
        print("\nSistem Manajemen Penjualan Barang Toko")
        print("1. Tampilkan Barang")
        print("2. Tambah Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Cari Barang")
        print("6. Keluar")
        pilihan = input("\nPilih menu (1-6): ")
        
        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            update_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            cari_barang()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            input("Pilihan tidak valid! Tekan Enter untuk coba lagi...")

if __name__ == "__main__":
    menu()
