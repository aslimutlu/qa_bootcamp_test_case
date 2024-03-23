from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from fonksiyonlar import fonksiyonlar as fn

class formPageTest():
    # sayfa doğrulama
    fn.start("https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436/apply") 
    fn.urlControl("Software QA Tester")
    
    #form kontrolü
    form_control = WebDriverWait(fn.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'application-form'))
    )
    print("Form açıldı")

    fn.driver.quit()