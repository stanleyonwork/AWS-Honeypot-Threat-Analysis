import pandas as pd

file_path = 'data/AWS_Honeypot_marx-geo.csv'
output_path = 'data/cleaned_honeypot_obt.csv'

print("Memulai proses Data Cleaning (OBT Pipeline)...")

# 1. Load dataset mentah
df = pd.read_csv(file_path)
print(f"Data awal: {df.shape[0]} baris, {df.shape[1]} kolom.")

# 2. Drop kolom sampah (Unnamed: 15)
if 'Unnamed: 15' in df.columns:
    df = df.drop(columns=['Unnamed: 15'])
    print("- Kolom 'Unnamed: 15' dihapus.")

# 3. Handle Missing Values di Port -> Isi dengan 0 (Indikasi protokol tanpa port seperti ICMP)
df['spt'] = df['spt'].fillna(0).astype(int)
df['dpt'] = df['dpt'].fillna(0).astype(int)
print("- Missing values pada 'spt' dan 'dpt' diisi dengan 0.")

# 4. Drop baris yang tidak punya info Negara
df = df.dropna(subset=['country'])
print("- Serangan tanpa jejak lokasi/negara dibersihkan.")

# 5. Standarisasi Format Waktu
df['datetime'] = pd.to_datetime(df['datetime'], format='%m/%d/%y %H:%M', errors='coerce')
print("- Kolom waktu dikonversi ke format Datetime standar.")

# 6. Rename kolom agar siap presentasi di BI Tools
df = df.rename(columns={
    'datetime': 'Attack_Time',
    'host': 'Target_Server',
    'src': 'Source_IP_Integer',
    'proto': 'Protocol',
    'spt': 'Source_Port',
    'dpt': 'Destination_Port',
    'srcstr': 'Attacker_IP',
    'cc': 'Country_Code',
    'country': 'Country_Name',
    'locale': 'Locale',
    'localeabbr': 'Locale_Abbr',
    'postalcode': 'Postal_Code',
    'latitude': 'Latitude',
    'longitude': 'Longitude'
})

# 7. Ekspor ke One Big Table (OBT)
df.to_csv(output_path, index=False)
print(f"\n[SUKSES] Data bersih disimpan sebagai: '{output_path}'")
print(f"Data akhir siap pakai: {df.shape[0]} baris, {df.shape[1]} kolom.")