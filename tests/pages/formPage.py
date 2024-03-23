from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base

class FormPageTest():
    
    def run(self, driver):
        
        base_test = Base(driver=driver)
        # sayfa doğrulama
        base_test.start("https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436/apply") 
        base_test.urlControl("https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436/apply") 
        base_test.titleControl("Software QA Tester")
        
        #form kontrolü
        form_control = WebDriverWait(base_test.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'application-form'))
        )
        print("Form açıldı")
