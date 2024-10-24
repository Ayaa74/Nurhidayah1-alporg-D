# Nurhidayah

# Daftar makanan dan harga
menu = {
    1: ("Nasi Goreng", 20000),
    2: ("Mie Ayam", 15000),
    3: ("Sate Ayam", 25000),
    4: ("Bakso", 30000),
}

def tampilkan_menu():
    print("Menu Makanan:")
    for nomor, (nama, harga) in menu.items():
        print(f"{nomor}. {nama} - Rp{harga}")

def pemesanan_makanan():
    while True:
        tampilkan_menu()
        
        # Input pilihan makanan
        try:
            pilihan = int(input("Masukkan nomor makanan yang diinginkan: "))
            if pilihan not in menu:
                print("Pilihan tidak valid. Silakan coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue
        
        # Input jumlah porsi
        try:
            jumlah = int(input("Masukkan jumlah porsi: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari nol. Silakan coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue
        
        # Hitung total harga
        nama_makanan, harga = menu[pilihan]
        total_harga = harga * jumlah
        
        # Tampilkan konfirmasi
        print(f"\nPesanan Anda:")
        print(f"Makanan: {nama_makanan}")
        print(f"Jumlah: {jumlah}")
        print(f"Total Harga: Rp{total_harga}")
        
        konfirmasi = input("Apakah Anda ingin mengonfirmasi pesanan? (ya/tidak): ").strip().lower()
        if konfirmasi == "ya":
            print("Pesanan telah disimpan. Terima kasih!")
            break
        else:
            print("Silakan lakukan pemesanan lagi.")

# Jalankan fungsi pemesanan
pemesanan_makanan()
