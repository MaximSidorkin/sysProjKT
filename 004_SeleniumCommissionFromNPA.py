# СОЗДАНИЕ ПОРУЧЕНИЯ ИЗ РАЗДЕЛА НПА

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

    def test003_GotoNPA(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(3)
        # assert "NPA" in driver.title
        driver.find_element_by_link_text("Нормативно-правовые акты").click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))

    def test004_FilterSetting(self):
        time.sleep(3)
        driver.find_element_by_css_selector("span.title_executor").click()
        time.sleep(1)
        driver.find_element_by_id("btn_executor").click()
        time.sleep(1)
        driver.find_element_by_id("btn_success_executor").click()
        time.sleep(3)

    def test005_SelectRandomNPA(self):
        driver.find_element_by_xpath("//table[@id='load_table']/tbody/tr/td[2]").click()
        time.sleep(2)

    def test006_ClickPlus(self):
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div/div[2]/div[4]/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[2]/a").click()
        time.sleep(2)

    def test008_FillingCommissionForm(self):
        time.sleep(2)
        # заполняем название поручения
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Название поручения Selenium')
        # автор
        driver.find_element_by_id('Checkpoint_ID_AUTHOR_MISSIONSelectBoxItArrowContainer').click()
        driver.find_element_by_link_text('Багреева М.А.').click()
        # участвующие сотрудники
        # driver.find_element_by_css_selector('input.select2-search__field').send_keys('А'+Keys.ENTER)
        # ответственный
        driver.find_element_by_css_selector("span.select2-selection__arrow").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Абра'+Keys.ENTER)
        # deadline
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123'+Keys.ENTER)
        time.sleep(1)
        # save
        driver.find_element_by_id("mission_form_save").click()

    def test009_Del(self):
        time.sleep(3)
        driver.find_element_by_xpath("//strong[. = 'Название поручения Selenium' ]").click()
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        time.sleep(2)
        driver.find_element_by_id('mission_del').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element_by_id('mission_del').click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
