# \# PostgreSQL Veri Üretimi Otomasyonu

# 

# Selenium web otomasyonu kullanarak PostgreSQL veritabanlarına otomatik veri üretimi aracı.

# 

# \## Genel Bakış

# 

# Bu Python scripti, web arayüzü üzerinden PostgreSQL veritabanlarında büyük miktarda test verisi üretme sürecini otomatikleştirir. Veritabanı kayıt sayısını gerçek zamanlı olarak izler ve belirlenen hedefe ulaşana kadar veri üretimini sürdürür.

# 

# \## Özellikler

# 

# \- Selenium kullanarak otomatik web arayüzü kontrolü

# \- Gerçek zamanlı PostgreSQL veritabanı izleme

# \- Hedef odaklı veri üretimi (hedefe ulaşana kadar devam eder)

# \- Otomatik yeniden deneme mekanizması ile hata yönetimi

# \- İlerleme takibi ve detaylı raporlama

# \- Otomatik veritabanı bağlantı yönetimi

# 

# \## Gereksinimler

# 

# \- Python 3.x

# \- Selenium WebDriver

# \- psycopg2 (PostgreSQL adaptörü)

# \- ChromeDriver

# \- Chrome tarayıcısı

# 

# \## Kurulum

# 

# Gerekli Python paketlerini yükleyin:

# 

# ```bash

# pip install selenium psycopg2-binary

# ```

# 

# ChromeDriver kurulumu:

# 1\. https://chromedriver.chromium.org/ adresini ziyaret edin

# 2\. Chrome tarayıcınızın sürümüne uygun versiyonu indirin

# 3\. `chromedriver.exe` dosyasını proje dizinine yerleştirin

# 

# \## Yapılandırma

# 

# \### Veritabanı Ayarları

# 

# `get\_data\_count()` fonksiyonunda veritabanı bağlantı parametrelerini güncelleyin:

# 

# ```python

# conn = psycopg2.connect(

# &nbsp;   host="10.66.113.1",      # Veritabanı sunucu IP'si

# &nbsp;   database="postgres",     # Veritabanı adı

# &nbsp;   user="sa",              # Kullanıcı adı

# &nbsp;   password="password",     # Şifre

# &nbsp;   port="5432"             # Port

# )

# ```

# 

# \### Hedef Ayarları

# 

# Hedef veri sayısını ihtiyacınıza göre değiştirin:

# 

# ```python

# target\_data = 1000000  # Hedef kayıt sayısını belirleyin

# ```

# 

# \### Web Uygulaması URL'si

# 

# Hedef web uygulaması URL'sini güncelleyin:

# 

# ```python

# driver.get("http://10.66.113.1:80")  # Web uygulaması URL'niz

# ```

# 

# \## Kullanım

# 

# Scripti çalıştırın:

# 

# ```bash

# python main.py

# ```

# 

# Script şu adımları gerçekleştirecektir:

# 1\. Chrome tarayıcısını açar ve hedef web uygulamasına gider

# 2\. Dropdown menüden PostgreSQL projesini seçer

# 3\. Data Generation Case kısmına gider

# 4\. Veritabanındaki mevcut kayıt sayısını kontrol eder

# 5\. Hedefe ulaşana kadar tekrar tekrar veri üretir

# 6\. Son istatistikleri görüntüler

# 

# \## Script Akışı

# 

# 1\. \*\*Başlatma\*\*: Tarayıcı kurulumu ve web sayfası navigasyonu

# 2\. \*\*Proje Seçimi\*\*: PostgreSQL seçeneğinin otomatik seçimi

# 3\. \*\*Case Seçimi\*\*: Data Generation Case'e navigasyon

# 4\. \*\*Veri Üretimi Döngüsü\*\*: Hedef sayıya ulaşana kadar tekrar

# 5\. \*\*İlerleme İzleme\*\*: Her işlem sonrası veritabanı kontrolü

# 6\. \*\*Raporlama\*\*: Detaylı sonuç raporu

# 

# \## Örnek Çıktı

# 

# ```

# Başlangıç veri sayısı kontrol ediliyor...

# ecommerce.addresses tablosunda şuan 245,678 kayıt var

# 

# Şuan: 245,678 | Hedefe kalan: 754,322

# Run 1 başlatıldı

# Veri üretimi başlatıldı

# İşlem tamamlandı!

# 25,000 yeni kayıt eklendi (Toplam: 270,678)

# 

# ...

# 

# HEDEF ULAŞILDI! 1,000,156 kayıt var!

# 

# BAŞARILI

# Başlangıç: 245,678

# Son durum: 1,000,156

# Eklenen: 754,478

# Toplam run: 31

# ```

# 

# \## Hata Yönetimi

# 

# Script aşağıdaki durumlar için otomatik hata yönetimi içerir:

# \- Web elementlerinin bulunamadığı durumlar

# \- Geçici ağ bağlantı sorunları

# \- Veritabanı bağlantı hataları

# \- JavaScript execution hataları

# 

# Her hata durumunda script 5 saniye bekler ve işlemi yeniden dener.

# 

# \## Veritabanı İzleme

# 

# Her veri üretimi işlemi sonrasında:

# \- Yeni kayıt sayısı kontrol edilir

# \- Eklenen kayıt miktarı hesaplanır

# \- İlerleme durumu ekrana yazdırılır

# \- Hedefe kalan kayıt sayısı gösterilir

# 

# \## Güvenlik ve Performans

# 

# \- Her veritabanı işlemi sonrası bağlantılar güvenli şekilde kapatılır

# \- Hata durumları izole edilir ve tüm süreci durdurmaz

# \- Script sonunda tüm kaynaklar temizlenir

# \- Bellek sızıntıları önlenir

# 

# \## Sorun Giderme

# 

# \### ChromeDriver Hatası

# ```

# selenium.common.exceptions.WebDriverException: 'chromedriver' executable needs to be in PATH

# ```

# \*\*Çözüm\*\*: ChromeDriver'ı doğru konuma yerleştirin ve PATH'e ekleyin

# 

# \### Veritabanı Bağlantı Hatası

# ```

# psycopg2.OperationalError: could not connect to server

# ```

# \*\*Çözüm\*\*: PostgreSQL server'ın çalıştığından ve bağlantı bilgilerinin doğru olduğundan emin olun

# 

# \### Element Bulunamama Hatası

# ```

# selenium.common.exceptions.NoSuchElementException

# ```

# \*\*Çözüm\*\*: Web sayfası yapısı değişmiş olabilir, XPath selector'larını güncelleyin

# 

# \## Geliştirilmesi Planlanan Özellikler

# 

# \- Modal dialog yönetimi ve otomatik kapatma

# \- Çoklu thread desteği ile paralel işlem

# \- Harici yapılandırma dosyası desteği

# \- İşlem tamamlandığında email bildirimi

# \- REST API entegrasyonu

# \- Docker containerization

# \- Grafik kullanıcı arayüzü

# 

# \## Performans Bilgileri

# 

# Ortalama değerler:

# \- Run başına kayıt sayısı: yaklaşık 25,000

# \- İşlem süresi: 30-60 saniye/run

# \- 1 milyon kayıt için: 40-50 run (30-45 dakika)

# 

# \## Katkıda Bulunma

# 

# 1\. Projeyi fork edin

# 2\. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)

# 3\. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)

# 4\. Branch'i push edin (`git push origin feature/yeni-ozellik`)

# 5\. Pull Request oluşturun

# 

# \## Lisans

# 

# Bu proje MIT lisansı altında lisanslanmıştır.

# 

# \## İletişim

# 

# Sorularınız için issue açabilir veya pull request gönderebilirsiniz.

