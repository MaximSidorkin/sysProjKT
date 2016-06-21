# СОЗДАНИЕ КОНТРОЛЬНОЙ ТОЧКИ ИЗ БЛОКА ПРОЕКТОВ
import unittest
import time
global str
import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# global variable
driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
time.sleep(3)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

    def test002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        try:
            driver.find_element_by_class_name('hidden-xs')
        except:
            print('test fall')

    def test003_GotoRating(self):
        time.sleep(2)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        report = driver.find_element_by_link_text("Отчёты")
        report.click()
        time.sleep(1)
        rating = driver.find_element_by_link_text('Отчёт Рейтинги')
        rating.click()
        time.sleep(4)
    def test004_FilterSetting(self):
        driver.find_element_by_css_selector('span.title_gears').click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[2]/ul/li[1]/ul/li[1]/div/label[1]/div").click()
        time.sleep(1)
        driver.find_element_by_id('btn_success_gears').click()
        time.sleep(2)
    def test005_EditCP(self):
        driver.find_element_by_css_selector('span.cp-title').click()
        time.sleep(3)
        driver.find_element_by_name('yt0').click()
        time.sleep(4)
        driver.find_element_by_id('Checkpoint_PLANNED_RESULT').send_keys(' Новый комментарий')
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='cancel']").click()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("Report.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='Test the Report',
        description='Result of tests'
    )
    runner.run(suite)