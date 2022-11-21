def pembatas():
    print("-"*46)
def pembatas2():
    print("="*46)

tampunganBarang = []

def menu():
    while True:
        pembatas()
        print(" Mine.CO ".center(46,"="))
        pembatas()
        print("0. Catalogue Product")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Edit Barang")
        print("4. Daftar Barang")
        print("5. Cek Barang")
        print("6. Exit App")

        pembatas()
        pilihanMenu = input("Pilih Menu :")
        if pilihanMenu == "0" or pilihanMenu == "Catalogue Product":
            catalogueToko()
        elif pilihanMenu == "1" or pilihanMenu == "Tambah Barang":
            tambahBarang()
        elif pilihanMenu == "2" or pilihanMenu == "Hapus Barang":
            hapusBarang()
        elif pilihanMenu == "3" or pilihanMenu == "Edit Barang":
            editBarang()
        elif pilihanMenu == "4" or pilihanMenu == "Daftar Barang":
            daftarBarang()
        elif pilihanMenu == "5" or pilihanMenu == "Cek Barang":
            cekBarang()
        elif pilihanMenu == "6" or pilihanMenu == "Exit App":
            pembatas()
            print("Terima Kasih Telah Berkunjung Ke Mine.CO".center(46,"-"))
            exit()
        else:
            print("Pilihan yang Anda Masukkan Salah, Silakan Masukkan Pilihan Lagi")
        
        pembatas()


listToko = {
    1:"Blouse",
    2:"Blazer",
    3:"Pants",
    4:"Kemeja",
    5:"Belt",
}

list_warna = {
    1:"Biru",
    2:"Nude",
    3:"Milo",
    4:"Pink",   
    5:"Abu"
}

daftar_harga = {
    1: 90000,
    2: 160000,
    3: 115000,
    4: 120000,
    5: 130000
}

catalogueToko = []

def catalogueToko() :
    pembatas()
    print(" Catalogue Mine.CO ".center(46,"="))
    pembatas()
    print("|ID".center(5, ' '), "|Product".center(15, ' '), "|Warna".center(8, ' '), "|Harga".center(8, ' '), "\n" )
    for i in catalogueToko:
        print("|",(listToko.index(i+1)),"\t | " ,listToko(i) |"\t ",list_warna(i) | "\t ",daftar_harga(i),"|")

def is_duplicate():
    anylist = input('Masukkan Nama Produk : ')
    if type(anylist) != listToko:
        print("Data duplikat")
    else:
        tambahBarang()

def menambahCatalogue() :
    pembatas()
    print(" Penambahan Catalogue ".center(46,"="))
    pembatas()
   # is_duplicate() tidak berfungsi
    listToko = input('Masukkan Nama Produk : ')
    list_warna = (input('Masukkan Warna Produk : '))
    daftar_harga = int(input('Masukkan Harga Produk : '))
    listToko.append()
    list_warna.append()
    daftar_harga.append()

def simpan():
    simpan = input ("Anda ingin menyimpan data? (y/n) :")
    if simpan == "y":
        print("Data tersimpan")
    elif simpan == "n":
        print("Data tidak tersimpan")
    else:
        daftarBarang()

def tambahBarang():
    pembatas()
    print(" Penambahan Barang ".center(46,"="))
    pembatas()
    while True:
        barang = input ("Masukkan Barang : ")
        is_duplicate()
        tampunganBarang.append(barang)
        print(f'Barang ["{barang}"] Berhasil Ditambahkan')
        pilihan = input("Anda ingin menambahkan barang lagi? (y/n): ")
        if pilihan == "y":
            pembatas()
            print("Daftar Barang ".center(46,"*"))
            pembatas()
            print("Kode".center(18, ' '), "Nama Barang".center(30, ' '), "\n")
            for i in tampunganBarang:
                print("|      ",(tampunganBarang.index(i)+1), "          |", (i).center(22, ' '),"|")
            pembatas2()
            simpan()
        else:
            return
        

#next 1 untuk kembali ke menu dari menu hapus
def next():
    lanjut =input('''Tekan y Jika Ingin Melanjutkan Program,
    Tekan n Untuk Kembali ke Menu: ''').lower()
    if lanjut == "y":
        hapusBarang()
    elif lanjut == "n":
        menu()
    else:
        print("Inputan salah, Program kembali ke Menu")
        menu()

#next 2 untuk kembali ke menu dari edit barang
def next2():
    lanjut =input('''Tekan Y jika ingin melanjutkan program,
    Tekan N untuk kembali ke Menu": ''')
    if lanjut == "y":
        editBarang()
    elif lanjut == "n":
        menu()
    else:
        print("Inputan salah, Program kembali ke Menu")
        menu()

#next 3 untuk kembali ke menu dari menu cek daftar barang
def next3():
    lanjut =input('''Tekan Y jika ingin melanjutkan program,
    Tekan N untuk kembali ke Menu: ''')
    if lanjut == "y":
        pass 
    elif lanjut == "n":
        menu()
    else:
        print("Inputan salah, Program kembali ke Menu")
        menu()


def hapusBarang():
    pembatas()
    print(" Menghapus Barang ".center(46,"="))
    pembatas()
    while True:
        hapus = input("Masukkan Nama Barang Yang Ingin Dihapus: ")
        if hapus in tampunganBarang:
            tampunganBarang.remove(hapus)
            print(f'Barang ["{hapus}"] Berhasil Dihapus')
            next()
        else:
            print(f'Barang ["{hapus}"] Tidak Tersedia')
            next()

def editBarang():
    pembatas()
    print(" Daftar Barang ".center(46,"="))
    pembatas()
    for i in tampunganBarang:
        print("|      ",(tampunganBarang.index(i)+1), "          |", (i).center(22, ' '),"|")
    while True:
        pembatas()
        print("Edit Barang ".center(46,"="))
        pembatas()
        cariBarang = str(input("Masukkan Nama Barang Yang Ingin Diedit: "))
        if cariBarang in tampunganBarang:
            ubahKe = input("Ubah Menjadi:")
            tampunganBarang[tampunganBarang.index(cariBarang)] = ubahKe
            for i in tampunganBarang:
                print("| Kode ".center(18," "), (tampunganBarang.index(i)+1) ,"|", (i).center(22, ' '),"|")
            pembatas()
            print(f'Barang ["{cariBarang}"] Berhasil Diubah Menjadi ["{ubahKe}"]')
            pembatas2()
            next2()

#menampilkan daftar barang

def daftarBarang():
    pembatas()
    print(" Daftar Barang ".center(46,"="))
    pembatas()
    print("Kode".center(18, ' '), "Nama Barang".center(30, ' '), "\n")
    for i in tampunganBarang:
        print("|      ",(tampunganBarang.index(i)+1), "          |", (i).center(22, ' '),"|")
    pembatas2()
    exit = input("Tekan y Untuk Keluar :")
    if exit == "y":
        menu()
    else:
        menu()

#cek barang
def cekBarang():
    pembatas()
    print(" Daftar Barang ".center(46,"="))
    pembatas()
    cek = input("Masukkan Nama Barang Yang Dicari:")
    if cek in tampunganBarang:
        print(f'Barang ["{cek}"] Tersedia')
    else:
         print(f'Barang ["{cek}"] Tidak Tersedia')
    next3()

menu()