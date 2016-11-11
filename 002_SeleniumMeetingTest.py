# СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ СОВЕЩАНИЯ ИЗ БЛОКА "РАСПИСАНИЕ"
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
wait = WebDriverWait(driver, 20)
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
            print('test fall')

    def test_003_GotoScheduler(self):
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print('тест №3 - переход в раздел "Расписание"')

    def test_004_ClickCreateMeeting(self):
        time.sleep(4)
        crMeeting = driver.find_element_by_xpath("//div[@id='bs-example-navbar-collapse-3']/div[5]/div[2]").click()
        print('тест №4 - нажимаем кнопку "Создать" на открывшейся форме')

    def test_005_FillingMeetingForm(self):
        time.sleep(3)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Совещение созданное Selenium')
        invite = driver.find_element_by_id('MeetingsData_S_INVITED').send_keys('Внешнее приглашение Selenium')
        unit = driver.find_element_by_css_selector('ul.select2-selection__rendered').click()
        unit = driver.find_element_by_xpath('//form/div[5]/div/span/span[1]/span/ul/li/input').send_keys('Соловьев Е' + Keys.ENTER)
        place = driver.find_element_by_id('MeetingsData_S_PLACE').send_keys('Москва')
        responsibleName = driver.find_element_by_xpath('//div[8]/div/span/span/span/span[2]').click()
        time.sleep(2)
        responsibleName = driver.find_element_by_xpath('//body[@id="ui-id-1"]/span/span/span/input').send_keys('Багреева' + Keys.ENTER)
        comment = driver.find_element_by_id('MeetingsData_S_COMMENT').send_keys('комментарий к совещанию')
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('19:01' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('20:01' + Keys.ENTER)
        triggerAllDay = driver.find_element_by_css_selector('span.switch-right').click()
        time.sleep(2)
        triggerAllDay = driver.find_element_by_css_selector('span.switch-left').click()
        time.sleep(1)
        triggerOffer = driver.find_element_by_xpath('//form[@id="meetings-form"]/div[13]/div/div/div/span[2]').click()
        time.sleep(2)
        triggerOffer = driver.find_element_by_xpath("//form[@id='meetings-form']/div[13]/div/div/div/span").click()
        driver.save_screenshot('C:\PyTest\inish.png')
        print('тест №5 - заполняем форму создания совещания')
    #@unittest.skip('Test Skipped1')

    def test_006_Confirm(self):
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        print('тест №6 - подтверждаем создание совещание')

    def test_007_FindAndEditMeeting(self):
        time.sleep(4)
        driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:01 - 20:01' ]")
        newMeet.click()
        time.sleep(5)
        editButton = driver.find_element_by_xpath("//button[2]").click()
        time.sleep(3)
        project = driver.find_element_by_css_selector('span.input-group-addon').click()
        time.sleep(1)
        project = driver.find_element_by_xpath("//div[2]/div/div/input").send_keys('Тестовый проект созданный Selenium edit')
        time.sleep(1)
        project = driver.find_element_by_css_selector('span.find-text').click()
        driver.find_element_by_xpath('//div[2]/div/button').click()     # кликнуть по кнопке "выбрать"
        time.sleep(1)
        missionButton = driver.find_element_by_name('yt0').click()
        time.sleep(2)
        print('тест №7 - находим созданное совещание и редактируем его')

        time.sleep(4)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:01 - 20:01' ]").click()  # открываем совещание
        time.sleep(3)
        driver.find_element_by_css_selector('i.fa.fa-plus').click()  # нажимаем кнопку + и создаём поручение

    def test_008_FillingCommissionForm(self):
        time.sleep(3)
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Название поручения Selenium')
        # ответственный
        driver.find_element_by_xpath('//div[6]/div/span/span/span/span').click()
        driver.find_element_by_xpath('//span/input').send_keys('ip'+Keys.ENTER)
        # deadline
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123'+Keys.ENTER)
        # проект
        driver.find_element_by_xpath('//div[2]/div/div/div/div/div/span').click()
        driver.find_element_by_css_selector('input.form-control').send_keys('Проект для совещаний Se')
        time.sleep(4)
        # находим в выпадающем списке нужный пункт
        driver.implicitly_wait(10)
        time.sleep(1)
        driver.find_element_by_css_selector('span.find-text').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div/div[3]/span[2]').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_xpath('//div/div[3]/span[2]').click()
        time.sleep(2)
        print('тест №8 - создаем поучение и заполняем его форму')

    def test_009_Close(self):
        print('тест №9 - подтверждаем создание поручения/закрываем форму')

    def test_010_NewCommissionPlus(self):
        time.sleep(1)
        driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:01 - 20:01' ]")
        newMeet.click()
        time.sleep(2)
        driver.find_element_by_css_selector('i.fa.fa-plus').click()
        time.sleep(3)
        ASeleniumLogin_1.test_008_FillingCommissionForm(self)
        time.sleep(2)
        driver.find_element_by_id('btn_close').click()
        print('тест №10 - создаем поручение непосредственно из паспорта совещания путем нажатия кнопки "+"')

    def test_011_DelMeeting(self):
        time.sleep(2)
        driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:01 - 20:01' ]")
        newMeet.click()
        time.sleep(2)
        driver.find_element(By.XPATH,".//*[text()='Удалить']/..").click()
        time.sleep(3)
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        # driver.find_element(By.XPATH, ".//*[text()='Да']/..").click()
        print('тест №11 - удаляем созданное совещание')

    def test_012_AllDayMeeting(self):
        time.sleep(2)
        ASeleniumLogin_1.test_004_ClickCreateMeeting(self)
        time.sleep(2)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('All Day Selenium')
        time.sleep(2)
        triggerAllDay = driver.find_element_by_css_selector('span.switch-right').click()
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        time.sleep(2)
        print('тест №12 - создаем совещание на весь день')

    def test_013_DelAllDayMeeting(self):
        #newMeet = driver.find_element_by_xpath("//span[. = 'All Day Selenium' ]").click()
        driver.find_element_by_css_selector('span.fc-title').click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Да']/..").click()
        print('тест №13 - удаляем совещание созданное на весь день')

    def test_014_CreateMeetingFromDT(self):
        time.sleep(2)
        # переходим на рабочий стол
        driver.find_element_by_link_text("Рабочий стол").click()
        driver.implicitly_wait(15)
        time.sleep(5)
        # создаем совещание
        driver.find_element_by_xpath('//tr[23]/td[2]').click()
        time.sleep(2)
        # заполняем форму совещания
        # имя уникально
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Совещание с рабочего стола')
        invite = driver.find_element_by_id('MeetingsData_S_INVITED').send_keys('Внешнее приглашение Selenium')
        unit = driver.find_element_by_css_selector('ul.select2-selection__rendered').click()
        unit = driver.find_element_by_xpath('//form/div[5]/div/span/span[1]/span/ul/li/input').send_keys('Багреева' + Keys.ENTER)
        place = driver.find_element_by_id('MeetingsData_S_PLACE').send_keys('Москва')
        comment = driver.find_element_by_id('MeetingsData_S_COMMENT').send_keys('комментарий к совещанию')
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('19:08' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('20:08' + Keys.ENTER)
        time.sleep(2)
        # нажимаем кнопку создать
        driver.find_element_by_name('yt0').click()
        print('тест №14 - создаем совещание с рабочего стола')

    def test_015_GotoScheduller(self):
        time.sleep(4)
        driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print('тест №15 - переходим в раздел "Расписание"')

    def test_016_SearchDTMeeting(self):
        time.sleep(5)
        #driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:08 - 20:08' ]")
        newMeet.click()
        time.sleep(4)
        print('тест №16 - находим только что созданное совещение')

    def test_017_AddCommission(self):
        driver.find_element_by_css_selector('i.fa.fa-plus').click()
        time.sleep(4)
        ASeleniumLogin_1.test_008_FillingCommissionForm(self)
        time.sleep(2)
        driver.find_element_by_id('btn_close').click()
        print('тест №17 - создаем поучение и заполняем его форму')

    def test_018_CreateMeetingCopy(self):
        time.sleep(3)
        driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:08 - 20:08' ]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, ".//*[text()='Создать копию']/..").click()
        time.sleep(3)
        driver.find_element_by_name('yt0').click()
        print('тест №19 - переходим в раздел "Расписание", находим совещание, и создаём его копию')

    def test_019_Comment(self):
        time.sleep(3)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:08 - 20:08' ]").click()
        time.sleep(3)
        print('тест №20 - открываем паспорт совещание')

    def test_020_printComment(self):
        driver.find_element_by_name('notes').click()
        time.sleep(4)
        commentText = driver.find_element_by_id('NoteMeeting').click()  # send_keys('Hello, World!')
        driver.implicitly_wait(10)
        time.sleep(4)
        commentText = driver.find_element_by_xpath('//textarea').send_keys(' Hello, World! ')
        saveBtn = driver.find_element_by_css_selector('input.btn').click()
        print('тест №21 - создаем комментарий')

    def test_021_editComment(self):
        time.sleep(2)
        ASeleniumLogin_1.test_020_printComment(self)
        print('тест №22 - редактируем комментарий')

    def test_022_closeComment(self):
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='notes']/div/div/div[2]/a/i").click()
        print('тест №23 - закрываем форму комментария')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_MEETING.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ СОВЕЩАНИЯ ИЗ РАСПИСАНИЯ И РАБОЧЕГО СТОЛА',
        description='Отчет по тестированию'
    )
    runner.run(suite)