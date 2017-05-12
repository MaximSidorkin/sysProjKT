# СОЗДАНИЕ СОВЕЩАНИЯ ДЛЯ ПОЛЬЗОВАТЕЛЯ БЕЗ АКК. OUTLOOK С ПРИГЛАШЕНИЕМ ПОЛЬЗОВАТЕЛЯ С АКК. OUTLOOK
import unittest
import time
import os
import HTMLTestRunner, sys
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/site/login'

# global variable
driver = webdriver.Chrome()
driver.get(dev)
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 120)
driver.implicitly_wait(50)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Selenium_01")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("123")
        elem.send_keys(Keys.RETURN)
        print(' логинимся в систему')

    def test_002_Not500or404andLoginIsVisible(self):
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print(' проверка на 404 и 500 ошибку после ввода логина/пароля')
        try:
            driver.find_element_by_class_name('hidden-xs')
        except:
            self.fail(print('Не отобразился / не подгрузился логин пользователя'))

    def test_003_GotoScheduler(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' переход в раздел "Расписание"')

    def test_004_CreateMeeting(self):
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]")))
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' нажимаем кнопку "Создать" на открывшейся форме')

    def test_005_FillingMeetingForm(self):
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('От ipad найти в Outlook')
        place = driver.find_element_by_id('MeetingsData_S_PLACE').send_keys('Москва')
        driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys('ipad')
        time.sleep(2)
        driver.find_element_by_xpath('//div[5]/div/div/div/input').send_keys(Keys.ENTER)
        time.sleep(1)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('21:10' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('21:25' + Keys.ENTER)
        print(' заполняем форму создания совещания')

    def test_006_Confirm(self):
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        print(' подтверждаем создание совещание')

    def test_007_Relog(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print(' Перезаходим в систему под пользователем ipad/ipad ')

    def test_008_GotoScheduller(self):
        driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' Переход в раздел "Расписание" ')
        try:
            driver.find_element_by_xpath("//span[. = '21:10 - 21:25' ]")
            print(' Совещание от пользователя без акк. Outlook найдено в ЭОР')
        except:
            print(' ОШИБКА!\nСовещание от пользователя без акк. Outlook не найдено в ЭОР')

    def test_009_GotoOutlook(self):
        time.sleep(1)
        driver.set_page_load_timeout(20)
        driver.get("https://owa.mos.ru/")
        print(" Переходим в Outlook")
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        elem = driver.find_element_by_id("username")
        elem.send_keys("MarenovaTE")
        elem = driver.find_element_by_id("password")
        elem.send_keys("rTZmYVbx")
        elem.send_keys(Keys.RETURN)

    def test_010_openCalendar(self):
        time.sleep(1)
        driver.set_page_load_timeout(20)
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        #try:
            #driver.find_element_by_xpath(".//*[text()='Пользователь А Отв.: Афанасьев В.П.']/..").click()
        #    print(' Совещание созданное в ЭОР найдено')
        #except:
        #    print(' аутглюк завис')
        #time.sleep(2)
        #driver.find_element_by_xpath(".//*[text()='ИЗМЕНИТЬ']/..").click()

if __name__ == '__main__':
    unittest.main()
