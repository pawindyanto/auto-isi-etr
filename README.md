# Auto ETR Badilag Filler 🚀

Bot otomatisasi berbasis Python untuk mengisi survei/penilaian pada aplikasi **Electronic Track Record (ETR) Badilag**. 

Script ini dirancang untuk mempermudah pengisian penilaian pegawai dalam jumlah banyak secara otomatis, akurat, dan aman dari deteksi bot standar.

## ✨ Fitur Utama

* **Anti-Bot Detection**: Menggunakan `undetected-chromedriver` untuk melewati proteksi Cloudflare dan deteksi browser standar.
* **Smart Looping**: Otomatis mencari pegawai dengan status "Belum" dan memprosesnya satu per satu hingga habis.
* **Adaptive Answering**: 
    * Mendeteksi jumlah opsi jawaban (A/B/C/D) secara dinamis (aman untuk soal dengan 2 atau 4 opsi).
    * **Logika Jawaban**: Soal No. 1 = A, Soal No. 2 = D, Sisanya = A.
* **Auto-Scroll & Precision Click**: Menggunakan mekanisme scroll otomatis sebelum klik untuk memastikan akurasi dan menghindari *miss-click*.
* **Auto-Confirm**: Otomatis menangani popup konfirmasi "Simpan" (Notiflix Modal).
* **Manual Login Trigger**: Memberikan waktu bagi pengguna untuk Login & Navigasi manual sebelum robot bekerja (aman dari kesalahan login).

## 🛠️ Persyaratan Sistem

1.  **Google Chrome** (Versi Terbaru).
2.  **Python 3.x** terinstall di komputer.
3.  Koneksi Internet stabil.

## 📦 Instalasi

1.  **Clone Repository ini**
    ```bash
    git clone [https://github.com/username-kamu/auto-etr-badilag.git](https://github.com/username-kamu/auto-etr-badilag.git)
    cd auto-etr-badilag
    ```

2.  **Install Library yang Dibutuhkan**
    Buka terminal/CMD dan jalankan:
    ```bash
    pip install selenium undetected-chromedriver
    ```

## 🚀 Cara Penggunaan

1.  **Jalankan Script**
    ```bash
    python quiz_loop.py
    ```

2.  **Proses Login Manual**
    * Jendela Chrome akan terbuka otomatis.
    * Silakan Login menggunakan NIP dan Password Anda.
    * Masuk ke menu **"Daftar Penilaian"** di sidebar kiri.
    * Pastikan tabel daftar pegawai sudah muncul.

3.  **Aktifkan Robot**
    * Kembali ke layar Terminal/CMD (Layar Hitam).
    * Tekan tombol **[ENTER]**.
    * Lepaskan mouse dan keyboard, biarkan robot bekerja mengisi form hingga selesai.

## 📂 Membuat File .EXE (Portable)

Jika ingin menjalankan script ini di komputer lain tanpa menginstall Python:

1.  Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```

2.  Build menjadi EXE:
    ```bash
    python -m PyInstaller --onefile --name "Auto_Isi_ETR" quiz_loop.py
    ```
    *File `.exe` akan muncul di folder `dist`.*

## ⚠️ Disclaimer

Aplikasi ini dibuat untuk tujuan edukasi dan efisiensi kerja. Gunakan dengan bijak. Penulis tidak bertanggung jawab atas penggunaan yang menyalahi aturan aplikasi target.

---
*Created with ❤️ by [Nama Kamu]*
