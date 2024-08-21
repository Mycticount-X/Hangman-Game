# Hangman Game

This is a simple console-based Hangman game implemented in Python. The game allows the player to guess letters or words to find a hidden word. The player has 6 attempts to guess the word correctly before the "hangman" is fully drawn, indicating a loss.

## Features

- **Random Word Selection**: Words are randomly selected from two lists: `Daftar_Kata` for regular gameplay and `Daftar_Kata_Tantangan` for challenge mode.
- **Two Modes**: The game supports a normal mode and a hidden "challenge mode" which is triggered by entering the secret input "TANTANGAN".
- **Interactive Gameplay**: Players can guess either a single letter or the entire word. The game provides feedback for correct or incorrect guesses.
- **ASCII Art Hangman**: Visual feedback is provided in the form of a "hangman" being drawn with each incorrect guess.

## How to Play

1. Run the script to start the game.
2. Choose a mode by either entering any input for the normal game or typing "TANTANGAN" for the challenge mode.
3. Start guessing letters or the entire word.
4. You win if you guess all the letters of the word correctly or the full word before running out of lives.
5. The game ends in a loss if you run out of lives, and the hangman is fully drawn.

## Prerequisites

- Python 3.x
- Ensure that the `Kata.py` file containing the word lists `Daftar_Kata` and `Daftar_Kata_Tantangan` is present in the same directory as this script.

## Example Output

```plaintext
Sistem: Permainan Hangman dimulai!
  --------
  |      |
  |      
  |    
  |      
  |     
  -
______

Tebakan tersisa: 6
Silahkan tebak sebuah huruf atau kata: 
```

## Author

This Hangman game was created by **Mycticount Xeta Ahlovely (Mycticount-X)**. Some parts of the code were inspired by content from Kite on YouTube.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

# Permainan Hangman

Ini adalah permainan Hangman berbasis konsol sederhana yang diimplementasikan dalam Python. Permainan ini memungkinkan pemain untuk menebak huruf atau kata untuk menemukan kata tersembunyi. Pemain memiliki 6 kesempatan untuk menebak kata dengan benar sebelum "hangman" digambar sepenuhnya, yang menunjukkan kekalahan.

## Fitur

- **Pemilihan Kata Acak**: Kata-kata dipilih secara acak dari dua daftar: `Daftar_Kata` untuk permainan biasa dan `Daftar_Kata_Tantangan` untuk mode tantangan.
- **Dua Mode**: Permainan mendukung mode normal dan mode "tantangan" tersembunyi yang dipicu dengan memasukkan input rahasia "TANTANGAN".
- **Permainan Interaktif**: Pemain dapat menebak huruf tunggal atau kata keseluruhan. Permainan memberikan umpan balik untuk tebakan yang benar atau salah.
- **Hangman ASCII Art**: Umpan balik visual diberikan dalam bentuk "hangman" yang digambar dengan setiap tebakan yang salah.

## Cara Bermain

1. Jalankan skrip untuk memulai permainan.
2. Pilih mode dengan memasukkan input apa saja untuk permainan normal atau ketik "TANTANGAN" untuk mode tantangan.
3. Mulai menebak huruf atau kata keseluruhan.
4. Anda menang jika menebak semua huruf dari kata dengan benar atau kata penuh sebelum nyawa habis.
5. Permainan berakhir dengan kekalahan jika nyawa habis, dan hangman digantung sepenuhnya.

## Prasyarat

- Python 3.x
- Pastikan file `Kata.py` yang berisi daftar kata `Daftar_Kata` dan `Daftar_Kata_Tantangan` ada di direktori yang sama dengan skrip ini.

## Contoh Output

```plaintext
Sistem: Permainan Hangman dimulai!
  --------
  |      |
  |      
  |    
  |      
  |     
  -
______

Tebakan tersisa: 6
Silahkan tebak sebuah huruf atau kata: 
```

## Penulis

Permainan Hangman ini dibuat oleh **Mycticount Xeta Ahlovely (Mycticount-X)**. Beberapa bagian kode terinspirasi dari konten di Kite di YouTube.

## Lisensi

Proyek ini bersifat open-source dan tersedia di bawah [Lisensi MIT](LICENSE).
