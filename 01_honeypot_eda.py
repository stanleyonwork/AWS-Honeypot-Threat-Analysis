import pandas as pd

file_path = 'data/AWS_Honeypot_marx-geo.csv'

print("Memindaian data log...")

# 1. Load dataset
df = pd.read_csv(file_path)

# 2. Intip 5 baris pertama untuk melihat bentuk asli datanya
print("\n=== 5 Baris Pertama ===")
print(df.head())

# 3. Cek struktur data (nama kolom, jumlah baris, dan tipe data)
print("\n=== Informasi Dataset ===")
print(df.info())

# 4. Cek apakah ada data yang bolong/kosong (Missing Values)
print("\n=== Jumlah Data Kosong per Kolom ===")
print(df.isnull().sum())