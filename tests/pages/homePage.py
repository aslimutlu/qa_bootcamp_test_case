from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base


class HomePageTest():
        
    def run(self,driver):

        base_test = Base(driver=driver)
        
        # sayfa doğrulama
        base_test.start("https://useinsider.com/") 
        base_test.urlControl("useinsider.com")

        # navbar'dan career sayfasının seçilmesi işlemi
        base_test.clickElement('Company',10,By.LINK_TEXT)
        base_test.clickElement("//a[.='Careers']",10)
        
        #sayfa kontrolleri
        base_test.urlControl("https://useinsider.com/careers/")
        base_test.titleControl("Career", 10)
    
 
   
