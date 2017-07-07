# -*- coding: utf-8 -*-
# загрузка документов из http://nsi.asur.mos.ru/ по запросу шедулера
# задача https://redmine.msk.spcom.biz/issues/2298

import unittest, sys, time, requests, os, urllib.request, shutil, zipfile

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

global str

user = 'TUser'
password = 'doolin'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 960)
driver.implicitly_wait(20)

f = open(r'C:\asur_export_data\data2.txt')
line = f.readline()

class StartTask(unittest.TestCase):
    def test_001_GetUrl(url, dir_path=None):
        driver.get("http://nsi.asur.mos.ru/")
        driver.maximize_window()
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.textEntry')))
        driver.find_element_by_css_selector('input.textEntry').send_keys(user)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password + Keys.RETURN)
        # перешли на главную страницу, дождёмся активности окна ввода данных
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.SuggestComboBox-SuggestBox')))
        driver.find_element_by_css_selector('input.SuggestComboBox-SuggestBox').send_keys(line + Keys.RETURN)
        time.sleep(2)
        _ = wait.until(EC.invisibility_of_element_located((By.XPATH, ".//*[text()='Загрузка элементов каталога...']/.."))) # Загрузка элементов каталога...
        time.sleep(1)
        driver.find_element_by_css_selector('div.ExportMenuItem').click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//*[text()='Каталог']/..").click()
        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='XML']/..").click()
        #
        driver.find_element_by_css_selector('button.gwt-Button.processButton').click()
        print(' выбираем нужный реестр и выгружаем XML')
    def test_002_AlertAsert(self):
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.alert_is_present())
            alert = driver.switch_to.alert()
            assert "В настоящее время производится редактирование каталога. Попробуйте запустить экспорт позже." in alert.text
            alert.accept()
            print(' В настоящее время производится редактирование каталога. Попробуйте запустить экспорт позже. ')
            driver.close()
        except:
            print(' алерт не появился')
        #
    def test_003_DownloadXML(self):
        wait = WebDriverWait(driver, 960)
        try:
            time.sleep(2)
            driver.find_element_by_xpath(".//*[text()='Запустить новый экспорт']/..").click()
            print(' кнопка Запустить новый экспорт присутствует')
            time.sleep(10)
            _ = driver.find_element_by_xpath(
                '//tr[3]/td/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td[7]').text == 'Экспорт завершен Cкачать файл'  #exp2
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Cкачать файл')]")))
            t = driver.find_element_by_xpath("//a[contains(text(),'Cкачать файл')]").get_attribute('href')
            filereq = requests.get(t, stream=True)
            with open(r"C:\asur_export_data\\" + line + ".zip", "wb") as receive:
                shutil.copyfileobj(filereq.raw, receive)
            del filereq
        except:
            time.sleep(10)
            print(" кнопки нет, ждём выгрузку вручную")
            _ = driver.find_element_by_xpath(
                '//tr[3]/td/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td[7]').text == 'Экспорт завершен Cкачать файл'
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Cкачать файл')]")))
            t = driver.find_element_by_xpath("//a[contains(text(),'Cкачать файл')]").get_attribute('href')
            filereq = requests.get(t, stream=True)
            with open(r"C:\asur_export_data\\" + line + ".zip", "wb") as receive:
                shutil.copyfileobj(filereq.raw, receive)
            del filereq
        time.sleep(2)
        unicode_name = ''
        name = ''
        print(unicode_name,'\n',name)
        xml_zip = zipfile.ZipFile(r"C:\asur_export_data\\" + line + ".zip")
        for name in xml_zip.namelist():
            unicode_name = name.encode('cp437').decode('cp866')
            print(unicode_name)
        xml_zip.extract(name,r'C:\asur_export_data\\')
        xml_zip.close()
        os.chdir(r'C:\asur_export_data\\')
        try:
            os.path.exists(r'C:\asur_export_data\53012.xml')
            os.remove(r'C:\asur_export_data\53012.xml')
            print(' Удаляем старый файл')
        except:
            print(' старый файл не обнаружен')
        os.rename(name,'53012.xml')
        os.remove(r'C:\asur_export_data\\' + line + ".zip")

if __name__ == "__main__":
    unittest.main()