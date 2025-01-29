import wikipedia

# Mengatur bahasa Wikipedia ke bahasa Indonesia
wikipedia.set_lang('id')

# Pertanyaan dan jawaban manual dan sebagai tes
manual_qa = {
    "siapa kamu": "Saya adalah Lyra.ai, sebuah asisten virtual yang dapat membantu Anda mencari informasi.",
    "siapa pencipta kamu": "Saya diciptakan oleh Zaki Mushthafa Billah, seorang mahasiswa Universitas Putra Indonesia Padang (UPI YPTK Padang), Fakultas Ilmu Komputer, Jurusan Teknik Informatika."
}

# Fungsi untuk mencari informasi di Wikipedia dan menampilkan sumbernya
def tanya_wikipedia(pertanyaan):
    try:
        # Memeriksa apakah pertanyaan ada di dalam daftar manual
        if pertanyaan.lower() in manual_qa:
            return f"Pertanyaan: {pertanyaan}\n\nJawaban: {manual_qa[pertanyaan.lower()]}\n"
        
        # Menyaring hasil pencarian yang relevan
        results = wikipedia.search(pertanyaan)
        
        if not results:
            return "Maaf, saya tidak menemukan informasi yang relevan."
        
        # Mengambil judul halaman pertama
        page_title = results[0]
        
        # Mengambil ringkasan dari halaman tersebut
        hasil = wikipedia.summary(page_title, sentences=2)  # Mengambil 2 kalimat pertama
        
        # Menambahkan URL halaman sebagai sumber
        sumber = wikipedia.page(page_title).url
        
        # Memformat output dengan jarak antar jawaban
        response = f"""
Pertanyaan: {pertanyaan}

Jawaban: 
{hasil}

Sumber: {sumber}

"""
        return response
    
    except wikipedia.exceptions.DisambiguationError as e:
        # Menangani jika ada banyak hasil yang terkait dengan pertanyaan
        return f"Pertanyaan Anda dapat mengarah ke beberapa topik. Pilih salah satu: {e.options}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Terjadi kesalahan koneksi, coba lagi nanti."
    except wikipedia.exceptions.RedirectError:
        return "Halaman yang Anda cari mengarah ke halaman lain."
    except wikipedia.exceptions.PageError:
        return "Halaman yang Anda cari tidak ditemukan."
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

# Fungsi untuk input pertanyaan dan memperkenalkan diri
if __name__ == "__main__":
    print("Halo! Nama saya Lyra. Saya akan membantu Anda mencari informasi di Wikipedia.")
    while True:
        # Menyediakan input dari pengguna
        pertanyaan = input("Tanyakan sesuatu kepada Lyra: ")
        if pertanyaan.lower() == 'exit':
            print("Terima kasih telah menggunakan Lyra! Sampai jumpa.")
            break
        jawab = tanya_wikipedia(pertanyaan)
        print(jawab)
