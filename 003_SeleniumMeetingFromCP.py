# СОЗДАНИЕ СОВЕЩАНИЯ ИЗ КОНТРОЛЬНОЙ ТОЧКИ
import time
import unittest, sys
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import HTMLTestRunner

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 40)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('тест №1 - логинимся в систему')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print('тест №2 - проверка на 404 и 500 ошибку после ввода логина/пароля')

    def test_003_OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print('тест №3 - переход в раздел "Все проекты"')

    def test_004_Not500or404(self):
        assert "Error" not in driver.title
        print('тест №4 - проверка страницы на ошибка 500/404')

    def test_005_OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(3)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('тест №5 - задаём в фильтре ключевое слово Selenium')

    def test_006_FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования')
        findBlock.click()
        time.sleep(2)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('тест №6 - выбираем блок')

    def test_007_FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(2)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('тест №7 - выбираем проект')

    def test_008_CreateCP(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_id('create-cp')
        CreateCP.click()
        time.sleep(5)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('тест №8 - открываем форму создания КТ')

    def test_009_FillingCPForm(self):
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(5)
        #имя контрольной точки
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("Совещание из КТ созданное Selenium")
        time.sleep(2)
        #ответственный
        driver.implicitly_wait(10)
        responsibleName = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]")
        responsibleName.click()
        time.sleep(2)
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('DIT' + Keys.ENTER)
        time.sleep(2)
        driver.implicitly_wait(10)
        time.sleep(2)
        #сроки
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123' + Keys.ENTER)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('тест №9 - заполняем форму КТ')

    def test_010_TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('тест №10 - подтверждаем создание КТ')

    def test_011_ConfirmCPCreating(self):
        finishButton = driver.find_element_by_name('yt0').click()
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        time.sleep(5)
        print('тест №11 - проверяем страницу на ошибки')

    def test_012_ClickEditButton(self):
        editButton = driver.find_element_by_name('yt0').click()
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        time.sleep(3)
        print('тест №12 - открываем форму редактирования КТ')

    def test_013_editCP(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('тест №13 - проверяем страницу на ошибки')

    def test_014_MeetingCreate(self):
        time.sleep(6)
        nap = driver.find_element_by_id("DIV_N_REALIZATION_TYPE").click()
        time.sleep(5)
        nap = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Совещание" + Keys.ENTER)
        time.sleep(5)
        #EditProject = driver.find_element_by_name('yt0').click()
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        driver.find_element_by_name('yt0').click()
        time.sleep(6)
        EditProject = driver.find_element_by_name('yt0').click()
        time.sleep(6)
        assert "ЭОР" in driver.title
        NPACr = driver.find_element_by_xpath('//button[text()="Создать совещание"]').click()
        time.sleep(5)
        print('тест №14 - устанавливаем форму реализации как Совещание')

    def test_015_FillingMeetingForm(self):
        time.sleep(5)
        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Совещение созданное Selenium из КТ')
        time.sleep(1)
        invite = driver.find_element_by_id('MeetingsData_S_INVITED').send_keys('Внешнее приглашение Selenium')
        time.sleep(1)
        #unit = driver.find_element_by_css_selector('ul.select2-selection__rendered').send_keys('Соловьев Е' + Keys.ENTER) # click()
        #time.sleep(1)
        #unit = driver.find_element_by_xpath('//form/div[5]/div/span/span[1]/span/ul/li/input').send_keys('Соловьев Е' + Keys.ENTER)
        #time.sleep(1)
        place = driver.find_element_by_id('MeetingsData_S_PLACE').send_keys('Москва')
        time.sleep(1)
        responsibleName = driver.find_element_by_xpath('//div[9]/div/span/span[1]/span/span[2]').click()
        time.sleep(2)
        responsibleName = driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Багреева' + Keys.ENTER)
        time.sleep(1)
        comment = driver.find_element_by_id('MeetingsData_S_COMMENT').send_keys('комментарий к совещанию')
        time.sleep(1)
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').clear()
        meetingDateB = driver.find_element_by_id('MeetingsData_D_START').send_keys('19:03' + Keys.ENTER)
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').clear()
        meetingDateE = driver.find_element_by_id('MeetingsData_D_END').send_keys('20:03' + Keys.ENTER)
        triggerAllDay = driver.find_element_by_css_selector('span.switch-right').click()
        time.sleep(1)
        triggerAllDay = driver.find_element_by_css_selector('span.switch-left').click()
        time.sleep(1)
        triggerOffer = driver.find_element_by_xpath('//form[@id="meetings-form"]/div[14]/div/div/div/span[2]').click()
        time.sleep(1)
        triggerOffer = driver.find_element_by_xpath("//form[@id='meetings-form']/div[14]/div/div/div/span").click()
        print('тест №15 - заполняем форму совещания')

    def test_016_ConfirmMeeting(self):
        time.sleep(3)
        driver.find_element_by_name('yt0').click()
        print('тест №16 - подтверждаем создание совещания')

    def test_017_ConfirmCP(self):
        time.sleep(5)
        t017 = driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        t017 = driver.find_element_by_name('yt0').click()
        print('тест №17 - подтверждаем создание КТ')

    def test_018_GotoScheduler(self):
        time.sleep(7)
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        print('тест №18 - переходим в раздел Расписание')

    def test_019_FindAndDelMeeting(self):
        time.sleep(7)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:03 - 20:03' ]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[3]").click()

        time.sleep(3)
        driver.find_element_by_name('yt0').click()
        print('тест №19 - находим созданное совещание и удаляем его')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CREATE_MEETING_FROM_CHECKPOINT.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ СОВЕЩАНИЯ ИЗ КОНТРОЛЬНОЙ ТОЧКИ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)