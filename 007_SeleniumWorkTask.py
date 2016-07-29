# СОЗДАНИЕ РАБОЧЕГО ЗАДАНИЯ
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
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        if __name__ == '__main__':
            unittest.main()

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
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test007_FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test008_CreateWT(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_id('create-cp')
        CreateCP.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test009_BadFillingWTForm(self):
        driver.find_element_by_xpath("//div[@id='DIV_TYPE']/div/span/span/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[2]/ul/li[2]').click()
        #driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Рабочая задача" + Keys.ENTER)
        time.sleep(1)
        # не заполняем ни одно из обязательных полей
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN+Keys.ENTER)
        time.sleep(6)
        try:
            driver.find_element_by_id('Checkpoint_TITLE_em_')
            driver.find_element_by_id('Checkpoint_ID_AUTHOR_MISSION_em_')
            driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_')
            driver.find_element_by_id('Checkpoint_DEADLINE_em_')
        except:
            print('Test 1 of warning messages is not successful!')
        time.sleep(2)
        # заполняем только одно из обязательных полей
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Уникальное название Рабочего задания')
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)
        time.sleep(6)
        try:
            driver.find_element_by_id('Checkpoint_ID_AUTHOR_MISSION_em_')
            driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_')
            driver.find_element_by_id('Checkpoint_DEADLINE_em_')
        except:
            print('Test 2 of warning messages is not successful!')
        time.sleep(2)
        # закомментрировано до решения бага 408
        #try:
        #    driver.find_element_by_xpath("//*[text()='контрольную точки']")
        #except:
        #    print('Test 3 of correct text is not successful!')

    def test010_GoodFillingWTForm(self):
        time.sleep(1)
        driver.find_element_by_id('DIV_AUTHOR_MISSION').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Багреева'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('DIT'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)

    def test011_EditWT(self):
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        time.sleep(2)
        driver.find_element_by_id('DIV_AUTHOR_MISSION').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Не выбрано'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Не выбрано'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id('Checkpoint_DEADLINE').clear()
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)
        time.sleep(5)
        try:
            driver.find_element_by_id('Checkpoint_TITLE_em_')
            driver.find_element_by_id('Checkpoint_ID_AUTHOR_MISSION_em_')
            driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_')
            driver.find_element_by_id('Checkpoint_DEADLINE_em_')
        except:
            print('Test 1 of warning messages is not successful!')

    def test012_FillingFormAgain(self):
        ASeleniumLogin_1.test010_GoodFillingWTForm(self)
        time.sleep(2)
        driver.find_element_by_name('yt0').click()

    def test013_SelectNewResponsible(self):
        time.sleep(5)
        #driver.find_element_by_name('yt0').click()
        driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('ipad'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)

    def test014_SearchWTinDT(self):
        time.sleep(3)
        driver.find_element_by_link_text("Рабочий стол").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/li[2]/a/span[2]/span").click()
        time.sleep(1)
        try:
            driver.find_element_by_link_text('Уникальное название Рабочего задания')
        except:
            print('Not found WT in DT!')
        time.sleep(1)

    def test015_GoToReport(self):
        time.sleep(3)
        report = driver.find_element_by_link_text("Отчёты")
        report.click()
        time.sleep(1)
        # Отчёт по контрольным точкам
        report1 = driver.find_element_by_link_text("Отчёт по контрольным точкам")
        report1.click()
        time.sleep(7)
        '''
    def test016_ReportFiltersSetting(self):
        driver.find_element_by_css_selector("span.title_executor").click()
        time.sleep(1)
        driver.find_element_by_id('btn_executor').click()
        time.sleep(1)
        driver.find_element_by_id('btn_executor').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/div[1]/div[2]/nav/div/div[2]/ul[5]/li/ul/li[1]/div/input').send_keys('ipad')
        time.sleep(1)
        driver.find_element_by_xpath('//li[3]/div/ul/li[3]/div/label').click()
        time.sleep(1)
        driver.find_element_by_id('btn_success_executor').click()
        time.sleep(3)
        driver.find_element_by_xpath('//ul[2]/li/a/span').click()
        driver.find_element_by_xpath('//li[5]/span').click()
        driver.find_element_by_xpath('//li[5]/span[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath("html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]").click()
        time.sleep(1)

    def test017_SearchWTinReport(self):
        try:
            driver.find_element_by_xpath("//div[@id='load_table']/div[4]/div[2]/div/h4/span")
        except:
            print('Not found WT in Report!')

    def test017_NewUserSeekWT(self):
        time.sleep(1)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'t')
        driver.get("https://dev.eor.gosapi.ru/site/login")
        '''