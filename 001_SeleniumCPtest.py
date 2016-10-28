# СОЗДАНИЕ КОНТРОЛЬНОЙ ТОЧКИ ИЗ БЛОКА ПРОЕКТОВ
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
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(20)

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

        print('тест №1 - логинимся в систему')

    def test002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print('тест №2 - проверка на 404 и 500 ошибку после ввода логина/пароля')
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

        print('тест №3 - переход в раздел "Все проекты"')

    def test004_OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(3)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        time.sleep(3)
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(4)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print('тест №4 в фильтре вводим ключевое слово для поиска "Selenium"')

    def test005_FindBlock(self):
        # находим блок
        findBlock = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[1]/h4/strong/a')
        findBlock.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print('тест №5 переходим из Блоков в Проекты')

    def test006_CreateCP(self):
    #     создаём Кт из формы создания проекта
        btnCr = driver.find_element_by_id('create-cp').click()
        time.sleep(2)
        try:
            driver.find_element_by_class_name('input-group')
            driver.find_element_by_id('warn-project')
        except:
            print('test fall')
        scrollDown = driver.find_element_by_xpath('//div/span/i')
        time.sleep(1)
        scrollDown.click()
        scrollDown = driver.find_element_by_xpath('//div[2]/div/div/input')
        scrollDown.click()
        scrollDown.send_keys("Тестовый проект созданный Selenium")#+ Keys.ARROW_DOWN + Keys.ENTER)
        time.sleep(2)
        scrollDown = driver.find_element_by_css_selector('div.title-item > span.find-text').click()
        time.sleep(1)

        print('тест №6 в форме создания проета выбираем из выпадающего списка родителя для КТ')

    def test007_FillingCPForm(self):
        # заполняем форму КТ
        time.sleep(3)
        print('тест №7 форма приобрела вид КТ')
        #имя контрольной точки

    def test008_CPName(self):
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys('КТ номер 2')
        time.sleep(1)

        print('тест №8 вводим имя КТ')

    def test009_Comment(self):
        nameShort = driver.find_element_by_id('Checkpoint_plannedResult').send_keys('Комментарий')
        time.sleep(1)

        print('тест №9 вводим комментарий КТ')

    def test010_Autor(self):
        print('тест №10 вводим автора КТ')

    def test011_Responsible(self):
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('DIT' + Keys.ENTER)
        time.sleep(1)
        print('тест №11 вводим ответственного КТ')

    def test012_Executor(self):
        executorName = driver.find_element_by_id('DIV_ID_EXECUTOR').click()
        executorName = driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Б' + Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        print('тест №12 вводим исполнителя КТ')

    def test013_deadline(self):
        time.sleep(1)
        deadline = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        time.sleep(1)
        print('тест №13 вводим дедлайн КТ')

    def test014_source(self):
        source = driver.find_element_by_id('Checkpoint_SOURCE').send_keys('Источник')
        time.sleep(1)
        print('тест №14 вводим источник КТ')

    def test016_dateSource(self):
        dateSource = driver.find_element_by_id('Checkpoint_SOURCE_DATE').send_keys('12345' + Keys.ENTER)
        time.sleep(1)
        print('тест №15 вводим дату источника КТ')

    def test017_triggerKPI(self):
        #kpi = driver.find_element_by_css_selector('span.switch-right').click()
        time.sleep(1)
        print('тест №16 устанавливаем тиггер KPI КТ')

    def test018_triggerPrior(self):
        #prior = driver.find_element_by_xpath('//div[@id="DIV_IS_PRIORITY"]/div/div/div/span[2]').click()
        time.sleep(1)
        print('тест №17 устанавливаем триггер приоритет КТ')

    def test019_triggerDone(self):
        done = driver.find_element_by_xpath('//div[@id="DIV_IS_DONE"]/div/div/div/span[2]').click()
        time.sleep(2)
        print('тест №18 устанавливаем триггер выполнено КТ')

    def test020_triggerVisible(self):
        driver.find_element_by_xpath('//div[3]/div/div/div/span[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[4]/div/span/span/span/ul/li/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[4]/div/span/span/span/ul/li/input').send_keys(Keys.ENTER)
        print('тест №19 устанавливаем триггер видимости КТ')

    def test021_AllTriggersClose(self):
        time.sleep(1)
        visible = driver.find_element_by_xpath('//div[3]/div/div/div/label').click()

        print('тест №20 выключаем триггеры выполнено и видимость КТ')

    def test022_addAttach(self):
        time.sleep(2)
        print('тест №21 добавляем ссылку для КТ')

    def test023_confirmCreateCP(self):
        time.sleep(1)
        finishBtn = driver.find_element_by_name('yt0').click()
        assert "Error" not in driver.title

        print('тест №22 подтверждаем создание КТ')

    def test024_delCP(self):
        _ = wait.until(EC.element_to_be_clickable((By.NAME, 'yt2')))
        delete = driver.find_element_by_name('yt2').click()
        time.sleep(7)
        driver.implicitly_wait(10)
        delete = driver.find_element_by_xpath('//div[3]/div/button').click()
        time.sleep(1)

        print('тест №23 удаляем КТ')

    def test025_noErrorInTitlePage(self):
        time.sleep(1)
        assert "Error" not in driver.title
        print('тест №23 проверяем страницу на наличие ошибок 500/404')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("АТ для КТ из Блока Проектов.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ КОНТРОЛЬНОЙ ТОЧКИ ИЗ БЛОКА ПРОЕКТОВ',
        description='Отчет по тестированию'
    )
    runner.run(suite)

