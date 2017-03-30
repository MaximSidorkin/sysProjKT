# РЕДАКТИРОВАНИЕ КОНТРОЛЬНОЙ ТОЧКИ ИЗ РЕЙТИНГОВ
import unittest
import time
global str
import HTMLTestRunner, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# global variable
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/new/")
driver.maximize_window()
time.sleep(3)
wait = WebDriverWait(driver, 50)
driver.implicitly_wait(20)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('тест №1 - логинимся в систему')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print('тест №2 - проверка на 404 и 500 ошибку после ввода логина/пароля')
        try:
            driver.find_element_by_class_name('hidden-xs')
        except:
            self.fail(print('Не отобразился / не подгрузился логин пользователя'))

    def test_003_GotoRating(self):
        wait = WebDriverWait(driver, 15)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        driver.find_element_by_css_selector("i.entypo-menu").click()
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Отчёты")))
        driver.find_element_by_link_text("Отчёты").click()
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Отчёт по контрольным точкам")))
        driver.find_element_by_link_text('Отчёт по контрольным точкам').click()
        print('тест №3 - переходим в раздел Отчёт Рейтинги')

    def test_004_FilterSetting(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.title_executor")))
        driver.find_element_by_css_selector("span.title_executor").click()
        driver.find_element_by_id('btn_executor').click()
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Selenium')
        driver.find_element_by_id('search-text-push').click()
        print('тест №4 - устанавливаем фильтры')

    def test_005_EditCP(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.find-text")))
        driver.find_element_by_css_selector('span.find-text').click()
        _ = wait.until(EC.element_to_be_clickable((By.NAME, "yt0")))
        driver.find_element_by_name('yt0').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, "Checkpoint_TITLE")))
        driver.find_element_by_id('Checkpoint_TITLE').send_keys(' ред. из Отчёта по контрольным точкам')
        driver.find_element_by_xpath("//form/div/div[3]/span[2]").click()
        print('тест №5 - редактируем КТ')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CREATION_CHECKPOINT_FROM_RATING.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='РЕДАКТИРОВАНИЕ КОНТРОЛЬНОЙ ТОЧКИ ИЗ РЕЙТИНГОВ',
        description='Отчет по тесту'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)