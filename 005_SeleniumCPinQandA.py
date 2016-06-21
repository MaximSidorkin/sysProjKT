# СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ КТ ИЗ ВИДЖЕТА "ВОПРОСЫ И ОТВЕТЫ" В ПАСПОРТЕ СОВЕЩАНИЯ
import unittest
import time

import os
import HTMLTestRunner
from selenium.webdriver.support.ui import Select

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
time.sleep(2)
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
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')
        print('тест №1 - логинимся в систему')

    def test002_Not500or404andLoginIsVisible(self):
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print('тест №2 - проверка на 404 и 500 ошибку после ввода логина/пароля')
        try:
            driver.find_element_by_class_name('hidden-xs')
        except:
            print('test fall')

    def test003_GotoScheduler(self):
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        assert 'Error' not in driver.title
        print('тест №3 - переход в раздел "Расписание"')

    def test004_OpenMeetingForm(self):
        assert 'Error' not in driver.title
        time.sleep(2)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:02 - 20:02' ]").click()
        time.sleep(3)
        driver.find_element_by_id('add_manual_cp').click()
        time.sleep(3)
        driver.find_element_by_id('Agenda_S_NAME').send_keys('Selenium создал очень важный вопрос')
        time.sleep(2)
        driver.find_element_by_xpath("//form[@id='agenda-form']/div[3]/div/span/span/span/span[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys("Багреева"+Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='search']").send_keys('Selenium')
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id("btn_close").click()
        print('тест №4 - открываем паспорт совещания и создаём вопрос из виджета путем нажатия на "+" и ввода текста в поле поиска виджета')

        assert 'Error' not in driver.title

    def test005_DelOneQuestion(self):
        assert 'Error' not in driver.title
        time.sleep(2)
        # task_remove
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:02 - 20:02' ]").click()
        time.sleep(2)
        driver.find_element_by_css_selector('span.task_remove').click()
        assert not 'Error' in driver.title
        print('тест №5 - открываем паспорт совещания и удаляем один из вопросов в виджете')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
            # File
    buf = open("Report.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=buf,
    title=' СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ КТ ИЗ ВИДЖЕТА "ВОПРОСЫ И ОТВЕТЫ" В ПАСПОРТЕ СОВЕЩАНИЯ',
    description='Отчет по тесту'
    )
    runner.run(suite)