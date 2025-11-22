#Random-Scribd-PDF-Maker Version 2
import random
import string
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os

def generate_random_string(length):
    """Menghasilkan string acak dengan panjang tertentu"""
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_filename():
    """Menghasilkan nama file acak"""
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"{random_name}.pdf"

def create_pdf_with_random_text(num_pages=5):
    """
    Membuat PDF dengan teks acak
    
    Parameters:
    num_pages (int): Jumlah halaman yang diinginkan (default: 5)
    """
    # Menghasilkan nama file acak
    filename = generate_random_filename()
    
    # Mendapatkan direktori tempat script Python berada
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    
    # Membuat canvas PDF
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    
    # Pengaturan margin dan font
    margin = 0.75 * inch
    font_size = 10
    c.setFont("Helvetica", font_size)
    
    # Menghitung jumlah karakter per baris dan jumlah baris per halaman
    chars_per_line = int((width - 2 * margin) / (font_size * 0.6))
    line_height = font_size * 1.2
    lines_per_page = int((height - 2 * margin) / line_height)
    
    print(f"Membuat PDF: {filename}")
    print(f"Jumlah halaman: {num_pages}")
    print(f"Menghasilkan teks acak...")
    
    # Membuat setiap halaman
    for page in range(num_pages):
        y_position = height - margin
        
        # Mengisi halaman dengan teks acak
        for line in range(lines_per_page):
            if y_position < margin:
                break
            
            # Generate teks acak untuk satu baris
            random_text = generate_random_string(chars_per_line)
            c.drawString(margin, y_position, random_text)
            y_position -= line_height
        
        # Pindah ke halaman berikutnya jika bukan halaman terakhir
        if page < num_pages - 1:
            c.showPage()
            c.setFont("Helvetica", font_size)
        
        print(f"Halaman {page + 1}/{num_pages} selesai")
    
    # Simpan PDF
    c.save()
    print(f"\n✓ PDF berhasil dibuat: {filepath}")
    print(f"✓ Ukuran file: {os.path.getsize(filepath) / 1024:.2f} KB")
    
    return filepath

if __name__ == "__main__":
    print("=" * 50)
    print("GENERATOR PDF DENGAN KONTEN ACAK")
    print("=" * 50)
    
    try:
        # Meminta input jumlah halaman dari user
        while True:
            try:
                jumlah_halaman = int(input("\nMasukkan jumlah halaman PDF (minimal 1): "))
                if jumlah_halaman < 1:
                    print("❌ Jumlah halaman harus minimal 1!")
                    continue
                break
            except ValueError:
                print("❌ Masukkan angka yang valid!")
        
        print(f"\n{'=' * 50}")
        create_pdf_with_random_text(num_pages=jumlah_halaman)
        print(f"{'=' * 50}\n")
        
    except KeyboardInterrupt:
        print("\n\n❌ Program dibatalkan oleh user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPastikan library reportlab sudah terinstall!")
        print("Install dengan: pip install reportlab")