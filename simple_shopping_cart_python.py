'''
=================================================
Graded Challenge 1

Nama  : Fazrin Muhammad

Program ini dibuat untuk membuat simulasi shopping cart. Dimana anda dapat menambahkan barang ke dalam keranjang, menampilkan barang dikeranjang,
menghapus barang di keranjang, dan menghitung total harga yang ada di keranjang
=================================================
'''

class CartItem:                                                                                
    '''
    class CartItem digunakan untuk menunjukan objek barang/item dengan atribut nama dan harga
    '''
    def __init__(self, nama_item, harga_item):
        '''
        fungsi ini ditunjukan untuk membuat objek dengan variable nama_item dan harga_item
        '''                                                            
        self.nama_item = nama_item                                                             #Membuat atribut self.nama_item
        self.harga_item = harga_item                                                           #Membuat atribut self.harga_item


class ShoppingCart(CartItem):
    '''
    class ShoppingCart digunakan untuk sebuah objek keranjang belanja tiap orang
    '''
    def __init__(self):
        '''
        fungsi ini digunakan untuk membuat objek pada ShoppingCart
        '''
        self.list_item = []                                                                  #Membuat self.list_item untuk menyimpan barang

    def tambah_item(self, item):
        '''
        fungsi ini digunakan untuk menambahkan barang/item yang diinput
        '''
        tambah = self.list_item.append(item)                                                 #Variable tambah untuk menambahkan barang/item ke list self.list_item
        print(f'Barang {item.nama_item} berhasil ditambahkan ke dalam keranjang.')           #Menampilkan keterangan bahwa barang/item telah berhasil diinput
        return tambah                                                                        #Digunakan untuk menyimpan hasil input barang dan ditujukan untuk melakukan testing
    
    def tampilkan_item(self):
        '''
        fungsi ini digunakan untuk menampilkan hasil nama dan harga barang/item yang telah diinput       
        '''                                                                
        print("Barang di keranjang:")                                                        #Menampilkan keterangan barang yang ada dikeranjang
        nomer_urut = 0                                                                       #Digunakan untuk menghitung nomor urut barang/item yang telah diinput
        for i in self.list_item:                                                             #Digunakan untuk memanggil semua barang/item yang sudah diinput
            nomer_urut +=1                                                                   #Digunakan untuk menghitung nomor urut barang/item yang diinput
            print(f"{nomer_urut}. {i.nama_item} - Rp{i.harga_item}")                         #Menampilkan list barang/item dan harga yang sudah di input
    
    def hapus_item(self, item):
        '''
        fungsi ini digunakan untuk menghapus barang/item yang sudah disimpan dalam list
        '''
        for j in self.list_item:                                                            #Digunakan untuk memanggil semua barang/item yang sudah diinput
            if j.nama_item == item:                                                         #Untuk menunjukan jika nama barang/item yang diinput sama dengan nama barang yang disimpan pada list
                hapus = self.list_item.remove(j)                                            #Digunakan untuk menghapus nama barang/item yang sudah tersimpan
                print(f'Barang {item} berhasil dihapus dari keranjang.')                    #Menampilkan nama barang/item yang sudah dihapus
                return hapus                                                                #Digunakan untuk menyimpan hasil hapus barang dan ditujukan untuk melakukan testing
            else:
                print(f'Barang {item} tidak tersedia di dalam keranjang')                   #Menampilkan keterangan jika barang yang diinput tidak tersedia pada keranjang
    
    def hitung_total(self):
        '''
        fungsi ini digunakan untuk menghitung total harga yang telah diinput dan disimpan
        '''
        harga_total = 0                                                                     #sebagai wadah untuk penambahan harga
        for k in self.list_item:
            harga_total += k.harga_item                                                     #Untuk penambahan harga
        return harga_total                                                                  #Digunakan untuk menyimpan hasil total harga barang dan ditujukan untuk melakukan testing

def menu_utama():
    '''
    Fungsi ini digunakan sebagai tampilan menu utama
    '''
    print("")
    print("Selamat datang di keranjang belanja toko makmur")
    print("\nmenu")
    print("1. Menambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Barang Di Keranjang")
    print("4. Lihat Total Belanja")
    print("5. Exit")

def main():            
    '''
    Fungsi ini digunakan untuk memproses hasil input dari tampilan menu
    '''
    keranjang = ShoppingCart()                                                          #Pembuatan variabel untuk memanggil class ShoppingCart
    while True:                                                                         #Loop yang digunakan agar menu utama berjalan 
        menu_utama()                                                                    #Menampilkan menu utama
        pilih_menu = input("Pilihan: ")                                                 #variable untuk melakukan input pilihan menu

        if pilih_menu == '1':                                                           #Pengkondisional jika menu yang dipilih nomor 1
            nama_item_input = str(input("Masukan nama barang: "))                       #Digunakan untuk input nama item/barang
            harga_item_input = int(input("Masukan harga barang: "))                     #Digunakan untuk input harga item/barang
            item = CartItem(nama_item_input, harga_item_input)                          #Variabel untuk memasukan nama dan harga item/barang
            keranjang.tambah_item(item)                                                 #Menambahkan nama dan harga item/barang ke dalam class ShoppingCart tambah_item lalu diproses

        elif pilih_menu == '2':                                                         #Pengkondisional jika menu yang dipilih nomor 2
            nama_item_input = input("Masukan nama barang yang ingin dihapus: ")         #Digunakan untuk input nama item/barang. Sesuaikan dengan nama yang sudah diinput
            keranjang.hapus_item(nama_item_input)                                       #Menambahkan nama item/barang ke dalam class ShoppingCart hapus_item lalu diproses

        elif pilih_menu == '3':                                                         #Pengkondisional jika menu yang dipilih nomor 3
            keranjang.tampilkan_item()                                                  #Menampilkan hasil input yang sudah disimpan di class ShoppingCart tampilkan_item
                    
        elif pilih_menu == '4':                                                         #Pengkondisional jika menu yang dipilih nomor 4
            total_belanja = keranjang.hitung_total()                                    #Membuat variabel total_belanja untuk memanggil class ShoppingCart hitung_total
            print(f"Total belanja: {total_belanja}")                                    #Menampilkan total_belanja yaitu penjumlahan total harga

        elif pilih_menu == '5':                                                         #Pengkondisional jika menu yang dipilih nomor 5
            print("Sampai jumpa! Terima kasih sudah belanja di toko makmur")            #Menampilkan keterangan jika program sudah selesai
            break                                                                       #Loop selesai

        else:
            print("Pilihannya salah, silahkan coba lagi!")                              #Pengkondisional jika menu yang dipilih selain nomor 1,2,3,4,5. Makan akan menampilkan keterangan bahwa input salah

if __name__ == "__main__": 
    main()

        