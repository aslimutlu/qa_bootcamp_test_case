from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base

class CareerPageTest():
    
    def run(self,driver):
        base_test = Base(driver=driver)
        
        base_test.start("https://useinsider.com/careers/")
        
        # sayfa doğrulama
        base_test.urlControl("https://useinsider.com/careers/")
        base_test.titleControl("Career", 10)

        # Career sayfasında Our Locations/Teams / Life at Insider alanlarının Kontolü
        # Locations text kontrol
        base_test.textReading("Locations", "//h3[@class='category-title-media ml-0']")
        # Life at Insider text kontrol
        base_test.textReading("Life at Insider", "//h2[.='Life at Insider']")
        # Teams text kontrol
        base_test.textReading("Find your calling", "//h3[contains(.,'Find your calling')]")
        #Teams altındaki butona tıklama (See All Teams)
        base_test.clickElement_js('//*[@id="career-find-our-calling"]/div/div/a', By.XPATH)    
        
        #butona tıklandığdan emin olmak için açılan kartların kontrolü
        job_items = []

        base_test.wait_for_load(3)
        elements = base_test.driver.find_elements(By.XPATH, "//div[@class='col-12 d-flex flex-wrap p-0 career-load-more']/div" )
        for element in elements:
            job_items.append(element.text)
        if len(job_items) == 15:
            print("işler listelendi.")
        else:
            print("Alan bulunamadı.")
        
        #quality assurance tıklanması
        base_test.clickElement_js('//*[@id="career-find-our-calling"]/div/div/div[2]/div[12]/div[2]/a')
        
        #sayfa kontrolleri
        base_test.urlControl("useinsider.com/careers/quality-assurance/")
        base_test.titleControl("quality assurance", 10)