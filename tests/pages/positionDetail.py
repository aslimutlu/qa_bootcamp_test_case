from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base import Base

class PositionDetailPageTest():
    
    
    def run(self, driver):
        base_test = Base(driver=driver)
        
        base_test.start("https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436")
        
        #açılan ilan sayfasındaki buton kontrolü ve tıklanması
        base_test.clickElement('/html/body/div[3]/div/div[1]/div/div[2]/a', 10)
        
        # sayfa doğrulama
        base_test.urlControl("https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436/apply") 
        base_test.titleControl("Software QA Tester",10)