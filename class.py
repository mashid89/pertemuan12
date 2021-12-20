print('====program menambah data dengan class=====')
dt={}
class daftarNilai():
    
    def tambah(self):
        print('\nTambah Data Mahasiswa')
        nama= input("Masukkan Nama\t\t: ")                                        
        nim= input("Masukkan NIM\t\t: ")                                         
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                              
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))                                   
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))                                    
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dt[nama]=nim,nilaiTugas,nilaiUts,nilaiUas,nilaiAkhir,
        
        
        

    def ubah(self):
        print('\nMengubah Data Mahasiswa')
        nama = input("Masukkan Nama: ")                                                         
        if nama in dt.keys():                              
            nim= input("Masukkan NIM Baru\t: ")                              
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                           
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))                           
            nilaiUas= int(input("Masukkan Nilai UAS\t: "))                           
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)          
            dt[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                      
            print("\nData Berhasil Di Update!\n")
        else:                                                                                    
            print("Data tidak ditemukan!\n")

    def hapus(self):
        print('\nmenghapus data')
        nama = input("Masukkan Nama:  ")                                                        
        if nama in dt.keys():                                                              
            del dt[nama]                                                                   
            print("Data Telah dihapus!\n")
        else:
            print("Data Mahasiswa Tidak Ada\n")

    def lihat(self):
        if dt.items():                                                                     
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in dt.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================\n")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================\n")

    def keluar(self):
        print('\n=====terimakasih=====\n')
        print(21*'=')
        print("Nama\t: Nur hidayat\nKelas\t: TI.21.C5\nNIM\t: 312110584")
        print(21*'=')             
                
                                                        
while True:
    data=daftarNilai()
    print('\ntambah\t(1)\nubah\t(2)\nlihat\t(3)\nhapus\t(4)')                                                                                     
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

