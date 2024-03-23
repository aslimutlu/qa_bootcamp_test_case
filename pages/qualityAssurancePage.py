from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from fonksiyonlar import fonksiyonlar as fn

class qualityAssurancePageTest():
    # sayfa doğrulama
    fn.urlControl("useinsider.com/careers/quality-assurance/")
    fn.titleControl("quality assurance", 10)
    
    #see all qa jobs butonuna tıkla
    fn.clickElement_js('//*[@id="page-head"]/div/div/div[1]/div/div/a')