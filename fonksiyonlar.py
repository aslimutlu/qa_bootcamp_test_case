from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()

class fonksiyonlar():
    
    def start(url):
        go_to_url = driver.get(url)
        driver.maximize_window()


    def urlControl(url):
        global current_url
        current_url = driver.current_url
        print(current_url)
        if url in current_url:
            print("Url Eşleşti")
        else:
            print("Url Eşleşmedi")
        

    def titleControl(contains, interval):
        global page_title
        page_title = driver.title
        title_control = WebDriverWait(driver, interval).until(EC.title_contains(contains))
        if contains in page_title:
            print("Title girilen parametreyi İÇERİYOR!")
        else: 
            print("Title girilen parametreyi İÇERMİYOR!")

    def clickElement(path,interval,method=By.XPATH):
        global current_url
        element = WebDriverWait(driver,interval).until(EC.element_to_be_clickable((method,path)))
        element.click()
        current_url = driver.current_url

    def textReading(text, path, method=By.XPATH):
        find_text = driver.find_element(method, path)
        text_control = find_text.text
        if text in text_control:
            print("İstenen Metin: "+text, "Mevcut Metin: "+text_control, "\n", "İstenen text mevcut!" )
        else:
            print("İstenen Metin: "+text, "Mevcut Metin: "+text_control, "\n", "İstenen text bulunamadı!")

    def clickElement_js(path, method=By.XPATH):
        click_element = driver.find_element(method, path)
        driver.execute_script("arguments[0].click();", click_element)       