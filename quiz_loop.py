import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- 1. SETTING & BUKA BROWSER ---
print("Membuka Chrome...")
options = uc.ChromeOptions()
driver = uc.Chrome(options=options, version_main=142)
driver.maximize_window()

driver.get("https://app.badilag.net/etr")

# --- 2. LOGIN MANUAL ---
print("\n" + "="*50)
print(">>> INSTRUKSI <<<")
print("1. Login Manual.")
print("2. Klik menu 'Daftar Penilaian'.")
print("3. Pastikan TABEL sudah muncul.")
print("="*50)

input("\nTEKAN [ENTER] DI SINI JIKA SUDAH SIAP...")

# --- 3. LOOPING PROSES ---
print("\n🔥 MEMULAI LOOPING (FIX NOTIFLIX)... 🔥")
jumlah_sukses = 0

while True:
    try:
        time.sleep(3) 
        
        if len(driver.find_elements(By.XPATH, "//table/tbody/tr")) == 0:
             print("⚠️ Menunggu tabel loading...")
             time.sleep(2)
             continue

        # --- A. CARI TARGET ---
        xpath_target = "//tr[contains(., 'Belum')]//td[last()]//*[self::a or self::button]"
        targets = driver.find_elements(By.XPATH, xpath_target)

        if len(targets) == 0:
            print(f"\n✅ Selesai! Tidak ditemukan lagi status 'Belum'.")
            break 
        
        print(f"\n[Sisa Antrian: {len(targets)}] Memproses pegawai...")
        
        tombol_aksi = targets[0]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tombol_aksi)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", tombol_aksi)
        
        # --- B. ISI FORM ---
        wait = WebDriverWait(driver, 15)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='radio']")))
        except:
            print("   ⚠️ Form gagal loading. Back...")
            driver.back()
            continue

        time.sleep(2) 
        
        all_radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
        seen_names = []
        for radio in all_radios:
            name = radio.get_attribute("name")
            if name not in seen_names:
                seen_names.append(name)
        
        print(f"   -> Terdeteksi {len(seen_names)} soal.")
        
        for index_soal, nama_soal in enumerate(seen_names):
            opsi_soal_ini = driver.find_elements(By.NAME, nama_soal)
            if not opsi_soal_ini: continue

            # Soal No 2 (index 1) -> Pilih Terakhir (D)
            if index_soal == 1: 
                pilihan = opsi_soal_ini[-1] 
            else:
                pilihan = opsi_soal_ini[0]
            
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", pilihan)
            driver.execute_script("arguments[0].click();", pilihan)
            
        print("   -> Semua soal terjawab.")

        # --- C. KLIK SIMPAN ---
        tombol_simpan = driver.find_element(By.XPATH, "//button[contains(., 'Simpan')]")
        driver.execute_script("arguments[0].scrollIntoView();", tombol_simpan)
        time.sleep(1) 
        driver.execute_script("arguments[0].click();", tombol_simpan)
        print("   -> Tombol Simpan diklik.")
        
        # --- D. KLIK KONFIRMASI 'YA' (FIX NOTIFLIX) ---
        print("   -> Menunggu popup konfirmasi...")
        try:
            # Tunggu modal muncul
            # Kita cari elemen tombol yang punya class 'notiflix-confirm-btn-ok'
            # Atau cari link/tombol apapun yang ada teks "Ya" di dalam modal
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "notiflix-confirm-content")))
            time.sleep(1) # Jeda visual biar popup stabil

            # Strategi 1: Cari Class Standar Notiflix (biasanya tag <a>)
            xpath_ya = "//a[contains(@class, 'notiflix-confirm-btn-ok')]"
            
            # Strategi 2: Kalau class beda, cari teks 'Ya' di dalam elemen notiflix
            if len(driver.find_elements(By.XPATH, xpath_ya)) == 0:
                 xpath_ya = "//*[contains(@class, 'notiflix-confirm')]//*[contains(text(), 'Ya')]"

            tombol_ya = driver.find_element(By.XPATH, xpath_ya)
            driver.execute_script("arguments[0].click();", tombol_ya)
            print("   -> ✅ Tombol 'Ya' DIKLIK!")
            
        except Exception as e:
            print(f"   ⚠️ Warning: Gagal klik Yes: {e}")

        # --- E. TUNGGU RELOAD ---
        print("   -> Menunggu tabel refresh...")
        time.sleep(4)
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        except:
             pass 

        jumlah_sukses += 1

    except Exception as e:
        print(f"❌ Eror: {e}")
        try:
            driver.back()
        except:
            pass
        time.sleep(3)

print("\n🎉 SELESAI! 🎉")