from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base

class QualityAssurancePageTest():
    
    def run(self, driver):

        base_test = Base(driver=driver)
        
        base_test.start("https://useinsider.com/careers/quality-assurance/")
        
        # sayfa doğrulama
        base_test.urlControl("useinsider.com/careers/quality-assurance/")
        base_test.titleControl("quality assurance", 10)
        
        #see all qa jobs butonuna tıkla
        base_test.clickElement_js('//*[@id="page-head"]/div/div/div[1]/div/div/a')
        
        # sayfa doğrulama
        base_test.urlControl("useinsider.com/careers/open-positions/?department=qualityassurance")
        base_test.titleControl("Open Positions", 10)