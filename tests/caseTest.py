import mysql.connector
from selenium import webdriver
from pages.homePage import HomePageTest
from pages.careerPage import CareerPageTest
from pages.qualityAssurancePage import QualityAssurancePageTest
from pages.openPositionsPage import OpenPositionsPageTest
from pages.positionDetail import PositionDetailPageTest
from pages.formPage import FormPageTest


def log_test_result(test_name, result):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1", user="root", password="admin", database="bootcampDB"
        )
        cursor = conn.cursor()
        query = "INSERT INTO case_reports (case_name, case_status) VALUES (%s, %s)"
        cursor.execute(query, (test_name, result))
        conn.commit()
        print("Test result logged successfully.")
    except Exception as e:
        print("Error while logging test result:", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def run_tests(browser="chrome"):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Unexpected browser type")
        return

    try:
        HomePageTest().run(driver=driver)
        log_test_result("HomePageTest", "Passed")
    except Exception as e:
        print("An error occurred during test execution:", e)
        log_test_result("HomePageTest", "Failed")

    try:
        CareerPageTest().run(driver=driver)
        log_test_result("CareerPageTest", "Passed")
    except Exception as e:
        print("An error occurred during test execution:", e)
        log_test_result("CareerPageTest", "Failed")

    try:
        QualityAssurancePageTest().run(driver=driver)
        log_test_result("QualityAssurancePageTest", "Passed")
    except Exception as e:
        print("An error occurred during test execution:", e)
        log_test_result("QualityAssurancePageTest", "Failed")

    try:
        OpenPositionsPageTest().run(driver=driver)
        log_test_result("OpenPositionsPageTest", "Passed")
    except Exception as e:
        print("An error occurred during test execution:", e)
        log_test_result("OpenPositionsPageTest", "Failed")

    try:
        PositionDetailPageTest().run(driver=driver)
        log_test_result("PositionDetailPageTest", "Passed")
    except Exception as e:
        print("An error occurred during test execution:", e)
        log_test_result("PositionDetailPageTest", "Failed")

    # try:
    #     FormPageTest().run(driver=driver)
    #     log_test_result("FormPageTest", "Passed")
    # except Exception as e:
    #     print("An error occurred during test execution:", e)
    #     log_test_result("FormPageTest", "Failed")

    finally:
        driver.close()


run_tests()
