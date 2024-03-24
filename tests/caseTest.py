from selenium import webdriver
from pages.homePage import HomePageTest
from pages.careerPage import CareerPageTest 
from pages.qualityAssurancePage import QualityAssurancePageTest
from pages.openPositionsPage import OpenPositionsPageTest
from pages.positionDetail import PositionDetailPageTest
from pages.formPage import FormPageTest 



def run_tests(browser="chrome"):

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("unexpected browser type")
        return        

    HomePageTest().run(driver=driver)
    CareerPageTest().run(driver=driver)
    QualityAssurancePageTest().run(driver=driver)
    OpenPositionsPageTest().run(driver=driver)
    PositionDetailPageTest().run(driver= driver)
    FormPageTest().run(driver = driver)
    
    driver.close()
    

run_tests()
