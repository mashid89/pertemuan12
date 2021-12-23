print('\033[93m==========================================')
print('|   program menambah data dengan class   |')
print('==========================================')
dt={}
class daftarNilai():    
    def tambah(self):
        print('\n\033[95mTambah Data Mahasiswa')
        nama= input("Masukkan Nama\t\t: ")                                        
        nim= input("Masukkan NIM\t\t: ")                                         
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                              
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))                                   
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))                                    
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dt[nama]=nim,nilaiTugas,nilaiUts,nilaiUas,nilaiAkhir,
        print("\n\033[93mData Berhasil Di ditambah!\n")
    def ubah(self):
        print('\n\033[95mMengubah Data Mahasiswa')
        nama = input("Masukkan Nama: ")                                                         
        if nama in dt.keys():                              
            nim= input("Masukkan NIM Baru\t: ")                              
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                           
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))                           
            nilaiUas= int(input("Masukkan Nilai UAS\t: "))                           
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)          
            dt[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                      
            print("\n\033[93mData Berhasil Di Update!\n")
        else:                                                                                    
            print("\n\033[93mData tidak ditemukan!\n")
    def hapus(self):
        print('\n\033[95mmenghapus data')
        nama = input("\nMasukkan Nama:  ")                                                        
        if nama in dt.keys():
            z=input('\n\033[93mapakah kamu yakin ingin menghapus (y/t) : ')                                                              
            if z == "y":
                del dt[nama]                                                                   
                print("\n\033[93mData Telah dihapus!\n")
            if z == "t":
                print('\n\033[93mKembali ke menu utama')
        else:
            print("\033[93mData Mahasiswa Tidak Ada\n")
    def lihat(self):
        if dt.items():                                                                     
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in dt.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================\n")
        else:
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                        TIDAK ADA DATA!                         |")
            print("==================================================================\n")
    def keluar(self):
        print('\n\033[97m=====terimakasih=====\n')
        print(21*'=')
        print("Nama\t: Nur hidayat\nKelas\t: TI.21.C5\nNIM\t: 312110584")
        print(21*'=')  
        print('\n>\033[03m copyright github.com/mashid89 2021\n')                                                                   
while True:
    data=daftarNilai()
    print('\n\033[96mtambah\t(1)\nubah\t(2)\nlihat\t(3)\nhapus\t(4)')                                                                                     
    c = input("\nsilahkan masukan pilihan : ")
    print()
    if (c=="1"):
        data.tambah()
    elif (c=="2"):
        data.ubah()
    elif (c=="3"):
        data.lihat()
    elif (c=="4"):
        data.hapus()
    else:
        data.keluar()
        break

