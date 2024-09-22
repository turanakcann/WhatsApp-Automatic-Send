from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriver yolunu belirtin
chrome_driver_path = 'C:\Program Files\Google\Chrome\chromedriver-win64\chromedriver.exe'

# ChromeDriver'ı Service ile başlatıyoruz
service = Service(executable_path=chrome_driver_path)

# WebDriver'ı başlatıyoruz
driver = webdriver.Chrome(service=service)

# WhatsApp Web'i aç
driver.get('https://web.whatsapp.com')
input("Lütfen WhatsApp Web'e QR kodu ile giriş yapın ve Enter'a basın...")

# Telefon numaralarını bir dosyadan okuyan fonksiyon
def get_phone_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = [line.strip() for line in file.readlines() if line.strip()]
    return numbers

# Telefon numaralarını dosyadan çek
phone_numbers = get_phone_numbers('number.txt')

# Gönderilecek mesaj
message = "Merhaba, bu bir otomatik WhatsApp mesajıdır!"

# Her numara için mesaj gönderme işlemi
for number in phone_numbers:
    url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
    driver.get(url)
    
    # Sayfanın yüklenmesini bekle
    try:
    # Butonun yüklenmesini beklemek için WebDriverWait kullan
        send_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))
        )
        send_button.click()
        print(f"Mesaj gönderildi: {number}")
    except Exception as e:
        print(f"Mesaj gönderilemedi: {number}. Hata: {e}")
    
    time.sleep(5)  # Mesaj gönderiminden sonra bekleme süresi
    

# Tarayıcıyı kapatıyoruz
driver.quit()
