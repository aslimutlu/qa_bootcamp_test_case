from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base import Base

class OpenPositionsPageTest():
    
    def run(self, driver):
        
        base_test = Base(driver=driver)
        base_test.start("https://useinsider.com/careers/open-positions/?department=qualityassurance")
        #department dropdown için title'ın quality assurance olduğundan emin olup location dropdownundan istanbul seçtirme işlemi
        while True:
            qa = base_test.driver.find_element(By.XPATH, '//*[@id="select2-filter-by-department-container"]')
            title_attribute = qa.get_attribute("title")

            if title_attribute == "Quality Assurance":
                print("Başlık doğru: Quality Assurance")
                base_test.clickElement('//*[@id="top-filter-form"]/div[1]/span/span[1]/span', 200)
                istanbul = base_test.driver.find_element(By.XPATH, '//li[.="Istanbul, Turkey"]')
                istanbul.click()
                base_test.wait_for_load(5)
                break  # Doğru başlık bulunduğunda döngüyü kır

            else:
                print("Başlık yanlış: ", title_attribute)
                base_test.wait_for_load(20)

                
        #seçilen bir rol üzerindeki view role butonuna tıkla
        base_test.clickElement_js('//*[@id="jobs-list"]/div[2]/div/a')
        
        
        #sayfa, yeni bir sekme olarak açılacak
        # Ana pencereyi sakla
        main_window_handle = base_test.driver.current_window_handle

        # Yeni sekmenin açılmasını bekle
        WebDriverWait(base_test.driver, 30).until(EC.number_of_windows_to_be(2))

        # Tüm pencere kollarını al
        all_window_handles = base_test.driver.window_handles

        # Yeni sekmenin penceresini bul
        new_window_handle = [window for window in all_window_handles if window != main_window_handle][0]

        # Yeni sekmenin penceresine geç
        base_test.driver.switch_to.window(new_window_handle)
        
        # sayfa doğrulama
        base_test.urlControl("https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436")
        base_test.titleControl("Software QA Tester", 10)
