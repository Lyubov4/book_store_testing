# 1. Регистрация аккаунта

# 1. Открываем practice.automationtesting.in:
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)

# 2. Нажимаем на вкладку "My Account Menu":
my_acc=driver.find_element_by_link_text('My Account')
my_acc.click()
time.sleep(3)

#3. В разделе "Register", вводим email для регистрации:
email=driver.find_elements_by_id('reg_email')
email[0].click()
email[0].send_keys("Danishek@internet.ru")
time.sleep(3)

#4. В разделе "Register", введим пароль для регистрации:
pass_fld=driver.find_elements_by_id("reg_password")
pass_fld[0].click()
pass_fld[0].send_keys("f@45LJG&f71k")
time.sleep(3)

# 5. Нажмем на кнопку "Register":
reg_btn=driver.find_element_by_css_selector('[name="register"]')
reg_btn.click()
time.sleep(3)

driver.quit()

# 2. Логин в систему

# 1. Открываем practice.automationtesting.in:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)

# 2. Нажимаем на вкладку "My Account Menu":
my_acc=driver.find_element_by_link_text('My Account')
my_acc.click()
time.sleep(3)

# 3. В разделе "Login", вводим email для логина:
username_fld=driver.find_elements_by_id('username')
username_fld[0].click()
username_fld[0].send_keys("Danishek@internet.ru")
time.sleep(3)

#4. В разделе "Login", вводим пароль для логина:
pass_fld=driver.find_elements_by_id("password")
pass_fld[0].click()
pass_fld[0].send_keys("f@45LJG&f71k")
time.sleep(3)

# 5. Нажимаем на кнопку "Login":
lgn_btn=driver.find_element_by_css_selector('[name="login"]')
lgn_btn.click()
time.sleep(3)

# 6. Добавляем проверку, что на странице есть элемент "Logout":
logout_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.LINK_TEXT, 'Logout'), "Logout"))

driver.quit()
