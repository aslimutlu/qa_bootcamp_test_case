import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():
    
    def __init__(self, driver, explicit_wait=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def driver(self):
        return self.driver
    
    
    def start(self, url):
        go_to_url = self.driver.get(url)
        self.driver.maximize_window()


    def urlControl(self, url):
        time.sleep(3)
        global current_url #silebilirsin
        current_url = self.driver.current_url
        print(current_url)
        if url in current_url:
            print("Url Eşleşti")
        else:
            print("Url Eşleşmedi")
            raise "url eşleşmedi"

    def titleControl(self, contains, interval=10):
        global page_title
        page_title = self.driver.title #stitle_contains kullanıldığında gereksiz kalıyor. satır 39a bak.
        title_control = WebDriverWait(self.driver, interval).until(EC.title_contains(contains))
        if contains in page_title:  #burada bu kontrolü yapmama gerek yoktu. title_control bool değer döndürüyor. Onu kullanabilirdin.
            print("Title girilen parametreyi İÇERİYOR!")
        else: 
            print("Title girilen parametreyi İÇERMİYOR!")
            raise "title eşleşmedi"


    def clickElement(self, path,interval=10,method=By.XPATH):
        try:
            global current_url
            element = WebDriverWait(self.driver,interval).until(EC.element_to_be_clickable((method,path)))
            element.click()
            current_url = self.driver.current_url
        except Exception as err:
            print(err)
            print( path + ":" + method + "-> tıklanamadi")
            self.take_screenshot(file_path="./tests/pages/data/" + path +".png")
            
            raise err
        print( path + ":" + method + "-> tıklandi")

    def textReading(self, text, path, method=By.XPATH):
        find_text = self.driver.find_element(method, path)
        text_control = find_text.text
        if text in text_control:
            print("İstenen Metin: "+text, "Mevcut Metin: "+text_control, "\n", "İstenen text mevcut!" )
        else:
            print("İstenen Metin: "+text, "Mevcut Metin: "+text_control, "\n", "İstenen text bulunamadı!")
            self.take_screenshot(file_path="./tests/pages/data/" + path +".png")
            raise "text eşleşmedi"

    def clickElement_js(self, path, method=By.XPATH):
        try:
            click_element = self.driver.find_element(method, path)
            self.driver.execute_script("arguments[0].click();", click_element)       
        except Exception as err:
            print(path + ":" + method + "-> tiklanamadi ")
            self.take_screenshot(file_path="./tests/pages/data/" + path +".png")
            raise err
        print( path + ":" + method + "-> tıklandi")
    
    def wait_for_load(self, timeout=10):
        time.sleep(timeout)

    def take_screenshot(self, file_path):
        total_height = self.driver.execute_script("return document.body.parentNode.scrollHeight")
        
        # Tarayıcı penceresinin yüksekliğini, sayfanın tamamını kapsayacak şekilde ayarla
        self.driver.set_window_size(1920, total_height)  # Genişliği sabit tutarken yüksekliği ayarlayın
        
        # Yeni boyutlara göre biraz bekleyin ve ekran görüntüsü alın
        time.sleep(2)  # Sayfanın yeniden boyutlandırılmasını beklemek için
        self.driver.save_screenshot(file_path)
