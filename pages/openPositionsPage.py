from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from fonksiyonlar import fonksiyonlar as fn

class openPositionsPageTest() :
    # sayfa doğrulama
    fn.urlControl("useinsider.com/careers/open-positions/?department=qualityassurance")
    fn.titleControl("Open Positions", 10)
    
    #department dropdown için title'ın quality assurance olduğundan emin olup location dropdownundan istanbul seçtirme işlemi
    while True:
        qa = fn.driver.find_element(By.XPATH, '//*[@id="select2-filter-by-department-container"]')
        title_attribute = qa.get_attribute("title")

        if title_attribute == "Quality Assurance":
            print("Başlık doğru: Quality Assurance")
            fn.clickElement('//*[@id="top-filter-form"]/div[1]/span/span[1]/span/span[2]', 200)
            istanbul = fn.driver.find_element(By.XPATH, '//li[.="Istanbul, Turkey"]')
            istanbul.click()
            break  # Doğru başlık bulunduğunda döngüyü kır

        else:
            print("Başlık yanlış: ", title_attribute)
            sleep(10)
            
    #seçilen bir rol üzerindeki view role butonuna tıkla
    fn.clickElement_js('//*[@id="jobs-list"]/div[2]/div/a')
    
    
    #sayfa, yeni bir sekme olarak açılacak
    # Ana pencereyi sakla
    main_window_handle = fn.driver.current_window_handle

    # Yeni sekmenin açılmasını bekle
    WebDriverWait(fn.driver, 30).until(EC.number_of_windows_to_be(2))

    # Tüm pencere kollarını al
    all_window_handles = fn.driver.window_handles

    # Yeni sekmenin penceresini bul
    new_window_handle = [window for window in all_window_handles if window != fn.main_window_handle][0]

    # Yeni sekmenin penceresine geç
    fn.driver.switch_to.window(new_window_handle)
