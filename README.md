# PostgreSQL Veri Üretimi Otomasyonu

Selenium web otomasyonu kullanarak PostgreSQL veritabanlarına otomatik veri üretimi aracı.

## Genel Bakış

Bu Python scripti, web arayüzü üzerinden PostgreSQL veritabanlarında büyük miktarda test verisi üretme sürecini otomatikleştirir. Veritabanı kayıt sayısını gerçek zamanlı olarak izler ve belirlenen hedefe ulaşana kadar veri üretimini sürdürür.

## Özellikler

- Selenium kullanarak otomatik web arayüzü kontrolü
- Gerçek zamanlı PostgreSQL veritabanı izleme
- Environment variables (.env) ile güvenli yapılandırma
- Hedef odaklı veri üretimi (hedefe ulaşana kadar devam eder)
- Otomatik yeniden deneme mekanizması ile hata yönetimi
- İlerleme takibi ve detaylı raporlama
- Otomatik veritabanı bağlantı yönetimi

## Gereksinimler

- Python 3.x
- Selenium WebDriver
- psycopg2 (PostgreSQL adaptörü)
- python-dotenv (Environment variables)
- ChromeDriver
- Chrome tarayıcısı

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install selenium psycopg2-binary python-dotenv
```

2. ChromeDriver kurulumu:
   - https://chromedriver.chromium.org/ adresini ziyaret edin
   - Chrome tarayıcınızın sürümüne uygun versiyonu indirin
   - `chromedriver.exe` dosyasını proje dizinine yerleştirin

## Yapılandırma

### 1. .env Dosyası Oluşturun
Proje kök dizininde `.env` dosyası oluşturun ve aşağıdaki yapılandırmayı ekleyin:

```env
# Database Configuration
DB_HOST=172.29.112.1
DB_PORT=5432
DB_DATABASE=postgres
DB_USER=sa
DB_PASSWORD=password
DB_SCHEMA=ecommerce
DB_TABLE=addresses

# Selenium Configuration
SELENIUM_URL=http://172.29.112.1
CHROMEDRIVER_PATH=./chromedriver.exe
IMPLICIT_WAIT=30

# Application Configuration
PROJECT_NAME=postgresqlproje
CASE_NAME=DATA GENERATION CASE
TARGET_DATA_COUNT=1000000

# XPATH Selectors
XPATH_PROJECT_SELECTOR=//div[contains(@class, 'ant-select-selector')]
XPATH_PROJECT_OPTION=//div[contains(text(),'{project_name}')]
XPATH_CASE_BUTTON=//span[text()='{case_name}']
XPATH_RUN_BUTTON_1=//tbody//tr[1]//button[3]
XPATH_RUN_BUTTON_2=//button[contains(., 'RUN')]

# Wait Times (seconds)
SLEEP_INTERVAL=2
ERROR_WAIT_TIME=5
```

## Kullanım

1. Scripti çalıştırın:
```bash
python main.py
```

2. Script şu adımları gerçekleştirecektir:
   - Chrome tarayıcısını açar ve hedef web uygulamasına gider
   - Dropdown menüden PostgreSQL projesini seçer
   - Data Generation Case kısmına gider
   - Veritabanındaki mevcut kayıt sayısını kontrol eder
   - Hedefe ulaşana kadar tekrar tekrar veri üretir
   - Son istatistikleri görüntüler

## Script Akışı

1. **Başlatma**: Tarayıcı kurulumu ve web sayfası navigasyonu
2. **Proje Seçimi**: PostgreSQL projesinin otomatik seçimi
3. **Case Seçimi**: Data Generation Case'e navigasyon
4. **Veri Üretimi Döngüsü**: Hedef sayıya ulaşana kadar tekrar
5. **İlerleme İzleme**: Her işlem sonrası veritabanı kontrolü
6. **Raporlama**: Detaylı sonuç raporu

## Örnek Çıktı

```
Environment variables kontrol ediliyor...
DB_HOST: 172.29.112.1
DB_DATABASE: postgres
SELENIUM_URL: http://172.29.112.1

Proje: postgresqlproje, Case: DATA GENERATION CASE, Hedef: 1,000,000
Başlangıç veri sayısı kontrol ediliyor...
ecommerce.addresses tablosunda şuan 245,678 kayıt var

Şuan: 245,678 | Hedefe kalan: 754,322
Run 1 başlatıldı
Veri üretimi başlatıldı
İşlem tamamlandı!
25,000 yeni kayıt eklendi (Toplam: 270,678)

...

HEDEF ULAŞILDI! 1,000,156 kayıt var!

BAŞARILI
Başlangıç: 245,678
Son durum: 1,000,156
Eklenen: 754,478
Toplam run: 31
```

## Yapılandırma Parametreleri

### Database Configuration
- `DB_HOST`: PostgreSQL sunucu IP'si
- `DB_PORT`: PostgreSQL port (varsayılan: 5432)
- `DB_DATABASE`: Veritabanı adı
- `DB_USER`: PostgreSQL kullanıcı adı
- `DB_PASSWORD`: PostgreSQL şifresi
- `DB_SCHEMA`: Şema adı
- `DB_TABLE`: Tablo adı

### Application Settings
- `TARGET_DATA_COUNT`: Hedef kayıt sayısı
- `PROJECT_NAME`: Web arayüzündeki proje adı
- `CASE_NAME`: Kullanılacak case adı

### Wait Times
- `SLEEP_INTERVAL`: İşlemler arası bekleme süresi (saniye)
- `ERROR_WAIT_TIME`: Hata durumunda bekleme süresi (saniye)

## Hata Yönetimi

Script aşağıdaki durumlar için otomatik hata yönetimi içerir:
- Web elementlerinin bulunamadığı durumlar
- Geçici ağ bağlantı sorunları
- PostgreSQL veritabanı bağlantı hataları
- JavaScript execution hataları

Her hata durumunda script belirlenen süre bekler ve işlemi yeniden dener.

## Veritabanı İzleme

Her veri üretimi işlemi sonrasında:
- Yeni kayıt sayısı kontrol edilir
- Eklenen kayıt miktarı hesaplanır
- İlerleme durumu ekrana yazdırılır
- Hedefe kalan kayıt sayısı gösterilir

## Güvenlik Notları

⚠️ **UYARI**: Bu projede `.env` dosyası ile hassas bilgiler saklanmaktadır:
- Veritabanı şifreleri
- Sunucu IP adresleri
- Kullanıcı bilgileri

**GitHub'a yüklemeden önce**:
1. `.env` dosyasındaki gerçek şifreleri kaldırın
2. Örnek değerler kullanın: `DB_PASSWORD=your_password_here`
3. Gerçek IP adreslerini değiştirin: `DB_HOST=your_db_host`

**Alternatif**: `.env.example` şablonu oluşturun ve gerçek `.env` dosyasını paylaşmayın.

## Performans ve Güvenlik

- Her veritabanı işlemi sonrası bağlantılar güvenli şekilde kapatılır
- Environment variables ile hassas bilgiler korunur
- Hata durumları izole edilir ve tüm süreci durdurmaz
- Script sonunda tüm kaynaklar temizlenir
- Bellek sızıntıları önlenir

## Sorun Giderme

### ChromeDriver Hatası
```
selenium.common.exceptions.WebDriverException: 'chromedriver' executable needs to be in PATH
```
**Çözüm**: ChromeDriver'ı doğru konuma yerleştirin ve `.env` dosyasında path'i güncelleyin

### PostgreSQL Bağlantı Hatası
```
psycopg2.OperationalError: could not connect to server
```
**Çözüm**: PostgreSQL server'ın çalıştığından ve `.env` dosyasındaki bağlantı bilgilerinin doğru olduğundan emin olun

### Environment Variable Hatası
```
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
```
**Çözüm**: `.env` dosyasının doğru konumda olduğundan ve formatının doğru olduğundan emin olun

### Element Bulunamama Hatası
```
selenium.common.exceptions.NoSuchElementException
```
**Çözüm**: Web sayfası yapısı değişmiş olabilir, `.env` dosyasındaki XPath selector'larını güncelleyin

## Performans Bilgileri

Ortalama değerler:
- Run başına kayıt sayısı: yaklaşık 25,000
- İşlem süresi: 30-60 saniye/run
- 1 milyon kayıt için: 40-50 run (30-45 dakika)