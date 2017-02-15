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

# global variable
driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/new/")
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 120)
driver.implicitly_wait(50)

class ASeleniumLogin_1(unittest.TestCase):
    def test_000_crMeetForUserA(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print(' логинимся в систему')

        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' переход в раздел "Расписание"')

        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        time.sleep(3)
        driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Пользователь А')
        driver.find_element_by_xpath('//div[8]/div/span/span/span/span[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//body[@id="ui-id-1"]/span/span/span/input').send_keys('Афанасьев' + Keys.ENTER)
        driver.find_element_by_id('MeetingsData_D_START').clear()
        driver.find_element_by_id('MeetingsData_D_START').send_keys('20:22' + Keys.ENTER)
        driver.find_element_by_id('MeetingsData_D_END').clear()
        driver.find_element_by_id('MeetingsData_D_END').send_keys('20:52' + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_name('yt0').click()

        print(' Проверка передачи изменений в совещании для\n '
              'пользователя А(+ outlook acc.) и Б (- outlook acc.) \n'
              '- Заполняем форму создания совещания для пользоватлея А (ipad)')

    def test_001_gotoOutlook(self):
        time.sleep(3)
        driver.set_page_load_timeout(20)
        driver.get("https://owa.mos.ru/")
        print(" Переходим в Outlook")
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        elem = driver.find_element_by_id("username")
        elem.send_keys("MarenovaTE")
        elem = driver.find_element_by_id("password")
        elem.send_keys("rTZmYVbx")
        elem.send_keys(Keys.RETURN)

    def test_002_openCalendar(self):
        driver.set_page_load_timeout(20)
        driver.find_element(By.XPATH, ".//*[text()='Календарь']/..").click()
        try:
            driver.find_element_by_xpath(".//*[text()='Пользователь А Отв.: Афанасьев В.П.']/..").click()
            print(' Совещание созданное в ЭОР найдено')
        except:
            print(' аутглюк завис')
        time.sleep(2)
        driver.find_element_by_xpath(".//*[text()='ИЗМЕНИТЬ']/..").click()

    def test_003_ConfirmField(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div[2]/div/div/input')))
        try:
            _ = driver.find_element_by_xpath(
                '//div[2]/div[2]/div[2]/div/div/input').text == 'Пользователь А Отв.: Афанасьев В.П.'
            print(' Текст названия и ответственного соответствует')
        except:
            self.fail(print(' ОШИБКА!'
                            '\nТекст названия и ответственного соответствует'))
        try:
            _ = driver.find_element_by_xpath('//li/div[2]/div/div/div/input').text == '20:22'
            print(' Время соответствует')
        except:
            self.fail(print(' ОШИБКА!\n'
                            'Время совещания не соответствует'))

    def test_004_reLogInEOR(self):
        time.sleep(3)
        driver.get("https://dev.eor.gosapi.ru/new/")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("login")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("login")
        elem.send_keys(Keys.RETURN)
        print(' Перезаходим в систему под пользователем login/login ')

    def test_005_gotoMeet(self):
        driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print(' Переход в раздел "Расписание" ')

    def test_006_searchMeet(self):
        time.sleep(1)
        try:
            driver.find_element_by_xpath("//span[. = '20:22 - 20:52' ]")
            print(' Совещание найдено')
        except:
            self.fail(print(' ОШИБКА!\n'
                            'совещание не найдено'))

    def test_007_reLogInEOR(self):
        time.sleep(1)
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

    def test_008_gotoMeet(self):
        ASeleniumLogin_1.test_005_gotoMeet(self)
        driver.find_element_by_xpath("//span[. = '20:22 - 20:52' ]").click()
        print(' В разеде "Расписание" находим совещание')

    def test_009_editMeet(self):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[2]')))
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(1)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').click()
        time.sleep(1)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        time.sleep(1)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('20:23' + Keys.ENTER)
        time.sleep(1)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('20:52' + Keys.ENTER)
        driver.save_screenshot('time_bug.jpg')
        driver.find_element_by_name('yt0').click()
        print(" Редактируем совещание - изменяем время")

    def test_010_reLogInEOR(self):
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("login")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("login")
        elem.send_keys(Keys.RETURN)
        print(' Перезаходим в систему под пользователем login/login ')

    def test_011_gotoMeet(self):
        time.sleep(1)
        ASeleniumLogin_1.test_005_gotoMeet(self)

    def test_012_searchMeet(self):
        time.sleep(1)
        try:
            driver.find_element_by_xpath("//span[. = '20:23 - 20:52' ]")
            print(' Совещание найдено')
        except:
            self.fail(print(' ОШИБКА!\n'
                            'совещание не найдено'))

    def test_013_gotoOutlook(self):
        time.sleep(1)
        driver.get("https://owa.mos.ru/")
        driver.set_page_load_timeout(20)
        # 25
        ASeleniumLogin_1.test_002_openCalendar(self)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div[2]/div/div/input')))
        driver.find_element_by_xpath('//li/div[2]/div/div/div/input').clear()
        driver.find_element_by_xpath('//li/div[2]/div/div/div/input').send_keys('20:24')
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='СОХРАНИТЬ']/..").click()
        print(' Переходим в Outlook, раздел календарь редактируем совещание')

    def test_014_gotoEOR(self):
        print('Запускаем синхронизатор')
        # синхронизируем outlook - ЕОР
        time.sleep(4)
        driver.get("https://dev.eor.gosapi.ru/new/")
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn-ewsup')))
        driver.find_element_by_id('btn-ewsup').click()
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'COMPLETE')]")))
            print(' Синхронизация прошла успешно ')
        except:
            self.fail(print(' \n \n ОШИБКА СИНХРОНИЗАЦИИ \n \n'))
            # переходим в ЭОР для login и проверяем время совещания
        ASeleniumLogin_1.test_005_gotoMeet(self)
        try:
            driver.find_element_by_xpath("//span[. = '20:24 - 20:53' ]")
            print(' Совещание найдено')
        except:
            self.fail(print(' ОШИБКА!\n'
                            'совещание не найдено'))

    def test_015_GoodTone(self):
        ASeleniumLogin_1.test_007_reLogInEOR(self)
        ASeleniumLogin_1.test_005_gotoMeet(self)
        driver.find_element_by_xpath("//span[. = '20:24 - 20:53' ]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Удалить']/..")))
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(3)
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        print(' Перезаходим в ЭОР под пользователем ipad, находим созданное совещание и удаляем его')
        time.sleep(3)
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_MEETING_FOR_2_USERS.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ СОВЕЩАНИЯ ИЗ РАСПИСАНИЯ И OUTLOOK ДЛЯ ПОЛЬЗОВАТЕЛЕЙ С УЧЕТНОЙ ЗАПИСЬЮ OUTLOOK И БЕЗ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)
