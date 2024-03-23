from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from fonksiyonlar import fonksiyonlar as fn

class positionDetailPageTest():
    # sayfa doğrulama
    fn.urlControl("https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436")
    fn.titleControl("Software QA Tester", 10)
    
    #açılan ilan sayfasındaki buton kontrolü ve tıklanması
    fn.clickElement('/html/body/div[3]/div/div[1]/div/div[2]/a', 10)