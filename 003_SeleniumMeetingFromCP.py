# СОЗДАНИЕ СОВЕЩАНИЯ ИЗ КОНТРОЛЬНОЙ ТОЧКИ
import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
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

    def test003_OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    def test004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test005_OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        #btn1 = driver.find_element_by_id("create-cp")
        #btn1.click()
        time.sleep(3)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(3)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test006_FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования')
        findBlock.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test007_FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test008_CreateCP(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_id('create-cp')
        CreateCP.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test009_FillingCPForm(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(2)
        #имя контрольной точки
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("Совещание из КТ созданное Selenium")
        time.sleep(2)
        #автор
        autorName = driver.find_element_by_id('DIV_AUTHOR_MISSION').click()
        #autorName = driver.find_element_by_xpath('//div[9]/div/span/span/span/span[2]')
        #autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Б' + Keys.ENTER)
        time.sleep(2)
        #ответственный
        responsibleName = driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        #responsibleName = driver.find_element_by_xpath('//div[10]/div/span/span/span/span[2]')
        #responsibleName.click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('DIT' + Keys.ENTER)
        time.sleep(2)
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123' + Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test010_TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        #time.sleep(1)
        #туда
        #triggerKPI = driver.find_element_by_xpath("//div[@id='DIV_IS_PRIORITY']/div/div/div/label")
        #triggerKPI.click()
        #time.sleep(1)
        #triggerDone = driver.find_element_by_xpath("//div[@id='DIV_IS_DONE']/div/div/div/span[2]")
        #triggerDone.click()
        time.sleep(4)
        #и обратно
        #triggerKPI.click()
        #time.sleep(1)
        #triggerDone.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test011_ConfirmCPCreating(self):
        finishButton = driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(5)

    def test012_ClickEditButton(self):
        editButton = driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

    def test013_editCP(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        #triggerKPI = driver.find_element_by_xpath("//div[@id='DIV_IS_PRIORITY']/div/div/div/label").click()
        #time.sleep(1)
        #triggerDone = driver.find_element_by_xpath("//div[@id='DIV_IS_DONE']/div/div/div/span[2]").click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test014_MeetingCreate(self):
        time.sleep(3)
        nap = driver.find_element_by_id("DIV_N_REALIZATION_TYPE").click()
        time.sleep(2)
        nap = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Совещание" + Keys.ENTER)
        time.sleep(2)
        EditProject = driver.find_element_by_name('yt0').click()
        time.sleep(4)
        EditProject = driver.find_element_by_name('yt0').click()
        time.sleep(2)
        assert "ЭОР" in driver.title
        NPACr = driver.find_element_by_xpath('//button[text()="Создать совещание"]').click()
        time.sleep(2)

    def test015_FillingMeetingForm(self):
        time.sleep(5)

        name = driver.find_element_by_id('MeetingsData_S_NAME').send_keys('Совещение созданное Selenium из КТ')
        time.sleep(1)
        invite = driver.find_element_by_id('MeetingsData_S_INVITED').send_keys('Внешнее приглашение Selenium')
        time.sleep(1)
        unit = driver.find_element_by_css_selector('ul.select2-selection__rendered').send_keys('Соловьев Е' + Keys.ENTER) # click()
        time.sleep(1)
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

    def test016_ConfirmMeeting(self):
        time.sleep(1)
        driver.find_element_by_name('yt0').click()

    def test017_ConfirmCP(self):
        time.sleep(3)
        t017 = driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        t017 = driver.find_element_by_name('yt0').click()

    def test018_GotoScheduler(self):
        time.sleep(4)
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()

    def test019_FindAndDelMeeting(self):
        time.sleep(4)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[. = '19:03 - 20:03' ]").click()
        time.sleep(3)
        # driver.find_element(By.XPATH,".//*[text()='Удалить']/..").click()
        # time.sleep(2)
        # yesButton = driver.find_element(By.XPATH, ".//*[text()='Да']/..")#.click()
        # time.sleep(2)
        # wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[text()='Да']/..")))
        # yesButton.click()
        # time.sleep(2)
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(3)
        driver.find_element_by_name('yt2').click()
        time.sleep(1)
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, "html/body/div[4]/div[3]/div/button[1]").click()






