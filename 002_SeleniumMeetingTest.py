# СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ СОВЕЩАНИЯ ИЗ БЛОКА "РАСПИСАНИЕ"
import unittest
import time
#import pytest
import xmlrunner
import os
import HTMLTestRunner
from selenium.webdriver.support.ui import Select

#import io
#from io import StringIO
#from email.generator import Generator
#fp = StringIO()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# global variable
driver = webdriver.Firefox()
driver.get("http://dev.eor.gosapi.ru/site/login")
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

    def test002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        try:
            driver.find_element_by_class_name('hidden-xs')
        except:
            print('test fall')

    def test003_GotoScheduler(self):
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))

    def test004_ClickCreateMeeting(self):
        time.sleep(1)
        crMeeting = driver.find_element_by_xpath('//div[@id="bs-example-navbar-collapse-3"]/div[6]/div[2]').click()

    def test005_FillingMeetingForm(self):
        time.sleep(3)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Совещение созданное Selenium')
        invite = driver.find_element_by_id('MeetingsData_S_INVITED').send_keys('Внешнее приглашение Selenium')
        unit = driver.find_element_by_css_selector('ul.select2-selection__rendered').click()
        unit = driver.find_element_by_xpath('//form/div[5]/div/span/span[1]/span/ul/li/input').send_keys('Багреева' + Keys.ENTER)
        place = driver.find_element_by_id('MeetingsData_S_PLACE').send_keys('Москва')
        responsibleName = driver.find_element_by_xpath('//div[8]/div/span/span/span/span[2]').click()
        time.sleep(1)
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
    #@unittest.skip('Test Skipped1')
    def test006_Confirm(self):
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
    def test007_FindAndEditMeeting(self):
        time.sleep(4)
        driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:01 - 20:01' ]")
        newMeet.click()
        time.sleep(3)
        editButton = driver.find_element_by_xpath("//button[2]").click()
        time.sleep(3)
        project = driver.find_element_by_id('ncp-text').click()
        time.sleep(1)
        project = driver.find_element_by_xpath("//div[@id='ncp-tree-container']/div/input").send_keys('Тестовый проект созданный Selenium edit')
        time.sleep(1)
        project = driver.find_element_by_css_selector('span.find-text').click()
        time.sleep(1)
        missionButton = driver.find_element_by_id('mission-btn').click()
        time.sleep(2)
    def test008_FillingCommissionForm(self):
        # заполняем название поручения
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Название поручения Selenium')
        # автор
        driver.find_element_by_id('Checkpoint_ID_AUTHOR_MISSIONSelectBoxItArrowContainer').click()
        driver.find_element_by_link_text('Багреева М.А.').click()
        # участвующие сотрудники
        driver.find_element_by_css_selector('input.select2-search__field').send_keys('А'+Keys.ENTER)
        # ответственный
        driver.find_element_by_xpath("//form[@id='mission-form']/div/div/div[4]/div/span/span/span/span[2]").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('А'+Keys.ENTER)
        # deadline
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123'+Keys.ENTER)
        # проект
        driver.find_element_by_id('mission-text').click()
        driver.find_element_by_xpath('//div[10]/div/div[1]/div[2]/div[1]/input').send_keys('Проект для совещаний Se')
        time.sleep(2)
        # находим в выпадающем списке нужный пункт
        # driver.find_element_by_xpath("//*[@id='mission9871_anchor']/descendant::span[text()='Тестовый проект созданный selenium edit']")
        driver.find_element_by_xpath('//form/div/div/div[10]/div/div[1]/div[2]/div[2]/ul/li[15]/ul/li/a/span/span').click()
        # закончит редактирвоание совещания
        driver.find_element_by_id('mission_create').click()
        time.sleep(2)
        driver.find_element_by_id('mission_close').click()
        time.sleep(2)
    def test009_Close(self):
        driver.find_element_by_name('yt1').click()
        #submit = driver.find_element_by_name("yt1").click()

    def test010_NewCommissionPlus(self):
        time.sleep(1)
        driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:01 - 20:01' ]")
        newMeet.click()
        time.sleep(2)
        driver.find_element_by_css_selector('i.fa.fa-plus').click()
        time.sleep(3)
        ASeleniumLogin_1.test008_FillingCommissionForm(self)
        time.sleep(2)
        driver.find_element_by_id('btn_close').click()

    def test011_DelMeeting(self):
        time.sleep(2)
        driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:01 - 20:01' ]")
        newMeet.click()
        time.sleep(2)
        driver.find_element(By.XPATH,".//*[text()='Удалить']/..").click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Да']/..").click()

    def test012_AllDayMeeting(self):
        time.sleep(2)
        ASeleniumLogin_1.test004_ClickCreateMeeting(self)
        time.sleep(2)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('All Day Selenium')
        time.sleep(2)
        triggerAllDay = driver.find_element_by_css_selector('span.switch-right').click()
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        time.sleep(2)

    def test013_DelAllDayMeeting(self):
        #newMeet = driver.find_element_by_xpath("//span[. = 'All Day Selenium' ]").click()
        driver.find_element_by_css_selector('span.fc-title').click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Удалить']/..").click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Да']/..").click()

    def test014_CreateMeetingFromDT(self):
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
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('19:02' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('20:02' + Keys.ENTER)
        time.sleep(2)
        # нажимаем кнопку создать
        driver.find_element_by_name('yt0').click()

    def test015_GotoScheduller(self):
        time.sleep(3)
        schedul = driver.find_element_by_link_text("Расписание").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))

    def test016_SearchDTMeeting(self):
        time.sleep(5)
        #driver.implicitly_wait(10)
        newMeet = driver.find_element_by_xpath("//span[. = '19:02 - 20:02' ]")
        newMeet.click()
        time.sleep(3)
    def test017_AddCommission(self):
        driver.find_element_by_css_selector('i.fa.fa-plus').click()
        time.sleep(3)
        ASeleniumLogin_1.test008_FillingCommissionForm(self)
        time.sleep(2)
        driver.find_element_by_id('btn_close').click()

    def test018_FindDTMeetingInReport(self):
        time.sleep(3)
        driver.find_element_by_link_text("Отчёты").click()
        time.sleep(1)
        driver.find_element_by_link_text("Отчёт по контрольным точкам").click()
        time.sleep(5)
        # настраиваем фильтр "проекты"
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li/a/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li/ul/li[5]/span[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li/ul/li[5]/span[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li/a/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li/ul/li[1]/div/input').send_keys('Проект для совещаний Se'+ Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_css_selector('span.find-text').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[2]/li/ul/li[5]/span[3]').click()

        # ответственный клик по квадрату
        time.sleep(2)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[5]/li/a/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[5]/li/ul/li[1]/div/input').send_keys('Абрамов')
        time.sleep(1)
        driver.find_element_by_xpath('//ul[5]/li/ul/li[3]/div/ul/li[8]/div/label[1]/div').click()
        time.sleep(1)
        driver.find_element_by_id('btn_success_executor').click()

if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(ASeleniumLogin_1)

    # I thought you want to run the HTMLTestRunner
    # unittest.TextTestRunner(verbosity=2).run(suite)

    #outfile = open(r"C:\PyTest\TestReport.html", "w")
    # double \ or raw string r""

    #runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='This is demo')
    #runner.run(suite)

    #outfile.close()
    unittest.main()
