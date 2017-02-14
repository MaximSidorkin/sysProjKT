# СОЗДАНИЕ РАБОЧЕГО ЗАДАНИЯ
import unittest
import time
global str
import HTMLTestRunner, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# global variable
driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/new/")
driver.maximize_window()
time.sleep(3)
wait = WebDriverWait(driver, 25)
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
        print('\n1. Логинимся в систему')

    def test002_Not500or404andLoginIsVisible(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print("2. Логин пользователя отобажен, страница загружена без ошибок")

    def test003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print("3. Переходим в раздел 'Все проекты'")

    def test004_Not500or404(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("4. Страница загружена без ошибок")

    def test005_OpenForm(self):
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
        time.sleep(3)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("5. По ключевому слову Selenium находим блок")

    def test006_FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования')
        findBlock.click()
        time.sleep(1)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("6. От блока переходим к проекту")

    def test007_FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(2)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("7. От проекта переходим к контрольным точкам")

    def test008_CreateWT(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_id('create-cp')
        CreateCP.click()
        time.sleep(5)
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print("8. Нажимаем кнопку Создать")

    def test009_BadFillingWTForm(self):
        driver.find_element_by_xpath("//div[@id='DIV_TYPE']/div/span/span/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[2]/ul/li[2]').click()
        time.sleep(1)
        # не заполняем ни одно из обязательных полей
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN+Keys.ENTER)
        time.sleep(6)
        try:
            driver.find_element_by_id('Checkpoint_TITLE_em_')
            driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_')
            driver.find_element_by_id('Checkpoint_DEADLINE_em_')
        except:
            self.fail(print('\n ПРЕДУПРЕЖДАЮЩИЕ УВЕДОМЛЕНИЯ О НЕЗАПОЛНЕННЫХ \n ОБЯЗАТЕЛЬНЫХ ПОЛЯХ НЕ ОТОБРАЖЕНЫ! \n'))
        time.sleep(2)
        # заполняем только одно из обязательных полей
        driver.find_element_by_id('Checkpoint_TITLE').send_keys('Уникальное название Рабочего задания')
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)
        time.sleep(6)
        try:
            driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_')
            driver.find_element_by_id('Checkpoint_DEADLINE_em_')
        except:
            self.fail(print('\n ПРЕДУПРЕЖДАЮЩИЕ УВЕДОМЛЕНИЯ О НЕЗАПОЛНЕННЫХ \n ОБЯЗАТЕЛЬНЫХ ПОЛЯХ НЕ ОТОБРАЖЕНЫ! \n!'))
        time.sleep(2)
        print("9. На форме создания контрольной точки проверяем, что в случае \nне заполнения обязательных полей выводятся соответствующие сообщения")

    def test010_GoodFillingWTForm(self):
        time.sleep(2)
        driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('DIT'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)
        print("10. Корректно заполняем все обязательные поля и сохраняем рабочую задачу")

    def test011_EditWT(self):
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        driver.find_element_by_name('yt0').click()
        time.sleep(3)
        driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Не выбрано'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id('Checkpoint_DEADLINE').clear()
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)
        time.sleep(5)
        try:
            driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_')
            driver.find_element_by_id('Checkpoint_DEADLINE_em_')
        except:
            print('\n ПРЕДУПРЕЖДАЮЩИЕ УВЕДОМЛЕНИЯ О НЕЗАПОЛНЕННЫХ \n ОБЯЗАТЕЛЬНЫХ ПОЛЯХ НЕ ОТОБРАЖЕНЫ! \n')
        print("11. Из открывшегося паспорта рабочего задания, переходим в редактирование, \nудаляем обязательные поля и пытаемся сохранить")

    def test012_FillingFormAgain(self):
        ASeleniumLogin_1.test010_GoodFillingWTForm(self)
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        print("12. После вывода сообщений о незаполненности обязательных полей,\n корректно заполняем форму и сохраняем рабочую задачу")

    def test013_SelectNewResponsible(self):
        time.sleep(5)
        driver.find_element_by_id('DIV_ID_RESPONSIBLE').click()
        time.sleep(1)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('ipad'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN + Keys.ENTER)
        print("13. Ещё раз переходим в форму редактирования, выбираем нового ответственного \n(ответственный = текущий пользователь) и сохраняем")

    def test014_SearchWTinDT(self):
        time.sleep(3)
        driver.find_element_by_link_text("Рабочий стол").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/li[2]/a/span[2]/span").click()
        time.sleep(1)
        try:
            driver.find_element_by_link_text('Уникальное название Рабочего задания')
            print('14. Переходим на рабочий стол и в последних созданных рабочих \nзадачах/контрольных точках \nпытаемся найти только что созданную нами')
        except:
            self.fail(print('\n 14. НЕ НАЙДЕНА РАБОЧАЯ ЗАДАЧА!\n'))
        time.sleep(1)

    def test015_GoToReport(self):
        time.sleep(3)
        report = driver.find_element_by_link_text("Отчёты")
        report.click()
        time.sleep(1)
        report1 = driver.find_element_by_link_text("Отчёт по контрольным точкам")
        report1.click()
        print("15. Переходим в раздел 'Отчёт по контрольным точкам' ")

    def test016_ReportFiltersSetting(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Уникальное название Рабочего задания')
        driver.find_element_by_id('search-text-push').click()
        print("16. В поиске вводим название созданного рабочего задания")

    def test017_SearchWTinReport(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.find-text')))
        try:
            driver.find_element_by_css_selector("span.find-text")
            print('17. Рабочая задача найдена')
        except:
            self.fail(print('\n 17. НЕ НАЙДЕНА РАБОЧАЯ ЗАДАЧА!\n'))

    def test018_NewUserLogin(self):
        time.sleep(1)
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'t')
        driver.get("https://dev.eor.gosapi.ru/")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()

        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("login")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("login")
        elem.send_keys(Keys.RETURN)
        print("18. Открываем новую вкладку и перелогиниваемся под другим пользоватлеме")

    def test019_NewUserSearchWT(self):
        # переходим в раздел "Отчёт по контрольным точкам"
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Отчёты')))
        driver.find_element_by_link_text("Отчёты").click()
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Отчёт по контрольным точкам')))
        driver.find_element_by_link_text("Отчёт по контрольным точкам").click()
        # настраиваем фильтры и ищем по поиску РЗ
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.title_executor')))
        driver.find_element_by_css_selector('span.title_executor').click()
        driver.find_element_by_id('btn_executor').click()
        time.sleep(1)
        driver.find_element_by_id('btn_executor').click()
        time.sleep(1)
        # поиск
        wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Уникальное название Рабочего задания')
        driver.find_element_by_id('search-text-push').click()
        print("19. Переходим в раздел 'Отчёт по контрольным точкам' и вводим в поиске \nназвание контрольной точки")

    def test020_isWTisEnabled(self):
        time.sleep(25)
        try:
            if driver.find_element_by_css_selector("span.find-text"):
                self.fail()
            else:
                print('else \n')
        except:
            print('20. Рабочая задача не найдена другим пользователем - всё Ок')

    def test021_GoodTone(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.caret')))
        driver.find_element_by_css_selector('span.caret').click()
        driver.find_element_by_link_text('Выход').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        driver.find_element_by_link_text("Отчёты").click()
        time.sleep(1)
        driver.find_element_by_link_text("Отчёт по контрольным точкам").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        driver.find_element_by_id('search-show').click()
        driver.find_element_by_id('search-text').send_keys('Уникальное название Рабочего задания')
        driver.find_element_by_id('search-text-push').click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.find-text')))
        driver.find_element_by_css_selector('span.find-text').click()
        wait.until(EC.element_to_be_clickable((By.NAME, 'yt2')))
        time.sleep(1)
        driver.find_element_by_name('yt2').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
        time.sleep(5)
        print('21. Логинимся за первого пользователя, в разделе\n "Отчёт по контрольным точкам" находим\n рабочее задание и удаляем его')
        driver.close()
        #
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CREATE_WORK_TASK.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ РАБОЧЕГО ЗАДАНИЯ + ПОИСК РАБОЧЕГО ЗАДАНИЯ ПОД ДРУГИМ ПОЛЬЗОВАТЕЛЕМ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)