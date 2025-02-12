import pandas as pd
from pymongo import MongoClient

# Koneksi ke MongoDB (pastikan MongoDB berjalan)
client = MongoClient("mongodb://localhost:27017/")
db = client["semester4"]  # Ganti dengan nama database
collection = db["tugas1"]  # Ganti dengan nama koleksi

# File CSV yang akan diimpor (pastikan file ada di direktori yang benar)
csv_file = "D:\Matana\Semester 4\Basis Data Lanjut\Google-Playstore.csv"

# Tentukan ukuran batch untuk insert
chunk_size = 500000  # Bisa disesuaikan (misalnya 10.000 atau 50.000)

# Baca CSV secara bertahap
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    # Konversi DataFrame ke dictionary
    data_dict = chunk.to_dict(orient="records")

    # Masukkan data ke MongoDB
    collection.insert_many(data_dict)
    print(f"{len(data_dict)} baris berhasil diimpor...")

print("Semua data berhasil diimport ke MongoDB!")
