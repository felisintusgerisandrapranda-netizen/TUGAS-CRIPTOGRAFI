# 3 Aplikasi Cipher Klasik

Aplikasi dibuat dengan Python + Tkinter sehingga tidak membutuhkan library tambahan.

## 1. Caesar Cipher
File: `caesar_cipher.py`

Cara menjalankan:
python caesar_cipher.py

Contoh:
Plaintext = HALO DUNIA
Kunci = 3
Hasil = KDOR GXQLD

Rumus:
Enkripsi: C = (P + k) mod 26
Dekripsi: P = (C - k) mod 26

## 2. Vigenere Cipher
File: `vigenere_cipher.py`

Cara menjalankan:
python vigenere_cipher.py

Contoh:
Plaintext = KRIPTOGRAFI
Kunci = LAMPION

Kunci diulang sepanjang plaintext. Rumus:
Enkripsi: C = (P + K) mod 26
Dekripsi: P = (C - K) mod 26

## 3. Columnar Transposition Cipher
File: `columnar_transposition.py`

Cara menjalankan:
python columnar_transposition.py

Contoh kunci:
TOMBAK

Plaintext disusun ke dalam baris dan cipherteks dibaca berdasarkan urutan alfabet huruf pada kunci.

## Persyaratan
- Python 3.x
- Tkinter (biasanya sudah tersedia pada instalasi Python Windows)

Tidak membutuhkan:
- pip install
- Flask
- database
- internet

Semua aplikasi memiliki tombol ENKRIPSI, DEKRIPSI, dan BERSIHKAN.
