# 📄 Random PDF Generator - Full Page Text

Program Python untuk menghasilkan dokumen PDF dengan nama acak dan halaman yang terisi penuh dengan teks acak. Program ini menyimpan file PDF di folder yang sama dengan script Python.

## ✨ Fitur Utama

- 🎲 **Nama file unik** - Menggunakan timestamp dan suffix acak (format: `document_YYYYMMDD_HHMMSS_xxxxxx.pdf`)
- 📑 **Dua mode pembuatan PDF**:
  - Mode 1: Setiap halaman penuh dengan teks acak (recommended)
  - Mode 2: Teks acak kontinu yang mengalir antar halaman
- 📝 **Halaman terisi penuh** - Setiap halaman berisi maksimal baris teks sesuai kapasitas halaman
- 💾 **Simpan otomatis** - File tersimpan di folder yang sama dengan script Python
- 📊 **Informasi detail** - Menampilkan progress, ukuran file, dan daftar PDF yang ada
- 🔄 **Buat PDF tambahan** - Opsi untuk membuat beberapa PDF dalam satu sesi

## 📋 Persyaratan

- Python 3.6 atau lebih baru
- Library `reportlab`

## 🚀 Instalasi

1. **Clone atau download repository ini**

2. **Install library yang diperlukan:**
   ```bash
   pip install reportlab
   ```

## 💻 Cara Penggunaan

### Mode Interaktif (Recommended)

1. **Jalankan program:**
   ```bash
   python random_pdf_generator.py
   ```

2. **Ikuti instruksi yang muncul:**
   ```
   === Generator PDF dengan Halaman Penuh Teks Acak ===

   📁 Direktori program: C:\Users\alfin\Downloads\Random-Scribd-PDF-Maker
   ✅ Direktori dapat ditulis (writable)

   Masukkan jumlah halaman (default 3): 5

   Pilih tipe PDF:
   1. Setiap halaman penuh dengan teks acak (recommended)
   2. Teks acak kontinu yang mengalir antar halaman
   Pilihan (1/2, default 1): 1
   ```

3. **Program akan membuat PDF dan menampilkan informasi:**
   ```
   📄 Setiap halaman akan berisi maksimal 50 baris teks
   💾 File akan disimpan di: C:\...\document_20241122_153045_abcdef.pdf
   ✅ Halaman 1: 50 baris teks acak
   ✅ Halaman 2: 50 baris teks acak
   ...

   🎉 Dokumen PDF berhasil dibuat!
   📄 Nama file: document_20241122_153045_abcdef.pdf
   📁 Disimpan di: C:\Users\alfin\Downloads\Random-Scribd-PDF-Maker
   📊 Ukuran file: 45,632 bytes
   📄 Jumlah halaman: 5
   ```

4. **Opsi membuat PDF tambahan:**
   ```
   ==================================================
   Apakah Anda ingin membuat PDF tambahan? (y/n): y
   Jumlah halaman untuk PDF tambahan: 3
   ✅ PDF tambahan berhasil dibuat!
   ```

### Mode Programmatic (Untuk Developer)

Anda juga bisa menggunakan fungsi-fungsi dalam program ini sebagai module:

```python
from random_pdf_generator import create_simple_random_pdf

# Buat PDF dengan 5 halaman
create_simple_random_pdf(num_pages=5)

# Buat PDF dengan nama file custom
create_simple_random_pdf(num_pages=3, filename="custom_name.pdf")
```

## 📁 Struktur File

```
Random-Scribd-PDF-Maker/
│
├── random_pdf_generator.py           # Script utama
├── README.md                          # Dokumentasi ini
└── document_*.pdf                     # File PDF yang dihasilkan
    ├── document_20241122_153045_abcdef.pdf
    ├── document_20241122_154230_xyzabc.pdf
    └── ...
```

## ⚙️ Fungsi-Fungsi Utama

### 1. `create_full_page_random_pdf(num_pages)`
Membuat PDF dimana setiap halaman terisi penuh dengan teks acak (recommended).

**Parameter:**
- `num_pages` (int): Jumlah halaman yang diinginkan

**Return:**
- `str`: Path lengkap file PDF yang dibuat

### 2. `create_continuous_random_pdf(num_pages)`
Membuat PDF dengan teks acak kontinu yang mengalir antar halaman.

**Parameter:**
- `num_pages` (int): Jumlah halaman yang diinginkan

**Return:**
- `str`: Path lengkap file PDF yang dibuat

### 3. `create_simple_random_pdf(num_pages, filename)`
Versi simple untuk membuat PDF dengan cepat (tanpa interaksi).

**Parameter:**
- `num_pages` (int): Jumlah halaman (default: 3)
- `filename` (str, optional): Nama file custom (default: auto-generated)

**Return:**
- `str`: Path lengkap file PDF yang dibuat

### 4. Fungsi Helper

- `get_script_directory()`: Mendapatkan path direktori script
- `generate_random_filename()`: Menghasilkan nama file unik
- `calculate_max_lines_per_page()`: Menghitung kapasitas baris per halaman
- `show_current_directory()`: Menampilkan info direktori dan permission

## 🎨 Konfigurasi

Anda dapat mengubah pengaturan di dalam kode:

### Margin dan Spacing
```python
margin = 20 * mm           # Margin halaman (default: 20mm)
line_height = 12           # Tinggi baris (default: 12 points)
```

### Font
```python
font_name = "Helvetica"    # Jenis font
font_size = 10             # Ukuran font (default: 10)
```

### Karakter Teks Acak
```python
# Dalam fungsi generate_random_string()
characters = string.ascii_letters + string.digits + string.punctuation + " "
```

Karakter yang digunakan:
- Huruf (A-Z, a-z)
- Angka (0-9)
- Simbol & tanda baca
- Spasi

### Panjang Teks per Baris
```python
chars_needed = random.randint(50, 100)  # Karakter per baris (50-100)
```

## 📊 Format Output

### Nama File
Format: `document_YYYYMMDD_HHMMSS_xxxxxx.pdf`

Contoh: `document_20241122_153045_abcdef.pdf`

- `YYYYMMDD`: Tanggal (Year, Month, Day)
- `HHMMSS`: Waktu (Hour, Minute, Second)
- `xxxxxx`: 6 karakter random lowercase

### Struktur Halaman PDF

```
┌──────────────────────────────────────┐
│ Halaman 1              50 baris      │  ← Header
├──────────────────────────────────────┤
│ aB3$xY#9m kL2*pQ@7n vC8!wE4& ...    │
│ zA9#bX2*cW& eV7!dS4@ fT1%gR8^ ...   │
│ ...                                   │  ← Konten acak
│ ... (48 baris lagi)                  │
│ pX5!mN3@ qW7&rT1$ sY9*uV2# ...      │
└──────────────────────────────────────┘
```

## 🛠️ Troubleshooting

### Error: ModuleNotFoundError: No module named 'reportlab'
**Solusi:**
```bash
pip install reportlab
```

### Error: Permission denied
**Penyebab:** Tidak ada izin menulis di folder

**Solusi:**
1. Jalankan Command Prompt/Terminal sebagai Administrator
2. Atau pindahkan script ke folder dengan izin write (seperti Documents atau Downloads)

### Error: Direktori tidak dapat ditulis
**Solusi:** Program akan menampilkan status direktori. Pastikan direktori memiliki permission untuk menulis file.

### PDF tidak tersimpan di folder yang benar
**Solusi:** Program menggunakan `os.path.dirname(os.path.abspath(__file__))` yang menjamin file selalu tersimpan di folder yang sama dengan script Python, tidak peduli dari mana script dijalankan.

### Input tidak valid
**Solusi:** Pastikan memasukkan angka untuk jumlah halaman, dan pilihan 1 atau 2 untuk tipe PDF.

## 📝 Contoh Output

### Contoh Run Program

```
=== Generator PDF dengan Halaman Penuh Teks Acak ===

📁 Direktori program: C:\Users\alfin\Downloads\Random-Scribd-PDF-Maker
✅ Direktori dapat ditulis (writable)

Masukkan jumlah halaman (default 3): 10

Pilih tipe PDF:
1. Setiap halaman penuh dengan teks acak (recommended)
2. Teks acak kontinu yang mengalir antar halaman
Pilihan (1/2, default 1): 1

🔄 Membuat PDF dengan halaman penuh teks acak...
📄 Setiap halaman akan berisi maksimal 50 baris teks
💾 File akan disimpan di: C:\...\document_20241122_153045_abcdef.pdf
✅ Halaman 1: 50 baris teks acak
✅ Halaman 2: 50 baris teks acak
✅ Halaman 3: 50 baris teks acak
✅ Halaman 4: 50 baris teks acak
✅ Halaman 5: 50 baris teks acak
✅ Halaman 6: 50 baris teks acak
✅ Halaman 7: 50 baris teks acak
✅ Halaman 8: 50 baris teks acak
✅ Halaman 9: 50 baris teks acak
✅ Halaman 10: 50 baris teks acak

🎉 Dokumen PDF berhasil dibuat!
📄 Nama file: document_20241122_153045_abcdef.pdf
📁 Disimpan di: C:\Users\alfin\Downloads\Random-Scribd-PDF-Maker
📊 Ukuran file: 91,264 bytes
📄 Jumlah halaman: 10

📋 File PDF dalam direktori:
   - document_20241122_153045_abcdef.pdf (91,264 bytes)
   - document_20241122_154230_xyzabc.pdf (54,752 bytes)

==================================================
Apakah Anda ingin membuat PDF tambahan? (y/n): n
```

## 🔍 Perbedaan Dua Mode

### Mode 1: Setiap halaman penuh (Recommended)
- ✅ Setiap halaman dijamin terisi penuh sampai batas bawah
- ✅ Jumlah baris per halaman konsisten
- ✅ Lebih terstruktur dan rapi
- ✅ Cocok untuk testing kapasitas halaman

### Mode 2: Teks kontinu
- ✅ Teks mengalir natural dari halaman ke halaman
- ✅ Seperti membaca dokumen biasa
- ✅ Cocok untuk simulasi dokumen text panjang

## 💡 Tips Penggunaan

1. **Untuk testing dokumen besar:** Gunakan Mode 1 dengan jumlah halaman banyak (>10)
2. **Untuk dokumen natural:** Gunakan Mode 2
3. **Untuk buat banyak PDF sekaligus:** Gunakan opsi "PDF tambahan" di akhir program
4. **Untuk automasi:** Import sebagai module dan gunakan fungsi `create_simple_random_pdf()`

## 🤝 Kontribusi

Jika Anda ingin berkontribusi:
1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📄 Lisensi

Program ini bebas digunakan untuk keperluan pribadi, edukasi, dan testing.

## 👨‍💻 Author

Program ini dibuat untuk keperluan testing dan pengembangan.

---

## ⚠️ Catatan Penting

- Program ini dibuat untuk keperluan **testing dan edukasi**
- Teks yang dihasilkan adalah **100% acak** dan tidak memiliki makna
- Ukuran file akan bertambah sesuai jumlah halaman (~9KB per halaman)
- Pastikan memiliki ruang disk yang cukup untuk file PDF yang akan dibuat

## 📞 Support

Jika mengalami masalah atau memiliki pertanyaan, silakan:
- Buat Issue di repository
- Cek bagian Troubleshooting di atas
- Review kode dan komentar dalam program

---

**Happy PDF Generating! 📄✨**