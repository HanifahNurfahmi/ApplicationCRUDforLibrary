from datetime import datetime, timedelta, date

daftarbuku = {
    'A0001':{'nama' : 'Matahari','pengarang' : 'Tere Liye','penerbit' : 'Gramedia','tahun': '2016','stok' : 3},
    'A0002':{'nama' : 'Ekonomi','pengarang' : 'S. Sukirno','penerbit' : 'Bina Grafika','tahun': '1982','stok' : 2},
    'A0003':{'nama' : 'Kalkulus','pengarang' : 'Purcell','penerbit' : 'Erlangga','tahun': '2004','stok' : 1},
    'A0004':{'nama' : 'Bulan','pengarang' : 'Tere Liye','penerbit' : 'Erlangga','tahun': '2015','stok' : 3},
    'A0005':{'nama' : 'Koala Kumal','pengarang' : 'Raditya Dika','penerbit' : 'Gagas Media','tahun': '2015','stok' : 2}}

## Menu 1 : Menampilkan Daftar Buku
def readbuku():
    while True:
        menu1 = input('''
            ==================== Menu 1 ====================
                1. Menampilkan Seluruh Koleksi Buku
                2. Menampilkan Koleksi Buku tertentu
                3. Kembali ke Menu Utama
            
            Masukkan menu yang ingin dijalankan : ''')
        if menu1 == '1':
            if len(daftarbuku) != 0:
                seluruhbuku()
            else:
                print('Maaf Tidak Ada Daftar Buku yang tersedia')
        elif menu1 == '2':
            if len(daftarbuku) != 0:
                bukutertentu()
            else:
                print('Maaf Tidak Ada Daftar Buku yang tersedia')
        elif menu1 == '3':
            break
        else :
            print('\nMenu yang anda pilih tidak tersedia.')

def seluruhbuku():
    print('\nDaftar Koleksi Buku Perpusnas : ')
    print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
    for kodebuku in daftarbuku.keys():
        print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')

def bukutertentu():
    print('\nMencari Buku Berdasarkan Kode Buku')
    kodebuku = str(input('Masukkan Kode Buku : ').upper())
    if kodebuku in daftarbuku.keys():
        print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
        print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
    else:
        print('Maaf Kode Buku Tidak Ada ')


## 2. Menambahkan Daftar Buku
def createbuku():
    while True:
        menu2 = input('''
        ==================== Menu 2 ====================
            1. Menambahkan Buku
            2. Kembali ke Menu Utama
        
        Masukkan menu yang ingin dijalankan : ''')
        
        if  menu2 == '1' :
            tambahbuku()
        elif menu2 == '2' : 
            break
        else :
            print('\nMenu yang anda pilih tidak tersedia.')

def tambahbuku():
    kodebuku = str(input('Masukkan Kode Buku : ').upper())
    if kodebuku in daftarbuku.keys() :
        print('\nKode buku sudah ada. \nMasukkan kode lain.')
    else:
        print('\nKode buku belum ada. \nLengkapi data buku. \n')
        nama = str(input('Masukkan Nama Buku : ').capitalize())
        pengarang = str(input('Masukkan Nama Pengarang : ').capitalize())
        penerbit = str(input('Masukkan Nama Penerbit : ').capitalize())
        tahun = input('Masukkan Tahun Terbit : ')
        stok = int(input('Masukkan Stok Buku : '))
        bukubaru = {kodebuku: {'nama':'','pengarang':'','penerbit':'','tahun':'', 'stok': ''}}
        bukubaru[kodebuku] ={}
        bukubaru[kodebuku]['nama'] = nama
        bukubaru[kodebuku]['pengarang'] = pengarang
        bukubaru[kodebuku]['penerbit'] = penerbit
        bukubaru[kodebuku]['tahun'] = tahun
        bukubaru[kodebuku]['stok'] = stok
        print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
        print(kodebuku,'\t\t|',bukubaru[kodebuku]['nama'],'\t\t|',bukubaru[kodebuku]['pengarang'],'\t\t|',bukubaru[kodebuku]['penerbit'],'\t\t|',bukubaru[kodebuku]['tahun'],'\t\t|',bukubaru[kodebuku]['stok'],'\t\t|')
        while True :
            iyatidak = str(input('Apakah anda ingin menyimpan data ini? (Y/T) ').upper())
            if iyatidak == 'Y' :
                daftarbuku.update(bukubaru)
                print('\nData tersimpan.')
                break
            elif iyatidak == 'T' :
                print('\nData Tidak Tersimpan.')
                break
            else:
                print('\nInput anda salah. \nPilih Y atau T')
                break


## 3. Mangubah Daftar Buku
def updatebuku():
    while True:
        menu3 = input('''
        ==================== Menu 3 ====================
            1. Mengubah data Buku
            2. Kembali ke Menu Utama
            
            Masukkan menu yang ingin dijalankan : ''')
        
        if  menu3 == '1' :
            ubahbuku()
        elif menu3 == '2' : 
            break
        else :
            print('\nMenu yang anda pilih tidak tersedia.')

def ubahbuku():
    seluruhbuku()
    kodebuku = str(input('\n\nMasukkan Kode Buku : ').upper())
    if kodebuku in daftarbuku.keys() :
        print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
        print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
        while True:
            print('''
            Pilih menu yang ingin di ubah :
                1. Nama Buku
                2. Nama Pengarang
                3. Nama Penerbit
                4. Tahun Terbit
                5. Stok Buku''')
            menuedit = input('\nMasukkan kolom yang ingin diedit : ')
            
            if menuedit == '1':
                yakinubah = str(input('\nApakah anda yakin ingin mengubah nama buku ini? (Y/T) ').upper())
                if yakinubah == 'Y':
                    namabaru = input('Masukkan nama buku yang baru : ')
                    daftarbuku[kodebuku]['nama'] = namabaru
                    print('\nData berhasil diubah')
                    print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
                    print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
                    break
                elif yakinubah == 'T':
                    break
                else:
                    print('\nInput anda salah. \nPilih Y atau T')
                    break
            
            elif menuedit == '2':
                yakinubah = str(input('\nApakah anda yakin ingin mengubah pengarang buku ini? (Y/T) ').upper())
                if yakinubah == 'Y':
                    pengarangbaru = input('Masukkan pengarang buku yang baru : ')
                    daftarbuku[kodebuku]['pengarang'] = pengarangbaru
                    print('\nData berhasil diubah')
                    print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
                    print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
                    break
                elif yakinubah == 'T':
                    break
                else:
                    print('\nInput anda salah. \nPilih Y atau T')
                    break
            
            elif menuedit == '3':
                yakinubah = str(input('\nApakah anda yakin ingin mengubah penerbit buku ini? (Y/T) ').upper())
                if yakinubah == 'Y':
                    penerbitbaru = input('Masukkan penerbit buku yang baru : ')
                    daftarbuku[kodebuku]['penerbit'] = penerbitbaru
                    print('\nData berhasil diubah')
                    print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
                    print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
                    break
                elif yakinubah == 'T':
                    break
                else:
                    print('\nInput anda salah. \nPilih Y atau T')
                    break

            elif menuedit == '4':
                yakinubah = str(input('\nApakah anda yakin ingin mengubah tahun terbit buku ini? (Y/T) ').upper())
                if yakinubah == 'Y':
                    tahunbaru = input('Masukkan tahun terbit buku yang baru : ')
                    daftarbuku[kodebuku]['tahun'] = tahunbaru
                    print('\nData berhasil diubah')
                    print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
                    print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
                    break
                elif yakinubah == 'T':
                    break
                else:
                    print('\nInput anda salah. \nPilih Y atau T')
                    break

            elif menuedit == '5':
                yakinubah = str(input('\nApakah anda yakin ingin mengubah stok buku ini? (Y/T) ').upper())
                if yakinubah == 'Y':
                    stokbaru = int(input('Masukkan stok buku yang baru : '))
                    daftarbuku[kodebuku]['stok'] = stokbaru
                    print('\nData berhasil diubah')
                    print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
                    print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
                    break
                elif yakinubah == 'T':
                    break
                else:
                    print('\nInput anda salah. \nPilih Y atau T')
                    break
            else:
                print('\nMenu yang anda pilih tidak tersedia.')                            
    else:
        print('Data yang anda cari tidak ditemukan')        


## 4. Menghapus Daftar Buku
def deletebuku():
    while True:
        menu4 = input('''
        ==================== Menu 4 ====================
    
            1. Menghapus Seluruh Koleksi Buku
            2. Menghapus Koleksi Buku tertentu
            3. Kembali ke Menu Utama
        
        Masukkan menu yang ingin dijalankan : ''')
        
        if menu4 == '1':
            hapussemuabuku()
        elif menu4 == '2':
            hapusbukutertentu()
        elif menu4 == '3':
            break
        else:
            print('\nMenu yang anda pilih tidak tersedia.')

def hapussemuabuku():
    while True :
        yakinhapus = str(input('Apakah anda yakin ingin menghapus seluruh daftar buku? (Y/T) ').upper())
        if yakinhapus == 'Y' :
            daftarbuku.clear()
            print('\nSeluruh daftar buku telah terhapus.')
            break
        elif yakinhapus == 'T' :
            print('\nSeluruh daftar buku TIDAK terhapus.')
            break
        else:
            print('\nInput anda salah. \nPilih Y atau T')
            break

def hapusbukutertentu():
    kodebuku = str(input('Masukkan Kode Buku : ').upper())
    if kodebuku in daftarbuku.keys():
        print('Kode Buku\t| Nama Buku\t\t| Pengarang\t\t| Penerbit\t\t| Tahun Terbit\t| Stok Buku\t|')
        print(kodebuku,'\t\t|',daftarbuku[kodebuku]['nama'],'\t\t|',daftarbuku[kodebuku]['pengarang'],'\t\t|',daftarbuku[kodebuku]['penerbit'],'\t\t|',daftarbuku[kodebuku]['tahun'],'\t\t|',daftarbuku[kodebuku]['stok'],'\t\t|')
        while True:
            yakinhapus = str(input('Apakah anda yakin ingin menghapus buku ini? (Y/T) ').upper())
            if yakinhapus == 'Y' :
                daftarbuku.pop(kodebuku)
                print('\nBuku telah terhapus.')
                break
            elif yakinhapus == 'T' :
                print('\nBuku tidak terhapus.')
                break
            else:
                print('\nInput anda salah. \nPilih Y atau T')
                break
    else:
        print('Data yang anda cari tidak ditemukan')


## 5. Meminjam Buku
def no():
    while True:
        nomor  = input('Masukkan No Anggota  (10 digit) :') 
        if len(nomor) < 10 :
            print('Nomor yang anda masukkan kurang')
        elif len(nomor) > 10 :
            print('Nomor yang anda masukkan lebih')
        else:
            return nomor

def buku():
    x = str(input('Masukkan kode buku yang akan dipinjam : ').upper())
    y = int(input('Masukkan jumlah buku yang akan dipinjam : '))
    for i in daftarbuku.keys():
        if i == x:
            return x,   daftarbuku[x]['nama'],      y
        else:
            print('Data Tidak Ada')

def pinjambuku():
        pinjam = (datetime.now()).replace(microsecond=0)
        kembali = date.today() + timedelta(days=7)
        num = no()
        nama    = str(input('Masukkan Nama Anggota :').upper())
        Id, judul, jumlah = buku()

        print(f'''
                        Bukti Peminjaman Koleksi Perpusnas
                ------------------------------------------------
                No Anggota      : {num}
                Nama Anggota    : {nama}
                Tgl Pinjam      : {pinjam}
                Tgl Hrs Kembali : {kembali}
                ------------------------------------------------
                Item ID     Judul                       Jml
                {Id}\t {judul}\t\t {jumlah}
                ------------------------------------------------
                
                Kembalikan koleksi tepat waktu untuk menghindari
                suspensi pelayanan berupa denda

                                Terima Kasih,
                Perpustakaan Nasional Republik Indonesia
        ''')


## 6. Menu
while True:
    menu = input('''
        Selamat Datang di Perputakaan Nasional Indonesia
        
            1. Menampilkan Daftar Buku
            2. Menambahkan Daftar Buku
            3. Mengubah Daftar Buku
            4. Menghapus Daftar Buku
            5. Meminjam Buku
            6. Keluar dari Program

        Masukkan menu yang akan dijalankan : ''')

    if  menu == '1' :
        readbuku()
    elif menu == '2' :
        createbuku()
    elif menu == '3' :
        updatebuku()
    elif menu == '4' :
        deletebuku()
    elif menu == '5' :
        pinjambuku()
    elif menu == '6' :
        print('\n \t****Terima Kasih Telah Berkunjung ke Perpusnas****\n')
        break
    else:
        print('\nMaaf menu yang anda masukkan salah. \nSilahkan masukkan menu yang tertera.')
