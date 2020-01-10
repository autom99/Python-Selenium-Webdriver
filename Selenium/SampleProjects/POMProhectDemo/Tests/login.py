from selenium import webdriver

import time
import urllib

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options,executable_path='D:/Testing Purpose/Pycharm Testing/Selenium/Driver/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

try:
    driver.get('https://opensource-demo.orangehrmlive.com/')

    time.sleep(5)
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    time.sleep(2)
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    time.sleep(3)
    driver.find_element_by_id('btnLogin').click()
    time.sleep(3)
    print("Test Completed successfully..!!")

except urllib.error.URLError as Error:
    print(Error)

finally:
    driver.close()
    driver.quit()