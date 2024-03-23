from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fonksiyonlar import fonksiyonlar as fn

class HomePageTest():
    
    def run():
        # sayfa doğrulama
        fn.start("https://useinsider.com/") 
        fn.urlControl("useinsider.com")

        # navbar'dan career sayfasının seçilmesi işlemi
        fn.clickElement('Company',10,By.LINK_TEXT)
        print("Company tıklandı")
        fn.clickElement("//a[.='Careers']",10)
        print("Career tıklandı")


home_page_test= HomePageTest()