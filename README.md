@'
# Pertemuan 06 - Nested Loop, Pola, Akumulasi, dan Pencacahan

**Nama:** Meyliana Solihah  
**NIM:** 2225250080  
**Kelas:** 3B  

## Tujuan

Pada pertemuan ini saya belajar tentang nested loop, pola, akumulasi, dan pencacahan menggunakan Python. Saya juga belajar membuat program yang menggunakan perulangan di dalam perulangan.

## Struktur Folder

```text
pertemuan-06-nested-loop-2225250080/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
└── tugas/
    └── tabel_perkalian_dan_statistik.py
    Cara Menjalankan

Program dijalankan melalui Terminal VS Code dengan perintah:

python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py
Latihan 1 - Pasangan Indeks

Program menggunakan nested loop untuk menampilkan pasangan (i, j) dari i = 1 sampai 3 dan j = 1 sampai 4.

Jumlah pasangan yang dihasilkan adalah 12 pasangan.

Latihan 2 - Pola Segitiga

Program menerima input n dan menampilkan pola segitiga menggunakan tanda *.

Contoh jika n = 3:

*
**
***
Latihan 3 - Jumlah Per Baris

Program menghitung hasil i × j dan menjumlahkannya pada setiap baris.

Hasil jumlah setiap baris adalah:

Baris 1 = 6
Baris 2 = 12
Baris 3 = 18
Baris 4 = 24
Latihan 4 - Menghitung Pasangan

Program menghitung banyak pasangan (i, j) yang memenuhi kondisi i + j <= n.

Hasil pengujian:

n = 2 → 1 pasangan
n = 3 → 3 pasangan
n = 5 → 10 pasangan
Tugas - Tabel Perkalian dan Statistik

Program membuat tabel perkalian menggunakan nested loop.

Program juga menghitung jumlah setiap baris, total semua hasil perkalian, dan banyaknya hasil perkalian yang genap.

Hasil Pengujian
n = 1 → total 1, hasil genap 0
n = 2 → total 9, hasil genap 3
n = 3 → total 36, hasil genap 5

Semua hasil pengujian sesuai dengan hasil yang diharapkan.

Analisis Efisiensi

Pada tugas utama terdapat dua perulangan. Perulangan pertama digunakan untuk baris dan perulangan kedua digunakan untuk kolom.

Jumlah prosesnya adalah n × n = n², sehingga kompleksitas waktunya adalah O(n²).

Refleksi

Setelah mengerjakan pertemuan ini, saya lebih memahami cara menggunakan nested loop dalam Python. Saya juga memahami penggunaan akumulasi untuk menghitung jumlah dan pencacahan untuk menghitung banyaknya hasil yang memenuhi kondisi tertentu.
'@ | Set-Content README.md