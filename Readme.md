# 📄 Random PDF Generator

Program Python untuk menghasilkan dokumen PDF dengan nama acak dan konten teks acak yang dapat dikustomisasi jumlah halamannya.

## ✨ Fitur

- 🎲 **Nama file acak** - Setiap PDF memiliki nama unik 10 karakter alfanumerik
- 📑 **Jumlah halaman fleksibel** - Tentukan sendiri berapa halaman yang diinginkan
- 📝 **Konten teks acak penuh** - Setiap halaman terisi penuh dengan karakter acak (huruf, angka, simbol, spasi)
- 💾 **Simpan otomatis** - File tersimpan di folder yang sama dengan script Python
- 📊 **Informasi detail** - Menampilkan progress pembuatan dan informasi file

## 📋 Persyaratan

- Python 3.6 atau lebih baru
- Library `reportlab`

## 🚀 Instalasi

1. **Clone atau download repository ini**

2. **Install dependency yang diperlukan:**
   ```bash
   pip install reportlab
   ```

## 💻 Cara Penggunaan

1. **Jalankan program:**
   ```bash
   python random_pdf_generator.py
   ```

2. **Masukkan jumlah halaman yang diinginkan:**
   ```
   ==================================================
   GENERATOR PDF DENGAN KONTEN ACAK
   ==================================================

   Masukkan jumlah halaman PDF (minimal 1): 10
   ```

3. **Program akan membuat PDF dan menampilkan informasi:**
   ```
   ==================================================
   Membuat PDF: a7Bx9kL2mP.pdf
   Jumlah halaman: 10
   Menghasilkan teks acak...
   Halaman 1/10 selesai
   Halaman 2/10 selesai
   ...
   ✓ PDF berhasil dibuat: C:\Users\...\a7Bx9kL2mP.pdf
   ✓ Ukuran file: 45.32 KB
   ==================================================
   ```

4. **File PDF akan tersimpan di folder yang sama dengan script Python**

## 📁 Struktur File

```
Random-Scribd-PDF-Maker/
│
├── random_pdf_generator.py    # Script utama
├── README.md                   # Dokumentasi ini
└── *.pdf                       # File PDF yang dihasilkan (nama acak)
```

## ⚙️ Konfigurasi

### Mengubah Pengaturan Teks

Anda dapat memodifikasi beberapa parameter di dalam kode:

```python
# Ukuran font (default: 10)
font_size = 10

# Margin halaman (default: 0.75 inch)
margin = 0.75 * inch

# Jenis font (default: Helvetica)
c.setFont("Helvetica", font_size)
```

### Karakter yang Digunakan

Program menggunakan kombinasi karakter berikut:
- Huruf besar dan kecil (A-Z, a-z)
- Angka (0-9)
- Tanda baca dan simbol
- Spasi

Untuk mengubah karakter yang digunakan, edit fungsi `generate_random_string()`:
```python
characters = string.ascii_letters + string.digits + string.punctuation + ' '
```

## 🛠️ Troubleshooting

### Error: ModuleNotFoundError: No module named 'reportlab'
**Solusi:** Install library reportlab
```bash
pip install reportlab
```

### Error: Permission denied
**Solusi:** Pastikan Anda memiliki izin menulis di folder tempat script berada

### PDF tidak tersimpan di folder yang benar
**Solusi:** Program sudah diperbaiki untuk menggunakan `os.path.dirname(os.path.abspath(__file__))` yang menjamin file tersimpan di folder yang sama dengan script

## 📝 Contoh Output

**Nama file:** `MKzCOp5FLh.pdf`

**Isi halaman:**
```
aB3$xY#9m kL2*pQ@7n vC8!wE4& fR1%tU6^ gH5(jI0) ...
zA9#bX2*cW& eV7!dS4@ fT1%gR8^ hY3(kQ6) lP0$mN5! ...
...
(setiap halaman terisi penuh dengan teks acak seperti ini)
```

## 🤝 Kontribusi

Kontribusi, issues, dan feature requests sangat diterima!

## 📄 Lisensi

Program ini bebas digunakan untuk keperluan pribadi dan edukasi.

## 👨‍💻 Author

Dibuat dengan ❤️ menggunakan Python dan ReportLab

---

**Note:** Program ini dibuat untuk keperluan testing dan edukasi. Gunakan dengan bijak!