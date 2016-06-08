# СОЗДАНИЕ КОНТРОЛЬНОЙ ТОЧКИ ИЗ БЛОКА ПРОЕКТОВ
import unittest
import time
global str

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

    def test003_OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    def test004_OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        #btn1 = driver.find_element_by_id("create-cp")
        #btn1.click()
        time.sleep(2)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        time.sleep(1)
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test005_FindBlock(self):
        # находим блок
        findBlock = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[1]/h4/strong/a')
        findBlock.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test006_CreateCP(self):
    #     создаём Кт из формы создания проекта
        btnCr = driver.find_element_by_id('create-cp').click()
        time.sleep(2)
        try:
            driver.find_element_by_class_name('input-group')
            driver.find_element_by_id('warn-project')
        except:
            print('test fall')
        scrollDown = driver.find_element_by_id('parent-text')
        time.sleep(1)
        #select = Select(scrollDown)
        #select.select_by_visible_text("Тестовый проект созданный Selenium")
        scrollDown.click()
        scrollDown = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/input')
        scrollDown.click()
        scrollDown.send_keys("Тестовый проект созданный Selenium")#+ Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(2)
        #scrollDown = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/ul/li[14]/i')   #span class
        #scrollDown.click()
        #time.sleep(1)
        scrollDown = driver.find_element_by_link_text('Тестовый проект созданный Selenium edit')
        scrollDown.click()
        time.sleep(1)

    def test007_FillingCPForm(self):
        # заполняем форму КТ
        time.sleep(3)
        #имя контрольной точки
    def test008_CPName(self):
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys('КТ номер 2')
    def test009_Comment(self):
        nameShort = driver.find_element_by_id('Checkpoint_PLANNED_RESULT').send_keys('Комментарий')
    def test010_Autor(self):
        autorName = driver.find_element_by_id('DIV_AUTHOR_MISSION').click()
        autorName = driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Б' + Keys.ENTER)
    def test011_Responsible(self):
        responsibleName = driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        responsibleName = driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Б' + Keys.ENTER)
    def test012_Executor(self):
        executorName = driver.find_element_by_id('DIV_ID_EXECUTOR').click()
        executorName = driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Б' + Keys.ENTER)
    def test013_deadline(self):
        deadline = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
    def test014_source(self):
        source = driver.find_element_by_id('Checkpoint_SOURCE').send_keys('Источник')
    def test015_scrollDown(self):
        editBtn = driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    def test016_dateSource(self):
        dateSource = driver.find_element_by_id('Checkpoint_SOURCE_DATE').send_keys('12345' + Keys.ENTER)
        time.sleep(1)
    def test017_triggerKPI(self):
        #kpi = driver.find_element_by_css_selector('span.switch-right').click()
        time.sleep(1)
    def test018_triggerPrior(self):
        prior = driver.find_element_by_xpath('//div[@id="DIV_IS_PRIORITY"]/div/div/div/span[2]').click()
        time.sleep(1)
    def test019_triggerDone(self):
        done = driver.find_element_by_xpath('//div[@id="DIV_IS_DONE"]/div/div/div/span[2]').click()
        time.sleep(1)
    def test020_triggerVisible(self):
        visible = driver.find_element_by_xpath('//div[3]/div/div/div/span[2]').click()
        time.sleep(2)
        users = driver.find_element_by_css_selector('ul.select2-selection__rendered')#.send_keys("Багреева" + Keys.ENTER)
        # users = driver.find_element_by_class_name('col-sm-5')
        users.click()
        users = driver.find_element_by_xpath('//div[1]/div[2]/div[4]/div/span/span[1]/span/ul/li/input').send_keys(Keys.ENTER)
        #users.send_keys("Багреева" + Keys.ENTER)
    def test021_AllTriggersClose(self):
        #kpi = driver.find_element_by_css_selector('span.switch-left').click()
        time.sleep(1)
        #prior = driver.find_element_by_xpath('//form/div/div[2]/div[18]/div/div/div/label').click()
        time.sleep(1)
        done = driver.find_element_by_xpath("//div[20]/div/div/div/label").click()
        time.sleep(1)
        visible = driver.find_element_by_xpath('//div[3]/div/div/div/label').click()
    def test022_addAttach(self):
        time.sleep(2)
        addlink = driver.find_element_by_xpath('//div[@id="DIV_FILES"]/div/div/div[2]/ul/li[2]/a/span').click()
        time.sleep(2)
        textLink = driver.find_element_by_xpath('//div[2]/div[2]/input').send_keys('Yandex')
        link = driver.find_element_by_xpath('//div[2]/div[2]/input[2]').send_keys('ya.ru')
        uploadLink = driver.find_element_by_xpath('//span[3]/span').click()
    def test023_confirmCreateCP(self):
        time.sleep(1)
        finishBtn = driver.find_element_by_name('yt0').click()
        assert "Error" not in driver.title
        #linkCheck = driver.find_element_by_xpath('//a[contains(text(),"Yandex")]').click()
    def test024_delCP(self):
        _ = wait.until(EC.element_to_be_clickable((By.NAME, 'yt2')))
        delete = driver.find_element_by_name('yt2').click()
        time.sleep(2)
        driver.implicitly_wait(10)
        #_ = wait.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[3]/div[3]/div/button[1]')))
        delete = driver.find_element_by_xpath('//div[3]/div/button')
        delete.click()
        time.sleep(2)
    def test025_noErrorInTitlePage(self):
        time.sleep(2)
        assert "Error" not in driver.title
        print(' finish!')

if __name__ == '__main__':
    unittest.main()

