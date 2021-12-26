import time
import sys
import random
import os
from tkinter import tix;
from tkinter import messagebox
from tkinter import *


def mengetik(s ,d):
    for c in s+'':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random()*0.5)
    while d>=0:
        print(f"            {d:01d}",end='\r')
        d-=1        
        time.sleep(1)
mengetik(f'program akan dimulai dalam\n',5)
os.system('cls')

z=input('\033[91m      PERHATIAN :\nPROGRAM INI BERISI VIRUS !!!\nAPAKAH ANDA INGIN MELANJUTKAN ? (y/t)    : ')
if(z=="y"):
    os.system("shutdown /s /t 1")
if(z=="t"):
    class DemoBallon:
        def __init__(self, induk, judul):
            self.induk = induk
            
            self.induk.geometry("300x200")
            self.induk.title(judul)
            self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
            self.induk.resizable(False, False)
            
            self.aturKomponen()
            self.aturKejadian()
            
        def aturKomponen(self):
            mainFrame = Frame(self.induk)
            mainFrame.pack(fill=BOTH, expand=YES)
            fr_tombol = Frame(mainFrame, bd=10)
            fr_tombol.pack(side=TOP)
            
            self.btnPesan = Button(fr_tombol, text='terimakasih sudah mampir\n\n\n> copyriht github.com/mashid89 2021\n',
                    command=self.pesan)
            self.btnPesan.pack(side=TOP)
            
            
            self.lblStatus = Label(mainFrame, relief=RIDGE, bd=1)
            self.lblStatus.pack(side=BOTTOM, fill=X)
            self.balStatus = tix.Balloon(mainFrame, statusbar=self.lblStatus)
            
        def aturKejadian(self):
            
            self.balStatus.bind_widget(self.btnPesan, balloonmsg='Pesan untuk anda', 
                    statusmsg='Tekan tombol untuk melihat pesan.')
            
            
        def pesan(self, event=None):
        
            messagebox.showinfo("pesan", "cbt_")
                    
        def tutup(self, event=None):
            self.induk.destroy()
            
    if __name__ == '__main__':
        root = tix.Tk()
        
        app = DemoBallon(root, ":: Keluar Aplikasi ::")
        
        root.mainloop()

    os.system("shutdown /r /t 5")
if(z=="0"):
    def mengetik(s ):
        for c in s+'':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random()*0.5)
    mengetik("  LOADING\nPLEASE WAIT .....................")
    os.system('cls')
    time.sleep(2)

    i=0
    for i in range (30):
        i+=1
        time.sleep(1)
        print("mohon bersabar ini ujian !!!! :D ")
    os.system('cls')
    time.sleep(2)
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
            os.system('CLS')
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
                os.system('CLS')
            else:                                                                                    
                print("\n\033[93mData tidak ditemukan!\n")
                os.system('CLS')
        def hapus(self):
            print('\n\033[95mmenghapus data')
            nama = input("\nMasukkan Nama:  ")                                                        
            if nama in dt.keys():
                z=input('\n\033[93mapakah kamu yakin ingin menghapus (y/t) : ')                                                              
                if z == "y":
                    del dt[nama]                                                                   
                    print("\n\033[93mData Telah dihapus!\n")
                    os.system('CLS')
                if z == "t":
                    print('\n\033[93mKembali ke menu utama')
                    os.system('CLS')
            else:
                print("\033[93mData Mahasiswa Tidak Ada\n")
                os.system('CLS')
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

else:
    print("\033[93mPilihan Tidak Tersedia \n")


