## Menghitung pendapatan ditiap minggu 💰

#### who me 🧐 :
Name : Lucas renanda\
School : SMK AL - KHOIRIYAH BARON\
Major : Rekayasa perangkat lunak

---
#### 🔧 tool : 
- 👨‍💻 Python 3.10++
#### 💡 introduction 
projek ini saya buat atas dasar karena ingin mengetahui pendapatan ditiap minggunya.     
#### 📄 usage : 
##### contoh 1 : 
`python income_per_week.py`\
maka akan mengitung pendapatan di 4 minggu kedepan dimulai dari minggu kedua, Angka 4 adalah default ketika tidak menggunakan flag ketika menjalankan file.
##### contoh 2 : 
`python income_per_week.py -w 10`\
maka akan mengitung pendapatan di 10 minggu kedepan dimulai dari minggu kedua.
#### 📚 how to work
- pertama mendefinisikan pendapatan yang konsisten ditiap minggu nya `income_per_week = 50_000`.
- selanjutnya saya mengambil flag `-w` / `--week` untuk mengambil banyak minggu yang akan dikalkulasi.
- `now = datetime.datetime.now()` pada kode ini saya gunakan untuk mendapatkan tanggal dihari ini yang kemudian akan dilakukan penjumlahan pada flag `-w` / `--week`.
- didalam blok `while` diisi dengan kalkulasi pendapatan ditiap minggunya lalu ditampilkan.


> **thanks for read**

