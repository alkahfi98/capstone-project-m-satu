from tabulate import tabulate
from colorama import Fore,Style
import datetime
import time 
import threading
import pyinputplus as pyip


print(Fore.YELLOW + "*****Bandara Internasional Purwadhika*****" + Style.RESET_ALL)

info_penerbangan = []
info_maskapai = ['Lion', 'Garuda', 'Sriwijaya']
rute_domestik = {
        'Lion': ['Jakarta', 'Bali'],
        'Garuda': ['Makassar', 'Bali'],
        'Sriwijaya': ['Jakarta', 'Makassar']
    }
rute_internasional = {
        'Lion': ['Singapore', 'Malaysia'],
        'Garuda': ['Thailand', 'Malaysia'],
        'Sriwijaya': ['Singapore', 'Thailand']
    }
terminal_maskapai = {
        'Lion': 'Terminal 1',
        'Garuda': 'Terminal 2',
        'Sriwijaya': 'Terminal 3'
    }

terminal_maskapai_domestik = {
    'Lion': 'Terminal 1',
    'Garuda': 'Terminal 2',
    'Sriwijaya': 'Terminal 3'
}

terminal_maskapai_internasional = {
    'Lion': 'Terminal 1',
    'Garuda': 'Terminal 2',
    'Sriwijaya': 'Terminal 3'
}

def user():
    while True:
        print(Fore.YELLOW+"\n--- Anda adalah? ---\n"+Style.RESET_ALL)
        print("1. Manager")
        print("2. Passenger")
        print("3. Exit Program")

        pilihan = input("Masukkan pilihan (1-3): ")
        
        if pilihan == '1':
            manager_login()
        elif pilihan == '2':
            passenger_menu()
        elif pilihan == '3':
            print(Fore.BLUE + "Exit Program" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi." + Style.RESET_ALL)          

def manager_login():
    id_manager = "Kahfiganteng"
    pass_manager = "admin1234"
    
    user_id = pyip.inputStr(prompt="Masukkan ID Manager: ")
    user_pass = pyip.inputPassword(prompt="Masukkan Password: ")
    
    if user_id == id_manager and user_pass == pass_manager:
        print(Fore.GREEN + "Login berhasil sebagai Manager!" + Style.RESET_ALL)
        bandara() 
    else:
        print(Fore.RED + "ID atau Password salah. Coba lagi." + Style.RESET_ALL)
        return
    
def passenger_menu():
    while True:
        print(Fore.YELLOW + "\n--- Menu Passenger ---\n" + Style.RESET_ALL)
        print("1. Lihat info penerbangan")
        print("2. Lihat Maskapai, Rute, Terminal")
        print("3. Sorting Maskapai, Rute, Terminal")
        print("4. Kembali ke menu user\n")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            melihat_info_penerbangan()
        elif pilihan == '2':
            melihat_info_maskapai()
        elif pilihan == '3':
            sorting_data_maskapai()
        elif pilihan == '4':
            return  
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi." + Style.RESET_ALL)
                

def menu_info_penerbangan():
        while True:
            print(Fore.YELLOW + "\n--- Menu Info Penerbangan ---\n" + Style.RESET_ALL)
            print("1. Lihat info penerbangan")
            print("2. Tambah info penerbangan")
            print("3. Hapus info penerbangan")
            print("4. Ubah info penerbangan")
            print("5. Kembali ke menu Bandara\n")
            pilihan = input("Masukkan pilihan (1-5): ")
            if pilihan == '1':
                melihat_info_penerbangan()
            elif pilihan == '2':
                tambah_data_penerbangan()
            elif pilihan == '3':
                hapus_data_penerbangan()
            elif pilihan == '4':
                ubah_data_penerbangan()
            elif pilihan == '5':
                return  
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi." + Style.RESET_ALL)


def menu_info_maskapai_rute_terminal():
        while True:
            print(Fore.YELLOW + "\n--- Menu Maskapai, Rute, dan Terminal ---\n" + Style.RESET_ALL)
            print("1. Tampilkan Maskapai, Rute, Terminal")
            print("2. Tambah data Maskapai, Rute, Terminal")
            print("3. Hapus data Maskapai, Rute, Terminal")
            print("4. Ubah data Maskapai, Rute, Terminal")
            print("5. Sorting data Maskapai, Rute, Terminal")
            print("6. Kembali ke menu Bandara\n")
            
            pilihan = input("Masukkan pilihan (1-6): ")

            if pilihan == '1':
                melihat_info_maskapai()
            elif pilihan == '2':
                tambah_data_maskapai()
            elif pilihan == '3':
                hapus_data_maskapai()
            elif pilihan == '4':
                ubah_data_maskapai()
            elif pilihan == '5':
                sorting_data_maskapai()
            elif pilihan == '6':
                return  
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi." + Style.RESET_ALL)


def melihat_info_penerbangan ():
        if info_penerbangan:  
            table = tabulate(info_penerbangan, headers=["Nomor","Maskapai", "Kode Pesawat", "Tujuan","Tanggal", "Waktu Tiba", "Waktu Berangkat", "Keterangan", "Gate"])
            print(table)
        else:
            print(Fore.RED + "Tidak ada data penerbangan." + Style.RESET_ALL)

def tambah_data_penerbangan():
    nomor_penerbangan = len(info_penerbangan) + 1
    maskapai = input("Masukkan nama maskapai: ")
    kode_pesawat = input("Masukkan kode pesawat: ")

    for penerbangan in info_penerbangan:
        if penerbangan[1] == maskapai and penerbangan[2] == kode_pesawat:
            print(Fore.RED + "Data maskapai dan kode pesawat sudah ada. Silakan coba lagi." + Style.RESET_ALL)
            return  

    tujuan = input("Masukkan tujuan: ")
    tanggal_sekarang = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"Tanggal penerbangan: {tanggal_sekarang}")

    waktu_sekarang = datetime.datetime.now()
    waktu_tiba = waktu_sekarang.strftime("%H:%M")
    print(f"Waktu tiba: {waktu_tiba}")

    waktu_berangkat = (waktu_sekarang + datetime.timedelta(minutes=30)).strftime("%H:%M")
    print(f"Waktu berangkat: {waktu_berangkat}")

    keterangan = "Landing"
    print(f"Keterangan: {keterangan}")

    gate = input("Masukkan gate: ")

    info_penerbangan.append([nomor_penerbangan, maskapai, kode_pesawat, tujuan, tanggal_sekarang, waktu_tiba, waktu_berangkat, keterangan, gate])
    print(Fore.GREEN + "Data telah ditambahkan.\n" + Style.RESET_ALL)

    melihat_info_penerbangan()

    t = threading.Thread(target=update_keterangan_otomatis, args=(nomor_penerbangan - 1, waktu_sekarang))
    t.start()

def update_keterangan_otomatis(index,waktu_tiba):
    time.sleep(10 * 60)  
    info_penerbangan[index][7] = "Boarding"
    time.sleep(20 * 60)  
    info_penerbangan[index][7] = "Take off"

def ubah_data_penerbangan():
        if not info_penerbangan:
            print(Fore.RED + "Tidak ada data penerbangan yang dapat diubah." + Style.RESET_ALL)
            return  
        melihat_info_penerbangan()
        try:
            index = int(input("Masukkan nomor penerbangan yang ingin diubah: ")) - 1  
            if 0 <= index < len(info_penerbangan):
                while True:
                    print(Fore.YELLOW + "\nPilih kolom yang ingin diubah: \n" + Style.RESET_ALL)
                    print("1. Maskapai")
                    print("2. Kode Pesawat")
                    print("3. Tujuan")
                    print("4. Gate")
                    print("5. Selesai\n")
                    
                    pilihan_kolom = input("Masukkan pilihan (1-8): ")

                    if pilihan_kolom == '1':
                        info_penerbangan[index][1] = input("Masukkan nama maskapai baru: ")
                    elif pilihan_kolom == '2':
                        info_penerbangan[index][2] = input("Masukkan kode pesawat baru: ")
                    elif pilihan_kolom == '3':
                        info_penerbangan[index][3] = input("Masukkan tujuan baru: ")
                    elif pilihan_kolom == '4':
                        info_penerbangan[index][8] = input("Masukkan gate baru: ")
                    elif pilihan_kolom == '5':
                        print(Fore.GREEN + "Data telah diperbarui." + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nomor tidak valid!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Masukkan nomor yang valid!" + Style.RESET_ALL)

def hapus_data_penerbangan():
    if not info_penerbangan:
        print(Fore.RED + "Tidak ada data penerbangan yang dapat dihapus." + Style.RESET_ALL)
        return 
    melihat_info_penerbangan()
    index = pyip.inputNum("Masukkan nomor penerbangan yang ingin dihapus: ", min=1, lessThan=len(info_penerbangan) + 1) - 1  
    konfirmasi = pyip.inputYesNo(f"Anda yakin ingin menghapus penerbangan nomor {index + 1}? (yes/no): ")
    if konfirmasi == 'yes':
        del info_penerbangan[index]
        for i, penerbangan in enumerate(info_penerbangan, start=1):
            penerbangan[0] = i 
        print(Fore.GREEN + "Data penerbangan berhasil dihapus dan nomor urut diperbarui." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Penghapusan dibatalkan." + Style.RESET_ALL)

def melihat_info_maskapai():
    print(Fore.YELLOW + "\nPilih rute:\n" + Style.RESET_ALL)
    print("1. Domestik")
    print("2. Internasional\n")
    jenis_rute = input("Masukkan pilihan (1/2): ")

    if jenis_rute == '1':
        data_rute = rute_domestik
        terminal_data = terminal_maskapai_domestik
    elif jenis_rute == '2':
        data_rute = rute_internasional
        terminal_data = terminal_maskapai_internasional
    else:
        print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)
        return

    tabel_data = []
    for maskapai, rute in data_rute.items():
        terminal = terminal_data.get(maskapai, 'Unknown')
        tabel_data.append([maskapai, ', '.join(rute), terminal])

    print(tabulate(tabel_data, headers=["Maskapai", "Rute", "Terminal"]))


def tampilkan_tabel_maskapai(jenis_rute):
    if jenis_rute == '1':
        data_rute = rute_domestik
        terminal_data = terminal_maskapai_domestik
    else:
        data_rute = rute_internasional
        terminal_data = terminal_maskapai_internasional
    
    tabel_data = []
    for maskapai, rute in data_rute.items():
        terminal = terminal_data.get(maskapai, 'Unknown')  
        tabel_data.append([maskapai, ', '.join(rute), terminal])  
    print(tabulate(tabel_data, headers=["Maskapai", "Rute", "Terminal"]))
    return data_rute, terminal_data

def tambah_data_maskapai():
    print(Fore.YELLOW + "\nPilih rute untuk ditambahkan:\n" + Style.RESET_ALL)
    print("1. Domestik")
    print("2. Internasional\n")
    jenis_rute = input("Masukkan pilihan (1/2): ")

    if jenis_rute not in ['1', '2']:
        print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)
        return
    maskapai = input("Masukkan nama maskapai: ")
    if (jenis_rute == '1' and maskapai in rute_domestik) or (jenis_rute == '2' and maskapai in rute_internasional):
        print(Fore.RED + f"Maskapai {maskapai} sudah ada dalam data. Tidak bisa ditambahkan." + Style.RESET_ALL)
        return
    rute_baru = input("Masukkan rute baru (pisahkan dengan koma jika lebih dari satu): ").split(",")
    terminal = input("Masukkan terminal (angka): ")

    if jenis_rute == '1':
        rute_domestik[maskapai] = rute_baru
        terminal_maskapai_domestik[maskapai] = f"Terminal {terminal}"
    else:
        rute_internasional[maskapai] = rute_baru
        terminal_maskapai_internasional[maskapai] = f"Terminal {terminal}"

    terminal_maskapai[maskapai] = f"Terminal {terminal}"
    print(Fore.GREEN + "Data maskapai berhasil ditambahkan." + Style.RESET_ALL)


def ubah_data_maskapai():
    print(Fore.YELLOW + "\nPilih rute untuk diubah:\n" + Style.RESET_ALL)
    print("1. Domestik")
    print("2. Internasional\n")
    jenis_rute = input("Masukkan pilihan (1/2): ")

    if jenis_rute == '1':
        data_rute = rute_domestik
        terminal_data = terminal_maskapai_domestik
    elif jenis_rute == '2':
        data_rute = rute_internasional
        terminal_data = terminal_maskapai_internasional
    else:
        print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)
        return

    tabel_data = []
    for maskapai, rute in data_rute.items():
        terminal = terminal_data.get(maskapai, 'Unknown')
        tabel_data.append([maskapai, ', '.join(rute), terminal])

    print(tabulate(tabel_data, headers=["Maskapai", "Rute", "Terminal"]))

    maskapai = input("Masukkan nama maskapai yang ingin diubah: ")
    if maskapai in data_rute:
        while True:
            print(Fore.YELLOW + "\nPilih kolom yang ingin diubah:\n" + Style.RESET_ALL)
            print("1. Rute")
            print("2. Terminal")
            print("3. Selesai\n")
            
            pilihan_kolom = input("Masukkan pilihan (1-3): \n")
            
            if pilihan_kolom == '1':
                rute_baru = input("Masukkan rute baru (pisahkan dengan koma jika lebih dari satu): ").split(",")
                data_rute[maskapai] = rute_baru
                print(Fore.GREEN + "Rute berhasil diubah." + Style.RESET_ALL)
            elif pilihan_kolom == '2':
                terminal_baru = input("Masukkan terminal baru: ")
                terminal_data[maskapai] = f"Terminal {terminal_baru}"
                print(Fore.GREEN + "Terminal berhasil diubah." + Style.RESET_ALL)
            elif pilihan_kolom == '3':
                break
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi." + Style.RESET_ALL)


        print(Fore.GREEN + "Data maskapai berhasil diperbarui." + Style.RESET_ALL)
        return  
    else:
        print(Fore.RED + "Maskapai tidak ditemukan." + Style.RESET_ALL)


def hapus_data_maskapai():
    print(Fore.YELLOW + "\nPilih rute untuk dihapus:\n" +Style.RESET_ALL)
    print("1. Domestik")
    print("2. Internasional\n")

    jenis_rute = input("Masukkan pilihan (1/2): \n")
    if jenis_rute == '1':
        data_rute = rute_domestik
        terminal_maskapai = terminal_maskapai_domestik
        print(Fore.BLUE + "Rute Domestik:" + Style.RESET_ALL)
    elif jenis_rute == '2':
        data_rute = rute_internasional
        terminal_maskapai = terminal_maskapai_internasional
        print(Fore.BLUE + "Rute Internasional:" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)
        return

    tabel_data = []
    for maskapai, rute in data_rute.items():
        tabel_data.append([maskapai, ', '.join(rute), terminal_maskapai.get(maskapai, 'Unknown')])
    print(tabulate(tabel_data, headers=["Maskapai", "Rute", "Terminal"]))
    maskapai = input("Masukkan nama maskapai yang ingin dihapus: ")
    if maskapai in data_rute:
        konfirmasi = pyip.inputYesNo(f"Anda yakin ingin menghapus maskapai {maskapai}? (yes/no): ")
        
        if konfirmasi == 'yes':
            del data_rute[maskapai]  
            del terminal_maskapai[maskapai]  
            print(Fore.GREEN + f"Data maskapai {maskapai} berhasil dihapus" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Penghapusan dibatalkan." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Maskapai tidak ditemukan." + Style.RESET_ALL)


def sorting_data_maskapai():
    print(Fore.YELLOW + "\nPilih rute untuk diurutkan:\n" + Style.RESET_ALL),
    print("1. Domestik")
    print("2. Internasional\n")
    jenis_rute = input("Masukkan pilihan (1/2): \n")

    if jenis_rute == '1':
        data_rute = rute_domestik
        terminal_data = terminal_maskapai_domestik
    elif jenis_rute == '2':
        data_rute = rute_internasional
        terminal_data = terminal_maskapai_internasional
    else:
        print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)
        return
    
    print(Fore.YELLOW +"\nUrutkan berdasarkan:\n" + Style.RESET_ALL),
    print("1. Maskapai")
    print("2. Rute")
    print("3. Terminal\n")
    kolom = input("Masukkan pilihan (1-3): ")

    tabel_data = []
    for maskapai, rute in data_rute.items():
        terminal = terminal_data.get(maskapai, 'Unknown').replace('Terminal ', '')
        tabel_data.append([maskapai, ', '.join(rute), terminal])

    if kolom == "1":
        sorted_data = sorted(tabel_data, key=lambda x: x[0])  
    elif kolom == "2":
        sorted_data = sorted(tabel_data, key=lambda x: x[1])  
    elif kolom == "3":
        try:
            sorted_data = sorted(tabel_data, key=lambda x: int(x[2])) 
        except ValueError:
            print(Fore.RED + "Terjadi kesalahan saat mengurutkan terminal. Pastikan semua terminal adalah angka." + Style.RESET_ALL)
            return
    else:
        print(Fore.RED + "Pilihan tidak valid." + Style.RESET_ALL)
        return

    print(tabulate(sorted_data, headers=["Maskapai", "Rute", "Terminal"]))


def bandara():
        while True:
            print(Fore.YELLOW + "\n --- Menu Utama ---\n" +Style.RESET_ALL)
            print("1.Info Penerbangan")
            print('2.Maskapai dan Tujuan yang tersedia')
            print('3.Kembali ke menu user\n')
            menu_penerbangan = pyip.inputInt("Masukkan pilihan (1-3): ", min=1, max=3)
            if menu_penerbangan == 1:
                menu_info_penerbangan()  
            elif menu_penerbangan == 2:
                menu_info_maskapai_rute_terminal()  
            elif menu_penerbangan == 3:
                print(Fore.BLUE + "Kembali ke user" + Style.RESET_ALL)
                break 

user()
