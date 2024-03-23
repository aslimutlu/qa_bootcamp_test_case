from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from fonksiyonlar import fonksiyonlar as fn

class careerPageTest():

    # sayfa doğrulama
    fn.urlControl("https://useinsider.com/careers/")
    fn.titleControl("Career", 10)

    # Career sayfasında Our Locations/Teams / Life at Insider alanlarının Kontolü
    # Locations text kontrol
    fn.textReading("Locations", "//h3[@class='category-title-media ml-0']")
    # Life at Insider text kontrol
    fn.textReading("Life at Insider", "//h2[.='Life at Insider']")
    # Teams text kontrol
    fn.textReading("Find your calling", "//h3[contains(.,'Find your calling')]")
    #Teams altındaki butona tıklama (See All Teams)
    fn.clickElement_js('//*[@id="career-find-our-calling"]/div/div/a', By.XPATH)    
    
    #butona tıklandığdan emin olmak için açılan kartların kontrolü
    job_items = []
    elements = fn.driver.find_elements(By.XPATH, "//div[@class='col-12 d-flex flex-wrap p-0 career-load-more']/div" )
    for element in elements:
        job_items.append(element.text)
    if len(job_items) == 15:
        print("işler listelendi.")
    else:
        print("Alan bulunamadı.")
        
    #quality assurance tıklanması
    fn.clickElement_js('//*[@id="career-find-our-calling"]/div/div/div[2]/div[12]/div[2]/a')