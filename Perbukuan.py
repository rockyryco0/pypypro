import mysql.connector as mysql
import uuid
import sys
import re
import datetime
from os import system


db = mysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='tokobuku'
)


cursor = db.cursor(buffered=True)


def loginadmin():

    system('cls')
    print("""
                                        LOG IN ADMIN
    
==========================[TEKAN tombol ctrl+c untuk ke menu utama]==========================""")
    id_Admin = input("Masukkan ID admin : ")
    idadmin(id_Admin)

    if id_Admin in id_admin_log_in:
        halamanadmin()
    else:
        input("\n ID salah.")
        system('cls')
        main()


def idadmin(id_admin_login):

    global id_admin_log_in

    sql_admin = """select id_admin from admin where id_admin = %s"""
    cursor.execute(sql_admin, (id_admin_login, ))
    fetch = cursor.fetchall()

    for row in fetch:
        id_admin_log_in = row[0]


def halamanadmin():

    system('cls')
    print("""
    __  __      __                               ___    ____  __  ________   __
   / / / /___ _/ /___ _____ ___  ____ _____     /   |  / __ \/  |/  /  _/ | / /
  / /_/ / __ `/ / __ `/ __ `__ \/ __ `/ __ \   / /| | / / / / /|_/ // //  |/ /
 / __  / /_/ / / /_/ / / / / / / /_/ / / / /  / ___ |/ /_/ / /  / // // /|  /
/_/ /_/\__,_/_/\__,_/_/ /_/ /_/\__,_/_/ /_/  /_/  |_/_____/_/  /_/___/_/ |_/
    """)
    print("\n\n         MENU ADMIN\n\n"
              "[0] Edit tabel buku\n"
              "[1] Edit tabel pelanggan\n"
              "[2] Edit tabel pembelian\n"
              "[3] Tampilkan tabel buku\n"
              "[4] Tampilkan tabel pelanggan\n"
              "[5] Tampilkan tabel pembelian\n"
              "[6] Kembali\n")
    pilih = input(" Pilihan : ")
    if pilih == '0':
         edittabelbuku()
    elif pilih == '1':
         noneFunction()
    elif pilih == '2':
         noneFunction()
    elif pilih == '3':
         system('cls')
         tampilbukuadmin()
         halamanadmin()
    elif pilih == '4':
         system('cls')
         pelanggan()
         halamanadmin()
    elif pilih == '5':
         system('cls')
         pembelian()
         halamanadmin()
    elif pilih == '6':
         main()
    else:
         input('Pilihan salah!')
         halamanadmin()


def tampilbukuadmin():

    tampilbuku()
    input("\n\nTekan enter untuk kembali...")


def edittabelbuku():

    system('cls')
    print(" Menu edit buku \n")
    print("[0] Tambah buku\n"
          "[1] Hapus buku\n"
          "[2] Edit data buku ( Berdasarkan ID Buku ) \n"
          "[3] Kembali\n\n")
    pilih = input(" Pilihan : ")

    if pilih == '0':
        tambahbuku()
    elif pilih == '1':
        noneFunction()
    elif pilih == '2':
        adminBukuDBid()
        adminBukuDB()
    elif pilih == '3':
        halamanadmin()
    else:
        print('\n\nPilihan salah!')
        system('cls')
        edittabelbuku()


def tambahbuku():

    cursor = db.cursor(prepared=True)

    system('cls')
    print(" Tambah Buku \n\n")
    sql_tambah = """insert into buku (id_buku, judul_buku, stok_buku, harga) values(%s,%s,%s,%s)"""
    id_input = input("+ Masukkan ID Buku : ")
    judul_input = input("+ Masukkan Judul Buku : ")
    stok_input = input("+ Masukkan Stok Buku : ")
    harga_input = input("+ Masukkan Harga Buku : ")
    var = [(id_input, judul_input, stok_input, harga_input)]
    cursor.executemany(sql_tambah, var)
    db.commit()

    input("\n\nBuku berhasil ditambahkan...")
    system('cls')
    edittabelbuku()


def lanjutanadminBukuDB(IDB):

    cursor = db.cursor(prepared=True)

    global id_baru, fetcher

    #  Query ambil data
    sqli = """select * from buku where id_buku = %s"""
    cursor.execute(sqli, (IDB, ))
    fetcher = cursor.fetchall()

    for row in fetcher:
        id_baru = row[0].decode()


def adminBukuDBid():

    global id_buku_DB
    system('cls')

    try:
        id_buku_DB = input("Masukkan kode buku : \n")
        lanjutanadminBukuDB(id_buku_DB)

        if id_buku_DB in id_baru:
            pass
        else:
            input("Buku tidak tersedia!")
            system('cls')
            adminBukuDBid()
    except NameError:
        input("\n\nBuku tidak tersedia...")
        system('cls')
        adminBukuDBid()


def adminBukuDB():

    try:
        system('cls')
        cursor = db.cursor(prepared=True)


        sql_id = """select * from buku where id_buku = %s"""
        ide = id_buku_DB
        cursor.execute(sql_id, (ide, ))
        new = cursor.fetchall()

        for row in new:
            judul_buku1 = row[1].decode()
            harga_buku1 = row[2]
            stok_buku1 = row[3]

        print("""
        ==============================================
        ||             HALAMAN EDIT BUKU            ||
        ==============================================
        ||                                           
        ||                                            
        ||  >  Judul Buku  = """+judul_buku1+"""   
        ||  >  Harga Buku  = """+str(harga_buku1)+""" 
        ||  >  Stok Buku   = """+str(stok_buku1)+"""  
        ||                                            
        ||                                            
        ============================================== 
            
    [0] Kembali
    [1] Ubah Judul buku
    [2] Ubah Harga buku
    [3] Ubah Stok buku 
""")
        pilih = input(" Pilihan : ")
        if pilih == '0':
            system('cls')
            edittabelbuku()
        elif pilih == '1':
            sql_ubah_judul_buku = "update buku set id_buku = %s, judul_buku = %s where id_buku = %s"
            id_baru = input("Masukkan id baru : ")
            judul = input("Masukkan judul baru : ")
            id = id_buku_DB
            eksekusi = (id_baru, judul, id)
            cursor.execute(sql_ubah_judul_buku, eksekusi)
            db.commit()
            input("\n\nJudul buku berhasil diganti")
            adminBukuDB()
        elif pilih == '2':
            sql_ubah_harga_buku = "update buku set harga = %s where id_buku = %s"
            harga = input("Masukkan harga baru : ")
            id = id_buku_DB
            eksekusi = (harga, id)
            cursor.execute(sql_ubah_harga_buku, eksekusi)
            db.commit()
            input("\n\nHarga buku berhasil diganti")
            adminBukuDB()
        elif pilih == '3':
            sql_ubah_stok = "update buku set stok_buku = %s where id_buku = %s"
            stok = input("Masukkan stok baru : ")
            id = id_buku_DB
            eksekusi = (stok, id)
            cursor.execute(sql_ubah_stok, eksekusi)
            db.commit()
            input("\n\nJumlah stok berhasil diganti")
            adminBukuDB()
        else:
            print("\nPilihan salah!")
            input()
            system('cls')
            adminBukuDB()
    except NameError:
        input("Operasi gagal.")
        system('cls')
        adminBukuDB()


def login(id):

    global id_admin
    global username

    sql = """select * from admin where id_admin=%s"""
    cursor.execute(sql,(id, ))

    fetcher = cursor.fetchall()
    for row in fetcher:
        id_admin = row[0]
        username = row[1]


def akseslogin():

    global ID

    try:
        ID = input("ID : ")
        user = input("Username : ")
        print('\n\n')
        login(ID)

        if id == id_admin:
            print("Login sukses.")
            input("Tekan enter untuk lanjut...")
        elif user == username:
            print("Login sukses.")
            input("Tekan enter untuk lanjut...")
        else:
            print("ID atau username anda salah!")
            input("Tekan enter untuk kembali...")
            system('cls')
            main()

    except NameError:
        print("ID atau username anda salah!")
        input("Pastikan ID anda sudah terdaftar.")
        system('cls')
        main()


def tampilbuku():

    sql = """select * from buku"""
    cursor.execute(sql)
    fetcher = cursor.fetchall()

    print("\n")
    print("\t    DAFTAR BUKU\n\n".center(92))
    print("--------------------------------------------------------------------------------------------------")
    print("|  Kode Buku   |       "+"Nama Buku".center(20)+"      |       Harga Buku      |    Jumlah Stok Buku   |")
    print("--------------------------------------------------------------------------------------------------")
    print("-================================================================================================-")

    for row in fetcher:
        print('| ', row[0].center(10), ' |', row[1].center(30, ' '), ' |', str(row[2]).center(20), ' |', str(row[3]).center(20), ' |')
        print("-================================================================================================-")



def buku(ID, judul):

    global id_buku,judul_buku,harga,stok_buku

    cursor = db.cursor(prepared=True)
    sql = """select * from buku where id_buku=%s or judul_buku=%s"""
    cursor.execute(sql, (ID, judul))
    fetcher = cursor.fetchall()

    for row in fetcher:
        id_buku = row[0].decode()
        judul_buku = row[1].decode()
        harga = int(row[2])
        stok_buku = row[3]


def HalamanBeliBuku():

    print("\n\tHALAMAN PEMBELIAN BUKU \n")
    print("         Selamat Datang ".center(10)+nama_pel.capitalize())
    tampilbuku()

    lanjut = input("\n\n  0. Beli buku"
                   "\n  1. Kembali"
                   "\n  2. Lihat riwayat pembelian"
                   "\n\n Pilihan : ")

    if lanjut == '0':
        system('cls')
        prosesBeliBuku()
    elif lanjut == '1':
        system('cls')
        main()
    elif lanjut == '2':
        system('cls')
        riwayatbelibuku()
    else:
        print("Pilihan salah")
        input()
        system('cls')
        HalamanBeliBuku()


def riwayatbelibuku():

    cursor = db.cursor(prepared=True)

    sql = """select * from pembelian where kode_pembelian = %s"""
    kode_beli = input("Masukkan kode pembelian anda : ")
    cursor.execute(sql, (kode_beli, ))
    fetch_beli = cursor.fetchall()

    for row in fetch_beli:
        tanggal = row[1]
        namabuku = row[4].decode()
        jumlahbuku = row[5]
        hargabuku = row[6]

        print('\n-=======================================-')
        print("| Tanggal Pembelian  = ", str(tanggal))
        print('| Nama Buku          = ', str(namabuku.ljust(10)))
        print('| Jumlah Buku        = ', str(jumlahbuku).ljust(5))
        print('| Harga Buku         = ', str(hargabuku).ljust(6))

    input('\n\n Tekan enter untuk kembali...')
    system('cls')
    HalamanBeliBuku()


def prosesBeliBuku():

    global nako, kode, total, id_pelang, jumlah

    stringLength = 8
    randomString = uuid.uuid4().hex
    randomString = randomString.lower()[0:stringLength]
    kode = randomString
    date = datetime.datetime.now()
    tanggal_pem = date.strftime("%d/%m/%Y")
    print("-====================================================-")
    print("| Kode Pembelian    :", kode, '     '.rjust(7))
    print("| Tanggal Pembelian :", tanggal_pem)
    nako = input("| Nama/Kode buku    : ")

    buku(nako, nako)
    if nako == id_buku:
        print('| Nama buku         :', judul_buku)

    try:
        jumlah = int(input("| Jumlah            : "))
        print("|----------------------------------------------------|")
    except ValueError:
        input("\n\nMasukkan jumlah dengan benar!")
        system('cls')
        HalamanBeliBuku()

    total = int(harga*jumlah)
    if jumlah > stok_buku:
        print("\nJumlah pembelian melebihi stok buku!")
        input()
        system('cls')
        HalamanBeliBuku()

    if nako == id_buku:
        print("""| Total harga       : Rp. """+str(total)+"""
-====================================================-""")
        print("\n0. Beli"
              "\n1. Batal")
        lanjut = input("\n Pilihan : ")

        if lanjut == '0':
            eksekusibeli(jumlah, nako, nako)
            id_pelang = id_pel
            eksekusipembelian()
            print("\nPembelian Berhasil...")
            input()
            system('cls')
        elif lanjut == '1':
            system('cls')
            HalamanBeliBuku()
        else:
            input("Pembelian gagal...")
            system('cls')
            HalamanBeliBuku()

    elif nako == judul_buku:
        print("\n\nTotal harga : ", total)
        print("\n0. Beli"
              "\n1. Batal")
        lanjut = input("\n Pilihan : ")

        if lanjut == '0':
            eksekusibeli(jumlah, nako, nako)
            id_pelang = id_pel
            eksekusipembelian()
            print("\nPembelian Berhasil...")
            input()
            system('cls')
        elif lanjut == '1':
            system('cls')
            HalamanBeliBuku()
        else:
            input("Pembelian gagal...")
            system('cls')
            HalamanBeliBuku()

    elif nako != id_buku:
        print("\n\nBuku tidak tersedia...")
        input()
        system('cls')
        HalamanBeliBuku()
    elif nako != judul_buku:
        print("\n\nBuku tidak tersedia...")
        input()
        system('cls')
        HalamanBeliBuku()

    system('cls')
    lanjutan = input('\n\nLihat rincian transaksi?'
                     '\n0. Lihat'
                     '\n1. Menu utama'
                     '\n\n Pilihan : ')
    if lanjutan == '0':
        system('cls')
        print('\n-========================================================-')
        print('+ Kode Pembelian       : ', kode)
        print('+ Tanggal Pembelian    : ', tanggal_pem)
        print('+ Judul Buku           : ', judul_buku)
        print('+ Jumlah               : ', jumlah)
        print('+ Total Harga          : ', total)
        print('-========================================================-')

        input('\n\nTekan enter untuk kembali...')
        system('cls')
        HalamanBeliBuku()
    else:
        system('cls')
        HalamanBeliBuku()


def eksekusibeli(stok, id, judul):

    sql = """update buku set stok_buku = stok_buku-%s where id_buku = %s or judul_buku = %s"""
    cursor.execute(sql, (stok, id, judul ))

    db.commit()


def eksekusipembelian():

    cursor = db.cursor(prepared=True)
    date = datetime.datetime.now()
    tanggal_pem = date.strftime("%Y/%m/%d")
    sql = """INSERT INTO pembelian (kode_pembelian, tanggal_pembelian, id_pelanggan, nama_pelanggan, judul_buku, jumlah_buku, harga_total) values (%s,%s,%s,%s,%s,%s,%s)"""
    var = [(kode, tanggal_pem, id_pel, nama_pel, judul_buku, jumlah, total)]
    cursor.executemany(sql, var)

    db.commit()


def pelanggan():

    global id_pelangganan, nama_pelanggan, status_pelanggan

    cursor = db.cursor(prepared=True)
    sql = """select * from pelanggan"""
    cursor.execute(sql)
    fetcher = cursor.fetchall()


    print("Daftar nama pelanggan : \n")
    print("[id_pelanggan]   [nama_pelanggan]      [status_pelanggan]")
    for row in fetcher:
        id_pelangganan = row[0].decode()
        print(row[0].decode(),'\t\t  ', row[1].decode(),'\t       ', row[2].decode())

    input("\n\nTekan enter untuk kembali...")
    system('cls')


def Halamandaftarpelanggan():

    global id_daftar, nama_daftar, status_daftar

    try:

        sql_data_pelanggan = """select id_pelanggan from pelanggan"""
        cursor.execute(sql_data_pelanggan)

        fetch = cursor.fetchall()
        for row in fetch:
            id_data_pelanggan = row[0]

        system('cls')
        print("""           
                        DAFTAR PELANGGAN 
       
    Silahkan masukkan ID anda dengan format 4 digit angka
    contoh = '1234' 
        
    Gunakan ID yang mudah diingat!           
       
==========================[TEKAN tombol ctrl+c untuk ke menu utama]==========================""")
        id_daftar = input("+ Masukkan ID anda : ")
        if len(id_daftar) < 4:
            input("\nMasukkan ID anda dengan format 4 digit angka!")
            system('cls')
            Halamandaftarpelanggan()
        if len(id_daftar) > 4:
            input("\nMasukkan ID anda dengan format 4 digit angka!")
            system('cls')
            Halamandaftarpelanggan()
        if id_daftar == str:
            input("\nMasukkan ID anda dengan format 4 digit angka!")
            system('cls')
            Halamandaftarpelanggan()
        if id_daftar in id_data_pelanggan:
            print("\n\nID anda sudah terpakai.")
            input("Silahkan coba ID yang lain!")
            system('cls')
            Halamandaftarpelanggan()

        nama_daftar = input("+ Masukkan Nama anda : ")
        deteksi_nama = re.compile(r'\d')
        mo_nama = deteksi_nama.search(nama_daftar)
        if mo_nama:
            input("\nNama tidak boleh mengandung angka!")
            system('cls')
            Halamandaftarpelanggan()

        print("+ Pilih status pelanggan : ")
        print("\n[1] Pelanggan tetap      [2] Pelanggan tidak tetap       [3] Pelanggan harian        [4] Pelanggan bulanan       ")
        status_pilih = input("Pilih : ")
        if status_pilih == '1':
            status_daftar = 'Pelanggan tetap'
        elif status_pilih == '2':
            status_daftar = 'Pelanggan tidak tetap'
        elif status_pilih == '3':
            status_daftar = 'Pelanggan harian'
        elif status_pilih == '4':
            status_daftar = 'Pelanggan bulanan'
        else:
            input("\n Pilihan anda salah!")
            system('cls')
            Halamandaftarpelanggan()
        print('=============================================================================================\n\n')

        daftarpelanggan()
        print("\n\nPendaftaran berhasil.")
        input("Tekan enter untuk kembali...")
        main()
    except KeyboardInterrupt:
        system('cls')
        main()


def daftarpelanggan():

    cursor = db.cursor(prepared=True)

    sql_daftar = """INSERT INTO pelanggan (id_pelanggan, nama_pelanggan, status_pelanggan) values (%s,%s,%s)"""
    var = [id_daftar, nama_daftar, status_daftar]
    cursor.execute(sql_daftar, var)
    db.commit()


def loginpelanggan(id_pelanggan):


    global id_pelanggan_deteksi

    cursor = db.cursor(prepared=True)
    sql_login = """select * from pelanggan where id_pelanggan = %s"""
    cursor.execute(sql_login,(id_pelanggan, ))
    fetch = cursor.fetchall()

    for row in fetch:
        id_pelanggan_deteksi = row[0].decode()


def halamanloginpelanggan():

    global id_pel, nama_pel

    try:
        print("""
==========================[TEKAN tombol ctrl+c untuk ke menu utama]==========================""")
        id_pel = input("+ Masukkan ID anda : ")
        loginpelanggan(id_pel)

        if id_pel == id_pelanggan_deteksi:
            nama_pel = input("+ Masukkan Nama anda : ")
            input("\nAkses berhasil...")
            system('cls')
            HalamanBeliBuku()
        else:
            print('\n\nID salah.')
            input("Masukkan ID yang benar!")
            main()
    except NameError:
        print('\n\nID salah.')
        input("Masukkan ID yang benar!")
        main()
    except KeyboardInterrupt:
        system('cls')
        main()


def pembelian():

    sql = """select * from pembelian"""
    cursor.execute(sql)
    fetcher = cursor.fetchall()

    print('\n')
    print('\t       DAFTAR RIWAYAT PEMBELIAN \n\n'.center(100))
    print(" -----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print('|   Kode Pembelian   |   Tanggal Pembelian    |   ID Pelanggan   |     Nama Pelanggan    |            Nama Buku            |    Jumlah Buku   | Harga Buku  |')
    print(" -----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" -=========================================================================================================================================================-")


    for row in fetcher:
        print('|  ', row[0].center(15), ' |',str(row[1]).center(20), '  |', row[2].center(15, ' '), ' |', str(row[3]).center(20), ' |', str(row[4]).center(30), ' |', str(row[5]).center(15), ' |', str(row[6]).center(10), ' |')
        print(" -=========================================================================================================================================================-")


    input("\nTekan enter untuk kembali...")
    system('cls')


def noneFunction():

    system('cls')
    input("Fungsi belum dibuat...")
    main()


def main():

    system('cls')
    print(""" 

        SELAMAT DATANG DI TOKO BUKU VANCOUVER

[0] LOG IN Admin
[1] LOG IN Pelanggan
[2] Daftar buku
[3] Pendaftaran pelanggan
[4] Keluar
""")

    pilih = input(" Pilihan : ")

    if pilih == '0':
        loginadmin()
    elif pilih == '1':
        system('cls')
        halamanloginpelanggan()
    elif pilih == '2':
        system('cls')
        tampilbuku()
        input("\n\nTekan enter untuk kembali...")
        system('cls')
        main()
    elif pilih == '3':
        Halamandaftarpelanggan()
    elif pilih == '4':
        sys.exit()
    else:
        input("pilihan salah!")
        system('cls')
        main()


main()


