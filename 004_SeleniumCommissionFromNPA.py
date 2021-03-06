# СОЗДАНИЕ ПОРУЧЕНИЯ ИЗ РАЗДЕЛА НПА

import unittest, sys
import time
global str
import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/site/login'
perm = 'http://dev.perm.gosapi.ru/top/'

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get(pgs)
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

    def test_002_Not500or404andLoginIsVisible(self):
        time.sleep(5)
        print('тест №1 - логинимся в систему')
        try:
            driver.find_element_by_class_name('hidden-xs')
        except:
            self.fail(print('Не отобразился / не подгрузился логин пользователя'))

    def test_003_GotoNPA(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(3)
        driver.find_element_by_link_text("Нормативно-правовые акты").click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        print('тест №2 - переход в раздел "Нормативно-правовые акты"')

    def test_004_FilterSetting(self):
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.title_executor')))
        driver.find_element_by_css_selector("span.title_executor").click()
        time.sleep(1)
        driver.find_element_by_id("btn_executor").click()
        time.sleep(1)
        driver.find_element_by_id("btn_success_executor").click()
        time.sleep(3)
        print('тест №3 - устанавливаем фильтры')

    def test_005_SelectRandomNPA(self):
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@id='load_table']/tbody/tr/td[2]")))
        driver.find_element_by_xpath("//table[@id='load_table']/tbody/tr/td[2]").click()
        time.sleep(2)
        print('тест №4 - выбираем случайную КТ')

    def test_006_ClickPlus(self):
        time.sleep(1)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fa.fa-plus")))
        driver.find_element_by_css_selector("i.fa.fa-plus").click()
        time.sleep(2)
        print('тест №5 - кликаем по знакчку + "Создать поручение"')

    def test_008_FillingCommissionForm(self):
        time.sleep(2)
        # заполняем название поручения
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Название поручения Selenium')
        # автор
        driver.find_element_by_xpath('//div[7]/div/span/span/span/span[2]').click()
        driver.find_element_by_xpath('//span/input').send_keys('А'+Keys.ENTER)
        # deadline
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123'+Keys.ENTER)
        time.sleep(1)
        # save
        driver.find_element_by_xpath("//div/div[3]/span[2]").click()
        print('тест №6 - заполняем форму поручения и сохраняем его')

    def test_009_Del(self):
        time.sleep(2)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//strong[. = 'Название поручения Selenium' ]")))
        driver.find_element_by_xpath("//strong[. = 'Название поручения Selenium' ]").click()
        time.sleep(3)
        driver.find_element_by_name('yt2').click()  # find Delete button and click
        time.sleep(3)
        driver.find_element_by_xpath('//div[3]/div/button').click() #delete commission
        print('тест №7 - находим созданное поучние и удаляем его')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_COMMISSION_FROM_NPA.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ ПОРУЧЕНИЯ ИЗ РАЗДЕЛА НПА',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)
