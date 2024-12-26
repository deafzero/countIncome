# author `Lucas renanda`
# desc `Saya seorang siswa jurusan RPL di SMK - AL KHOIRIYAH BARON`

import datetime
import argparse
from babel.numbers import format_currency

# pengashilan per minggu 
income_per_week = 50_000 # Rp 50.000
# menegecek jumlah pengahasilan beberapa minggu kedepan
day_parse = argparse.ArgumentParser("Count income per - week!")
day_parse.add_argument("-w" ,"--week",  help="Income dari beberapa minggu ke depan", type=int, default=4)
user_week = day_parse.parse_args() # parsing flag -w or --week

now = datetime.datetime.now() # dicek mulai tanggal sekarang

# tahap logika 
week = 1 
# perulangan untuk pengashilan tiap minggu
while week <= (user_week.week): 
    # menjumlahkan waktu sekarang dengan tiap minggu berikutnya
    per_week = now + datetime.timedelta(days=7*week)
    # menampilkan tanggal disetiap hari senin di tiap minggu berikutnya
    print(f"\tHari Senin : {(per_week - datetime.timedelta(days=per_week.weekday())).date()}")
    # menampilkan minggu dan pendapatan per minggu
    print(f"\tPendapatan minggu ke {week} sebanyak Rp.{income_per_week*week:,}")
    print("-- -- -- -- -- -- -- -- -- -- -- -- --")
    week+=1