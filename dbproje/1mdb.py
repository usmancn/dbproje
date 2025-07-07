import os
import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Debug: Environment variables kontrol
print("Environment variables kontrol ediliyor...")
print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_DATABASE: {os.getenv('DB_DATABASE')}")
print(f"SELENIUM_URL: {os.getenv('SELENIUM_URL')}")


def get_data_count():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )

        cursor = conn.cursor()

        # Schema ve tablo adını env dosyasından al
        schema = os.getenv('DB_SCHEMA')
        table = os.getenv('DB_TABLE')
        query = f"SELECT COUNT(*) FROM {schema}.{table}"

        cursor.execute(query)
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return count

    except Exception as e:
        print(f"DB hatası: {e}")
        return 0


# Selenium kurulumu
service = Service(os.getenv('CHROMEDRIVER_PATH', './chromedriver.exe'))
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# IMPLICIT_WAIT için varsayılan değer
implicit_wait = int(os.getenv('IMPLICIT_WAIT', '30'))
driver.implicitly_wait(implicit_wait)

try:
    # Ana sayfaya git
    selenium_url = os.getenv('SELENIUM_URL')
    if not selenium_url:
        raise ValueError("SELENIUM_URL environment variable bulunamadı!")

    driver.get(selenium_url)

    # Environment variables'ları al
    project_name = os.getenv('PROJECT_NAME')
    case_name = os.getenv('CASE_NAME')
    target_data = int(os.getenv('TARGET_DATA_COUNT', '1000000'))

    if not project_name or not case_name:
        raise ValueError("PROJECT_NAME veya CASE_NAME environment variable bulunamadı!")

    print(f"Proje: {project_name}, Case: {case_name}, Hedef: {target_data:,}")

    # Select kısmından projeyi seç
    project_selector = os.getenv('XPATH_PROJECT_SELECTOR')
    driver.find_element(By.XPATH, project_selector).click()

    # Proje seçimi
    project_xpath = os.getenv('XPATH_PROJECT_OPTION').format(project_name=project_name)
    driver.find_element(By.XPATH, project_xpath).click()

    # Case seçimi
    case_xpath = os.getenv('XPATH_CASE_BUTTON').format(case_name=case_name)
    driver.find_element(By.XPATH, case_xpath).click()

    # Buton xpath'leri ve bekleme süreleri
    run_button_1_xpath = os.getenv('XPATH_RUN_BUTTON_1')
    run_button_2_xpath = os.getenv('XPATH_RUN_BUTTON_2')
    sleep_interval = int(os.getenv('SLEEP_INTERVAL', '2'))
    error_wait_time = int(os.getenv('ERROR_WAIT_TIME', '5'))

    current_run = 0

    print("Başlangıç veri sayısı kontrol ediliyor...")
    initial_count = get_data_count()
    schema = os.getenv('DB_SCHEMA')
    table = os.getenv('DB_TABLE')
    print(f"{schema}.{table} tablosunda şuan {initial_count:,} kayıt var")

    while True:
        # Her döngüde DB'yi kontrol et
        current_count = get_data_count()

        # Hedef sayıya ulaştık mı?
        if current_count >= target_data:
            print(f"HEDEF ULAŞILDI! {current_count:,} kayıt var!")
            break

        remaining = target_data - current_count
        print(f"Şuan: {current_count:,} | Hedefe kalan: {remaining:,}")

        try:
            # İlk run butonuna bas
            driver.find_element(By.XPATH, run_button_1_xpath).click()
            current_run += 1
            print(f"Run {current_run} başlatıldı")

            # İkinci RUN butonuna bas
            driver.find_element(By.XPATH, run_button_2_xpath).click()
            print(f"Veri üretimi başlatıldı")

            # İşlem bitene kadar bekle
            while True:
                time.sleep(sleep_interval)
                run_button = driver.find_element(By.XPATH, run_button_1_xpath)
                if run_button.is_enabled():
                    print("İşlem tamamlandı!")
                    break

            # İşlem bittikten sonra DB'yi kontrol et
            new_count = get_data_count()
            added = new_count - current_count
            print(f"{added:,} yeni kayıt eklendi (Toplam: {new_count:,})")

        except Exception as e:
            print(f"Hata: {e}")
            print(f"{error_wait_time} saniye bekleyip devam")
            time.sleep(error_wait_time)
            continue

    # Final rapor
    final_count = get_data_count()
    total_added = final_count - initial_count
    print(f"\nBAŞARILI")
    print(f"Başlangıç: {initial_count:,}")
    print(f"Son durum: {final_count:,}")
    print(f"Eklenen: {total_added:,}")
    print(f"Toplam run: {current_run}")

except Exception as e:
    print(f"Genel hata: {e}")

finally:
    input("Enter'a basınca kapanacak")
    driver.quit()