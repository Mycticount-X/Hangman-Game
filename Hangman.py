import random
from Kata import Daftar_Kata
from Kata import Daftar_Kata_Tantangan

"""
Made by Mycticount Xeta Ahlovely (Mycticount-X)
Some of this code belongs to Parvat Computer Technology (YouTube)
"""

""" [ENG]
Get Random Words from Daftar_Kata
and Daftar_Kata_Tantangan in File "Kata"
"""

""" [IND]
Mengambil Kata acak dari Daftar_Kata
dan Daftar_Kata_Tantangan di File "Kata"
"""

def Ambil_Kata():
     Kata = random.choice(Daftar_Kata)
     return Kata.upper()

def Ambil_Kata_Tantangan():
     Kata = random.choice(Daftar_Kata_Tantangan)
     return Kata.upper()

""" [ENG]
This is the main game section
Basically, 
- Displays Hangman and omitted words
(Word = APPLE) (Screen = _____)
- Ask the user to enter words or letters
- If correct, the Letter will be revealed.
- If wrong, Hangman's life will be reduced.
- Input will be rejected if:
   - Invalid: Not a letter
   - Words do not match the number of letters
   - The letters have already been guessed
- The game is considered finished when
   - Player guesses the correct word (Win)
   - The Hangman Hanged / Finished Drawn (Lose)
"""

""" [IND]
Ini adalah bagian game utamanya
Pada dasarnya, 
- Menampilkan Hangman dan kata yang dihilangkan
(Word = APPLE) (Screen = _____)
- Meminta pengguna memasukan Kata atau Huruf
- Jika benar, Huruf akan terungkap.
- Jika salah, Nyawa Hangman akan berkurang.
- Input akan ditolak apabila:
   - Invalid: Bukan huruf
   - Kata tidak sesuai jumlah huruf
   - Huruf sudah pernah ditebak
- Permainan Dianggap selesai apabila
   - Pemain menebak kata yang benar (Menang)
   - Hangman Digantung / Selesai DIgambar (Kalah)

"""
def play(Kata):
    Kompilasi_Kata = "_" * len(Kata)
    Tebakan_Benar = False
    Tebak_Huruf = []
    Tebak_Kata = []
    Nyawa = 6

    # print()
    # print("Sistem: Permainan Hangman segera dimulai!")
    # print("Tebaklah sebuah kata atau huruf")
    # print("Hangman akan digantung setelah 6 tebakan salah")
    # mode = input("Lakukan Input apa saja untuk melanjutkan... ")
    
    print()
    print("Sistem: Permainan Hangman dimulai!")
    print(display_hangman(Nyawa))
    print(Kompilasi_Kata)
    print("\n")
    while not Tebakan_Benar and Nyawa > 0:
        print("Tebakan tersisa:", Nyawa)
        coba = input("Silahkan tebak sebuah huruf atau kata: ").upper()
        if len(coba) == 1 and coba.isalpha():
            if coba in Tebak_Huruf:
                print("\nSistem: Huruf", coba, "sudah tertebak")
            elif coba not in Kata:
                print("\nSistem:", coba, "tidak ada dalam kata.")
                Nyawa -= 1
                Tebak_Huruf.append(coba)
            else:
                print("\nSistem: Menebak benar huruf", coba + "!")
                Tebak_Huruf.append(coba)
                Kata_list = list(Kompilasi_Kata)
                indices = [i for i, letter in enumerate(Kata) if letter == coba]
                for index in indices:
                    Kata_list[index] = coba
                Kompilasi_Kata = "".join(Kata_list)
                if "_" not in Kompilasi_Kata:
                    Tebakan_Benar = True

        elif len(coba) == len(Kata) and coba.isalpha():
            if coba in Tebak_Kata:
                print("\nSistem: Menebak benar kata", coba)
            elif coba != Kata:
                print("\nSistem:",coba, "bukan kata yang dimaksud.")
                Nyawa -= 1
                Tebak_Kata.append(coba)
            else:
                Tebakan_Benar = True
                Kompilasi_Kata = Kata

        elif len(coba) != len(Kata) and coba.isalpha():
            print("\nSistem: Mohon perhatikan jumlah huruf yang ada dalam kata")
        else:
            print("\nSistem: Tebakan invalid.")
        print(display_hangman(Nyawa))
        print(Kompilasi_Kata)
        print("\n")
    if Tebakan_Benar:
        print("Selamat! Kamu telah memenangkan permainan")
    else:
        print("Hangman telah digantung. Kata yang dimaksud adalah " + Kata)


""" [ENG]
This is the Hangman Drawing
for every stages / HP
"""

""" [IND]
Ini adalah gambar Hangman
untuk setiap nyawa / HP
"""

def display_hangman(Nyawa):
    stages = [  #(Final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                #(1)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                #(2)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                #(3)
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                #(4)
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                #(5)
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                #(Permulaan Kosong)
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[Nyawa]



def main():
    print()
    print("Sistem: Permainan Hangman segera dimulai!")
    print("        Tebaklah sebuah kata atau huruf")
    print("        Hangman akan digantung setelah 6 tebakan salah")
    print()
    mode = input("Lakukan Input apa saja untuk melanjutkan... ")
    if mode.upper() == "TANTANGAN":
        Kata = Ambil_Kata_Tantangan()
        print()
        print()
        print("<?> "*13)
        print("Sistem: Lapor. Input Rahasia telah dimasukan")
        print("        Sistem Game telah dialihkan ke Mode Tantangan")
        print()
        input("Lakukan Input apa saja untuk melanjutkan... ")
    else:
        Kata = Ambil_Kata()
    play(Kata)

    while input("Mau main lagi? (Y/T) ").upper() == "Y":
        print()
        print("Sistem: Permainan Hangman segera dimulai!")
        print("        Tebaklah sebuah kata atau huruf")
        print("        Hangman akan digantung setelah 6 tebakan salah")
        print()
        mode = input("Lakukan Input apa saja untuk melanjutkan... ")
        if mode.upper() == "TANTANGAN":
            Kata = Ambil_Kata_Tantangan()
            print()
            print()
            print("<?> "*13)
            print("Sistem: Lapor. Input Rahasia telah dimasukan")
            print("        Sistem Game telah dialihkan ke Mode Tantangan")
            input("Lakukan Input apa saja untuk melanjutkan... ")
        else:
            Kata = Ambil_Kata()
        play(Kata)


if __name__ == "__main__":
    main()