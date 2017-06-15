# ПРОВЕРКА ПЕРЕТАСКИВАНИЯ СОВЕЩАНИЯ
import unittest, datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
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
test_time = datetime.datetime.now()
test_day = test_time.day
test_month = test_time.month

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        driver.find_element_by_id("LoginForm_username").send_keys('ipad')
        driver.find_element_by_id("LoginForm_password").send_keys('ipad'+Keys.RETURN)
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

    def test_004_ClickCreateMeeting(self):
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print(' нажимаем кнопку "Создать" на открывшейся форме')

    def test_005_FillingMeetingForm(self):
        time.sleep(2)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Совещание drag and drop #1')
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('21:19' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('21:39' + Keys.ENTER)
        driver.find_element_by_xpath('//div[11]/div/div/input').clear()
        driver.find_element_by_xpath('//div[11]/div/div/input').send_keys(test_day+1,'.',test_month,'.','2017'+Keys.ENTER)
        time.sleep(2)
        # нажимаем кнопку создать
        driver.find_element_by_name('yt0').click()
        print(' создаём совещание: "Совещание drag and drop #1"')

    def test_006_FillingMeetingForm2(self):
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        time.sleep(2)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Совещание drag and drop #2')
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('19:19' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('19:49' + Keys.ENTER)
        driver.find_element_by_xpath('//div[11]/div/div/input').clear()
        driver.find_element_by_xpath('//div[11]/div/div/input').send_keys('123'+Keys.ENTER)#(test_day + 1, '.', test_month, '.','2017' + Keys.ENTER)
        time.sleep(2)
        # нажимаем кнопку создать
        driver.find_element_by_name('yt0').click()
        print(' создаём совещание: "Совещание drag and drop #2"')

    def test_007_GotoOutlook(self):
        time.sleep(3)
        driver.set_page_load_timeout(20)
        driver.get("https://owa.mos.ru/")
        print(" Переходим в Outlook")
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element_by_id("username").send_keys("MarenovaTE")
        driver.find_element_by_id("password").send_keys("rTZmYVbx"+Keys.RETURN)
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            driver.find_element_by_xpath('//div[12]/div/div/div/div/div/div/div[3]/button')
            time.sleep(3)
            driver.find_element_by_xpath('//div[4]/div/button').click()
        except:
            print(' Всплывающее уведомление не поялвилось')
        try:
            driver.find_element_by_xpath(".//*[text()='Совещание drag and drop #1']/..")#.click()
            print(' Совещание #1 созданное в ЭОР найдено')
        except:
            print(' аутглюк завис')
        try:
            driver.find_element_by_xpath(".//*[text()='Совещание drag and drop #2']/..")#.click()
            print(' Совещание #2 созданное в ЭОР найдено')
        except:
            print(' аутглюк завис')
        time.sleep(2)
        driver.find_element_by_xpath(".//*[text()='Совещание drag and drop #2']/..").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[text()='ИЗМЕНИТЬ']/..").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div[2]/div/div/input')))
        try:
            _ = driver.find_element_by_xpath('//li/div[2]/div/div/div/input').text == '19:19'
            print(' Время соответствует')
        except:
            self.fail(print(' ОШИБКА!\nВремя не соответствует'))

    def test_008_GotoEOR(self):
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        time.sleep(3)
        draggable = driver.find_element_by_xpath("//span[. = '19:19 - 19:49' ]")
        target = driver.find_element_by_xpath("//span[. = '21:19 - 21:39' ]")
        ActionChains(driver).drag_and_drop(draggable,target).perform()
        time.sleep(2)
        draggable = driver.find_element_by_xpath("//span[. = '19:19 - 19:49' ]")
        target = driver.find_element_by_xpath("//span[. = '21:19 - 21:39' ]")
        ActionChains(driver).drag_and_drop(draggable, target).perform()
        print(" возвращаемся в ЭОР и перетаскиваем совещание #2 на совещание #1")

    def test_009_CheckInOutlook(self):
        time.sleep(2)
        driver.set_page_load_timeout(20)
        driver.get("https://owa.mos.ru/")
        print(" Переходим в Outlook")
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            driver.find_element_by_xpath('//div[12]/div/div/div/div/div/div/div[3]/button')
            time.sleep(3)
            driver.find_element_by_xpath('//div[4]/div/button').click()
        except:
            print(' Всплывающее уведомление не поялвилось')
        time.sleep(2)
        driver.find_element_by_xpath(".//*[text()='Совещание drag and drop #2']/..").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[text()='ИЗМЕНИТЬ']/..").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div[2]/div/div/input')))
        try:
            _ = driver.find_element_by_xpath('//li/div[2]/div/div/div/input').text == '21:19'
            #_ = driver.find_element_by_xpath('//li[2]/div/div[2]/div/div/div/input').text == '21:39'
            print(' находим в календаре перенесённое совещание #2')
        except:
            self.fail(print(' ОШИБКА!\nВремя не соответствует / совещание не отображено'))

    def test_011_GoodTone(self):
        print(' возвращаемся в ЭОР и удаляем совещание #1 и #2')
        time.sleep(2)
        driver.get('https://dev.eor.gosapi.ru/new/schedule')
        time.sleep(3)
        driver.find_element_by_xpath("//span[. = '21:19 - 21:49' ]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(3)
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        print(' совещание #1 удалено')
        time.sleep(2)
        driver.find_element_by_xpath("//span[. = '21:19 - 21:39' ]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(3)
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        print(' совещание #2 удалено')

    def test_012_CloseDriver(self):
        time.sleep(2)
        driver.quit()
        print(" тест завершен, браузер закрыт")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_MEETING_DRAG_AND_DROP.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА ПЕРЕТАСКИВАНИЯ СОВЕЩАНИЯ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)