from tabulate import tabulate

data_karyawan = []

def tampilkan_data(karyawan_list):
    if not karyawan_list:
        print("Tidak ada data karyawan yang tersedia.")
        return
    
    headers = ["ID Karyawan", "Nama", "Jabatan", "Departemen", "Gaji","Pendidikan Terakhir"]
    data = [[k['id_karyawan'], k['nama'], k['jabatan'], k['departemen'], k['gaji'],k['pendidikan']] for k in karyawan_list]
    print(tabulate(data, headers=headers, tablefmt="grid"))
              
def buat_data_karyawan():
    while True:
        print("\n--- Menu Input Data Karyawan ---")
        print("1. Input Data Karyawan")
        print("2. Kembali ke Menu Utama")
        
        try:
            pilihan = int(input("Pilih opsi: "))
            if pilihan == 1:
                try:
                    id_karyawan = input("Masukkan ID Karyawan (KYW-XX): ")
                    id_duplikat = False
                    for karyawan in data_karyawan:
                        if karyawan['id_karyawan'] == id_karyawan:
                            id_duplikat = True
                            break
                    
                    if id_duplikat:
                        raise ValueError("Data sudah tersedia!")
                
                except ValueError as eror:
                    print(eror)
                    continue 
                
                nama = input("Masukkan Nama: ")
                jabatan = input("Masukkan Jabatan: ")
                departemen = input("Masukkan Departemen: ")
                gaji = int(input("Masukkan Gaji: "))
                pendidikan = input("Masukkan Pendidikan Terakhir: ")
                karyawan = {
                    'id_karyawan': id_karyawan,
                    'nama': nama,
                    'jabatan': jabatan,
                    'departemen': departemen,
                    'gaji': gaji,
                    'pendidikan': pendidikan,
                }
                
                while True:
                    try:
                        simpan = input("Simpan data karyawan ini? (ya/tidak): ").strip().lower()
                        if simpan not in ('ya', 'tidak'):
                            raise ValueError("Input tidak valid! Pilih 'ya' atau 'tidak'.")
                        if simpan == 'ya':
                            data_karyawan.append(karyawan)
                            print("Data karyawan berhasil disimpan!")
                        else:
                            print("Data tidak disimpan!")
                        break
                    except ValueError as eror:
                        print(eror)
                        continue
            elif pilihan == 2:
                return
            else:
                print("Opsi input yang anda masukkan tidak valid")
        except ValueError:
            print("Opsi input yang anda masukkan tidak valid")

def tampilkan_data_karyawan():
    while True:
        print("\n--- Menu Tampilan Data Karyawan ---")
        print("1. Tampilkan Seluruh Data Karyawan")
        print("2. Lihat Data Karyawan Spesifik")
        print("3. Kembali ke Menu Utama")
        
        try:
            pilihan = int(input("Pilih opsi: "))
            if pilihan == 1:
                if not data_karyawan:
                    print("Tidak ada data karyawan yang tersedia.")
                else:
                    tampilkan_data(data_karyawan)
            elif pilihan == 2:
                if not data_karyawan:
                    print("Tidak ada data karyawan yang tersedia.")
                    continue
                id_karyawan = input("Masukkan ID Karyawan (KYW-XX) yang ingin dilihat: ")
                karyawan = None
                for k in data_karyawan:
                    if k['id_karyawan'] == id_karyawan:
                        karyawan = k
                        break
                if karyawan:
                    tampilkan_data([karyawan]) 
                else:
                    print("Data karyawan tidak ditemukan.")   
            elif pilihan == 3:
                return 
            else:
                print("Opsi input yang anda masukkan tidak valid.")
        except ValueError:
            print("Opsi input yang anda masukkan tidak valid.")

def perbarui_data_karyawan():
    while True:
        print("\n--- Menu Update Data Karyawan ---")
        print("1. Update Data Karyawan")
        print("2. Kembali ke Menu Utama")

        try:
            pilihan = int(input("Pilih opsi: "))
            if pilihan == 1:
                id_karyawan = input("Masukkan ID Karyawan (KYW-XX) yang ingin diupdate: ")
                karyawan = None
                for k in data_karyawan:
                    if k['id_karyawan'] == id_karyawan:
                        karyawan = k
                        break
                if not karyawan:
                    print("Data karyawan tidak ditemukan.")
                    continue

                tampilkan_data([karyawan])
                lanjut = input("Ingin melanjutkan update data? (ya/tidak): ").strip().lower()
                if lanjut != 'ya':
                    continue
                while True:
                    kolom_pilihan = input("Masukkan nama kolom yang ingin diupdate (nama, jabatan, departemen, gaji, pendidikan): ").strip().lower()
                    if kolom_pilihan == 'id_karyawan':
                        print("Akses ditolak! ID Karyawan tidak dapat diubah.")
                        continue  
                    if kolom_pilihan in karyawan:
                        nilai_baru = input(f"Masukkan {kolom_pilihan} baru: ")
                        while True:
                            try:
                                simpan = input("Simpan perubahan? (ya/tidak): ").strip().lower()
                                if simpan not in ('ya', 'tidak'):
                                    raise ValueError("Input tidak valid! Pilih 'ya' atau 'tidak'.")
                                if simpan == 'ya':
                                    karyawan[kolom_pilihan] = nilai_baru
                                    print("Data karyawan berhasil diperbarui!")
                                else:
                                    print("Perubahan dibatalkan.")
                                return
                            except ValueError as eror:
                                print(eror)
                    else:
                        print("Kolom tidak valid. Silakan masukkan nama kolom yang benar.")
                
            elif pilihan == 2:
                return
            else:
                print("Opsi input yang Anda masukkan tidak valid.")
        except ValueError:
            print("Opsi input yang Anda masukkan tidak valid.")


def hapus_data_karyawan():
    while True:
        print("\n--- Menu Hapus Data Karyawan ---")
        print("1. Hapus Data Karyawan")
        print("2. Kembali ke Menu Utama")
        
        try:
            pilihan = int(input("Pilih opsi: "))
            if pilihan == 1:
                id_karyawan = input("Masukkan ID Karyawan (KYW-XX) yang ingin dihapus: ")
                karyawan = None
                for k in data_karyawan:
                    if k['id_karyawan'] == id_karyawan:
                        karyawan = k
                        break
                
                if not karyawan:
                    print("Data karyawan tidak ditemukan.")
                    continue
                
                tampilkan_data([karyawan])
                konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (ya/tidak): ").strip().lower()
                if konfirmasi == 'ya':
                    data_karyawan.remove(karyawan)
                    print("Data karyawan berhasil dihapus!")
                else:
                    print("Penghapusan dibatalkan.")
            elif pilihan == 2:
                return
            else:
                print("Opsi input yang anda masukkan tidak valid.")
        except ValueError:
            print("Opsi input yang anda masukkan tidak valid.")


def MulaiProgram():
    while True:
        print("\n--- Sistem Manajemen Database Karyawan PT Makmur Jaya ---")
        print("1. Tambah Data Karyawan")
        print("2. Tampilkan Data Karyawan")
        print("3. Perbarui Data Karyawan")
        print("4. Hapus Data Karyawan")
        print("5. Keluar Sistem")
        
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan < 1 or pilihan > 5:
                print("")
                print("Opsi input yang anda masukkan tidak valid")
        except ValueError:
            print("")
            print("Opsi input yang anda masukkan tidak valid")
            continue
        
        if pilihan == 1:
            buat_data_karyawan()
        elif pilihan == 2:
            tampilkan_data_karyawan()
        elif pilihan == 3:
            perbarui_data_karyawan()
        elif pilihan == 4:
            hapus_data_karyawan()
        elif pilihan == 5:
            print("Anda keluar dari sistem.")
            break

MulaiProgram()
