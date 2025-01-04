Berikut adalah program Python sesuai dengan permintaan Anda:

# Program pengecekan rentang angka berdasarkan NIM
nim_awal = 2
nim_akhir = 6

# Masukkan angka
angka = int(input(f"Masukkan angka antara {nim_awal} dan {nim_akhir}: "))

# Mengecek apakah angka dalam rentang NIM
if nim_akhir <= angka <= nim_awal:
    print(f"Angka {angka} berada dalam rentang {nim_awal} dan {nim_akhir}.")
    
    # Operasi logika
    or_true = nim_akhir | True
    or_false = nim_akhir | False
    and_true = nim_akhir & True
    and_false = nim_akhir & False
    xor_true = nim_akhir ^ True
    xor_false = nim_akhir ^ False

    # Output hasil
    print(f"Jika nilai akhir di OR-kan dengan True maka: {or_true}")
    print(f"Jika nilai akhir di OR-kan dengan False maka: {or_false}")
    print(f"Jika nilai akhir di AND-kan dengan True maka: {and_true}")
    print(f"Jika nilai akhir di AND-kan dengan False maka: {and_false}")
    print(f"Jika nilai akhir di XOR-kan dengan True maka: {xor_true}")
    print(f"Jika nilai akhir di XOR-kan dengan False maka: {xor_false}")
else:
    print(f"Angka {angka} tidak berada dalam rentang {nim_awal} dan {nim_akhir}.")

Penjelasan Program:

1. Input Rentang:

nim_awal = 2 dan nim_akhir = 6.

Program meminta pengguna memasukkan angka yang akan dicek.



2. Pengecekan Rentang:

Pastikan angka berada dalam rentang nim_akhir hingga nim_awal.



3. Operasi Logika:

Melakukan operasi OR, AND, dan XOR pada nim_akhir (6) dengan True dan False.



4. Output:

Program menampilkan hasil dari operasi logika berdasarkan angka yang diberikan.




Anda dapat mengganti nilai nim_awal dan nim_akhir sesuai kebutuhan!