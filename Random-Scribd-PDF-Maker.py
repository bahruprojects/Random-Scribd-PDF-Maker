import random
import string
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import os
from datetime import datetime

def get_script_directory():
    """Mendapatkan path direktori dimana script Python berada"""
    return os.path.dirname(os.path.abspath(__file__))

def generate_random_string(length=100):
    """Menghasilkan string acak dengan panjang tertentu"""
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_filename():
    """Menghasilkan nama file acak"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    random_suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"document_{timestamp}_{random_suffix}.pdf"

def get_output_path():
    """Mendapatkan path lengkap untuk menyimpan file PDF"""
    script_dir = get_script_directory()
    filename = generate_random_filename()
    return os.path.join(script_dir, filename)

def calculate_max_lines_per_page():
    """Menghitung berapa banyak baris yang muat dalam satu halaman"""
    width, height = A4
    margin = 20 * mm
    line_height = 12
    content_height = height - 2 * margin - 30  # Tinggi konten yang tersedia
    return int(content_height / line_height)

def create_full_page_random_pdf(num_pages=5):
    """Membuat PDF dimana setiap halaman PENUH dengan teks acak"""
    
    # Dapatkan path output di folder yang sama dengan script
    output_path = get_output_path()
    
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    # Settings
    margin = 20 * mm
    text_width = width - 2 * margin
    font_name = "Helvetica"
    font_size = 10
    line_height = 12
    
    # Hitung maksimal baris per halaman
    max_lines = calculate_max_lines_per_page()
    
    print(f"📄 Setiap halaman akan berisi maksimal {max_lines} baris teks")
    print(f"💾 File akan disimpan di: {output_path}")
    
    for page_num in range(1, num_pages + 1):
        if page_num > 1:
            c.showPage()
        
        # Header
        c.setFont(font_name, 12)
        c.drawString(margin, height - margin, f"Halaman {page_num}")
        c.drawString(width - 60, height - margin, f"{max_lines} baris")
        
        # Setup untuk konten
        c.setFont(font_name, font_size)
        y_position = height - margin - 30
        
        # Generate teks acak sampai halaman penuh
        lines_written = 0
        
        while lines_written < max_lines:
            # Generate teks acak yang cukup panjang
            chars_needed = random.randint(50, 100)  # Karakter per baris
            random_text = generate_random_string(chars_needed)
            
            # Split teks menjadi baris
            lines = simpleSplit(random_text, font_name, font_size, text_width)
            
            # Tulis setiap baris sampai halaman penuh
            for line in lines:
                if lines_written >= max_lines:
                    break
                    
                c.drawString(margin, y_position, line)
                y_position -= line_height
                lines_written += 1
        
        print(f"✅ Halaman {page_num}: {lines_written} baris teks acak")
    
    c.save()
    return output_path

def create_continuous_random_pdf(num_pages=5):
    """Membuat PDF dengan teks acak kontinu tanpa memperhatikan halaman"""
    
    # Dapatkan path output di folder yang sama dengan script
    output_path = get_output_path()
    
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    margin = 20 * mm
    text_width = width - 2 * margin
    font_name = "Helvetica"
    font_size = 10
    line_height = 12
    
    # Generate teks acak yang SANGAT PANJANG
    total_chars_needed = num_pages * 2000  # Estimasi kasar
    continuous_text = generate_random_string(total_chars_needed)
    
    # Split seluruh teks menjadi baris
    all_lines = simpleSplit(continuous_text, font_name, font_size, text_width)
    
    current_page = 1
    y_position = height - margin
    lines_per_page = 0
    
    for i, line in enumerate(all_lines):
        # Cek jika perlu halaman baru
        if y_position < margin + 30:
            c.showPage()
            current_page += 1
            y_position = height - margin
            lines_per_page = 0
        
        # Header untuk halaman baru
        if lines_per_page == 0:
            c.setFont(font_name, 12)
            c.drawString(margin, y_position, f"Halaman {current_page}")
            y_position -= 25
            c.setFont(font_name, font_size)
        
        # Tulis baris
        c.drawString(margin, y_position, line)
        y_position -= line_height
        lines_per_page += 1
        
        # Berhenti jika sudah mencapai jumlah halaman yang diminta
        if current_page > num_pages:
            break
    
    c.save()
    return output_path

def show_current_directory():
    """Menampilkan informasi direktori saat ini"""
    script_dir = get_script_directory()
    print(f"📁 Direktori program: {script_dir}")
    
    # Cek apakah direktori writable
    if os.access(script_dir, os.W_OK):
        print("✅ Direktori dapat ditulis (writable)")
    else:
        print("❌ Direktori tidak dapat ditulis (permission denied)")
    
    return script_dir

def main():
    """Program utama"""
    print("=== Generator PDF dengan Halaman Penuh Teks Acak ===")
    print()
    
    # Tampilkan informasi direktori
    current_dir = show_current_directory()
    
    try:
        num_pages = int(input("\nMasukkan jumlah halaman (default 3): ") or "3")
        
        if num_pages <= 0:
            print("Error: Jumlah halaman harus lebih dari 0!")
            return
        
        print("\nPilih tipe PDF:")
        print("1. Setiap halaman penuh dengan teks acak (recommended)")
        print("2. Teks acak kontinu yang mengalir antar halaman")
        
        choice = input("Pilihan (1/2, default 1): ") or "1"
        
        if choice == "1":
            print("\n🔄 Membuat PDF dengan halaman penuh teks acak...")
            file_path = create_full_page_random_pdf(num_pages)
        else:
            print("\n🔄 Membuat PDF dengan teks acak kontinu...")
            file_path = create_continuous_random_pdf(num_pages)
        
        # Informasi file
        file_size = os.path.getsize(file_path)
        filename = os.path.basename(file_path)
        
        print(f"\n🎉 Dokumen PDF berhasil dibuat!")
        print(f"📄 Nama file: {filename}")
        print(f"📁 Disimpan di: {current_dir}")
        print(f"📊 Ukuran file: {file_size:,} bytes")
        print(f"📄 Jumlah halaman: {num_pages}")
        
        # Tampilkan file yang berhasil dibuat
        print(f"\n📋 File PDF dalam direktori:")
        pdf_files = [f for f in os.listdir(current_dir) if f.endswith('.pdf')]
        for pdf_file in pdf_files:
            file_path = os.path.join(current_dir, pdf_file)
            file_size = os.path.getsize(file_path)
            print(f"   - {pdf_file} ({file_size:,} bytes)")
        
    except ValueError:
        print("Error: Masukkan angka yang valid!")
    except Exception as e:
        print(f"Error: {e}")

# Versi simple untuk penggunaan cepat
def create_simple_random_pdf(num_pages=3, filename=None):
    """Versi simple untuk membuat PDF dengan cepat"""
    if filename is None:
        output_path = get_output_path()
    else:
        script_dir = get_script_directory()
        output_path = os.path.join(script_dir, filename)
    
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    margin = 20 * mm
    text_width = width - 2 * margin
    font_name = "Helvetica"
    font_size = 10
    line_height = 12
    
    max_lines = calculate_max_lines_per_page()
    
    for page_num in range(1, num_pages + 1):
        if page_num > 1:
            c.showPage()
        
        c.setFont(font_name, 12)
        c.drawString(margin, height - margin, f"Halaman {page_num}")
        
        c.setFont(font_name, font_size)
        y_position = height - margin - 30
        
        lines_written = 0
        while lines_written < max_lines:
            random_text = generate_random_string(random.randint(50, 100))
            lines = simpleSplit(random_text, font_name, font_size, text_width)
            
            for line in lines:
                if lines_written >= max_lines:
                    break
                c.drawString(margin, y_position, line)
                y_position -= line_height
                lines_written += 1
    
    c.save()
    print(f"✅ PDF berhasil dibuat: {output_path}")
    return output_path

if __name__ == "__main__":
    main()
    
    # Opsi untuk membuat PDF tambahan
    print("\n" + "="*50)
    additional = input("Apakah Anda ingin membuat PDF tambahan? (y/n): ").lower()
    
    if additional == 'y':
        try:
            num_pages = int(input("Jumlah halaman untuk PDF tambahan: ") or "2")
            file_path = create_simple_random_pdf(num_pages)
            print(f"✅ PDF tambahan berhasil dibuat!")
        except Exception as e:
            print(f"Error: {e}")