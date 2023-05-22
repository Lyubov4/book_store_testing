#1. Отображение страницы товара:

#1. Открываем practice.automationtesting.in:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)

# 2. Залогинимся:
my_acc=driver.find_element_by_link_text('My Account')
my_acc.click()
time.sleep(3)

username_fld=driver.find_elements_by_id('username')
username_fld[0].click()
username_fld[0].send_keys("Danishek@internet.ru")
time.sleep(3)

pass_fld=driver.find_elements_by_id("password")
pass_fld[0].click()
pass_fld[0].send_keys("f@45LJG&f71k")
time.sleep(3)

lgn_btn=driver.find_element_by_css_selector('[name="login"]')
lgn_btn.click()
time.sleep(3)

# 3. Нажмем на вкладку "Shop":
shop_btn=driver.find_element_by_css_selector('[id="menu-item-40"]>a')
shop_btn.click()
time.sleep(3)

# 4. Проскроллим страницу вниз, откроем книгу "HTML 5 Forms":
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

book=driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
book.click()

# 5. Добавим тест, что заголовок книги назвается: "HTML5 Forms":
title_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[itemprop="name"]'),"HTML5 Forms"))
time.sleep(2)

driver.quit()

# 2. Количество товаров в категории

# 1. Открываем practice.automationtesting.in:
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)

# 2. Залогинимся:
my_acc=driver.find_element_by_link_text('My Account')
my_acc.click()
time.sleep(3)

username_fld=driver.find_elements_by_id('username')
username_fld[0].click()
username_fld[0].send_keys("Danishek@internet.ru")
time.sleep(3)

pass_fld=driver.find_elements_by_id("password")
pass_fld[0].click()
pass_fld[0].send_keys("f@45LJG&f71k")
time.sleep(3)

lgn_btn=driver.find_element_by_css_selector('[name="login"]')
lgn_btn.click()
time.sleep(3)

# 3. Нажмем на вкладку "Shop":
shop_btn=driver.find_element_by_css_selector('[id="menu-item-40"]>a')
shop_btn.click()
time.sleep(3)

# 4. Откроем категорию "HTML":
html=driver.find_element_by_link_text("HTML")
html.click()
time.sleep(2)

# 5. Добавим тест, что отображается три товара:
items_count = driver.find_elements_by_class_name("product")
if len(items_count) == 3:
     print("На странице 3 товара")
else:
     print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
time.sleep(2)

driver.quit()

# 3. Cортировка товаров

# 1. Открываем practice.automationtesting.in:
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)

# 2. Залогинимся:
my_acc=driver.find_element_by_link_text('My Account')
my_acc.click()
time.sleep(3)

username_fld=driver.find_elements_by_id('username')
username_fld[0].click()
username_fld[0].send_keys("Danishek@internet.ru")
time.sleep(3)

pass_fld=driver.find_elements_by_id("password")
pass_fld[0].click()
pass_fld[0].send_keys("f@45LJG&f71k")
time.sleep(3)

lgn_btn=driver.find_element_by_css_selector('[name="login"]')
lgn_btn.click()
time.sleep(3)

# 3. Нажмем на вкладку "Shop":
shop_btn=driver.find_element_by_css_selector('[id="menu-item-40"]>a')
shop_btn.click()
time.sleep(3)

# 4. Добавим тест, что в селекторе выбран вариант сортировки по умолчанию:
sorting_selector=driver.find_element_by_class_name("orderby").click()
default_sorting=driver.find_element_by_css_selector('[value="menu_order"]')
sorting_selected=default_sorting.get_attribute('selected')

if sorting_selected is not None:
    print ("status default")
else:
    print("status is not default")
time.sleep(2)

# 5. Отсортируем товары по цене от большей к меньшей:
sorting_selector=Select(driver.find_element_by_class_name("orderby"))
sorting_selector.select_by_value("price-desc")
time.sleep(2)

# 6. Снова объявим переменную с локатором основного селектора сортировки:
sorting_field=driver.find_element_by_class_name("orderby").click()

# 7. Добавим тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей:
sorting_high=driver.find_element_by_css_selector('[value="price-desc"]')
sort_select=sorting_high.text
assert sort_select=="Sort by price: high to low"
time.sleep(2)
driver.quit()


# 4. Oтображение, скидка товара:

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

# 2. Залогинимся:
my_acc=driver.find_element_by_link_text('My Account')
my_acc.click()
time.sleep(2)

username_fld=driver.find_elements_by_id('username')
username_fld[0].click()
username_fld[0].send_keys("Danishek@internet.ru")
time.sleep(2)

pass_fld=driver.find_elements_by_id("password")
pass_fld[0].click()
pass_fld[0].send_keys("f@45LJG&f71k")
time.sleep(2)

lgn_btn=driver.find_element_by_css_selector('[name="login"]')
lgn_btn.click()
time.sleep(2)

# 3. Нажмем на вкладку "Shop":
shop=driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(2)

# 4. Откроем книгу "Android Quick Start Guide":
book=driver.find_element_by_css_selector("[alt='Android Quick Start Guide']").click()
time.sleep(2)

# 5. Добавим тест, что содержимое старой цены = "₹600.00":
last_price=driver.find_element_by_css_selector('[itemprop="offers"]>p>del>span')
last_price_get_text=last_price.text
assert last_price_get_text=="₹600.00"

# 6. Добавим тест, что содержимое новой цены = "₹450.00":
new_price=driver.find_element_by_css_selector('[itemprop="offers"]>p>ins>span')
new_price_get_text=new_price.text
assert new_price_get_text=="₹450.00"

# 7. Добавим явное ожидание и нажмем на обложку книги:
pp_pic = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="attachment-shop_single size-shop_single wp-post-image"]')) )
pp_pic.click()

# 8. Добавим явное ожидание и закроем предпросмотр нажав на крестик:
close_btn=WebDriverWait(driver, 30).until(
EC.element_to_be_clickable((By.CSS_SELECTOR,'.pp_details>a')) )
close_btn.click()

driver.quit()

# 5. Проверка цены в корзине

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

# 2. Нажмем на вкладку "Shop":
shop=driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(2)

# 3. Добавим в корзину книгу:
book=driver.find_element_by_css_selector('[class="products masonry-done"]>li:nth-child(6)').click()
time.sleep(2)
book_by=driver.find_element_by_css_selector('[class="single_add_to_cart_button button alt"]').click()
time.sleep(2)

# 4. Добавим тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹350.00":
item=driver.find_element_by_class_name('cartcontents')
item_get_text=item.text
assert item_get_text=="1 Item"

price=driver.find_element_by_css_selector('#wpmenucartli>a>.amount')
price_get_text=price.text
assert price_get_text=="₹350.00"

# 5. Перейдем в корзину:
cart=driver.find_element_by_id("wpmenucartli").click()

# 6. Используя явное ожидание, проверяем, что в Subtotal отобразилась стоимость:
subtotal = WebDriverWait(driver, 20).until(
EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-title='Subtotal']>span")))

# 7. Используя явное ожидание, проверяем, что в Total отобразилась стоимость:
total=WebDriverWait(driver, 20).until(
EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-title='Total']>strong>span")))

driver.quit()

# 6. Работа в корзине:

# 1. :
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)

# 2 Открываем Shop:
shop=driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(2)

# 3: так как все книги out of stock, добавляем единственную доступную:

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)

book=driver.find_element_by_css_selector('[class="products masonry-done"]>li:nth-child(6)').click()
time.sleep(2)
book_by=driver.find_element_by_css_selector('[class="single_add_to_cart_button button alt"]').click()
time.sleep(2)

# 4 Переходим в корзину:
cart=driver.find_element_by_id("wpmenucartli").click()

# 5 Удаляем книгу:
time.sleep(2)
book_del=driver.find_element_by_class_name("remove").click()

# 6 Отменяем удаление:
time.sleep(2)
undo=driver.find_element_by_css_selector(".woocommerce-message>a").click()

# 7 Увеличиваем количество товара до трех:
quant_fld=driver.find_element_by_css_selector(".quantity>input").clear()
time.sleep(2)
quant_fld_2=driver.find_element_by_css_selector(".quantity>input")
quant_fld_2.send_keys("3")

# 8 Обновляем корзину:
update_bsk=driver.find_element_by_css_selector("[name=update_cart]").click()

# 9 Проверяем, что value=3:
element = driver.find_element_by_css_selector("[inputmode=numeric]")
element_check = element.get_attribute("value")
assert element_check == "3"

# 10 Нажимаем на кнопку Apply coupon:
time.sleep(2)
apply_btn=driver.find_element_by_css_selector("[name=apply_coupon]").click()

# 11 Проверяем, что возникло сообщение "Please enter a coupon code.":
time.sleep(2)
element=driver.find_element_by_css_selector('.woocommerce-error')
element_get_text = element.text
assert element_get_text == "Please enter a coupon code."

driver.quit()

# 7. Покупка товара:

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

shop=driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(2)

# 2. Открываем Shop:
shop=driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(2)

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)

# 3. Добавляем в корзину книгу:
book=driver.find_element_by_css_selector('[class="products masonry-done"]>li:nth-child(6)').click()
time.sleep(2)
book_by=driver.find_element_by_css_selector('[class="single_add_to_cart_button button alt"]').click()
time.sleep(2)

# 4. Переходим в корзину:
cart=driver.find_element_by_id("wpmenucartli").click()

# 5. Нажимаем "PROCEED TO CHECKOUT":
time.sleep(2)
check_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="checkout-button button alt wc-forward"]')) ).click()

# 6. Заполняем все обязательные поля:
first_name = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")) )
first_name.send_keys("Luybov")
time.sleep(3)

last_name=driver.find_elements_by_id('billing_last_name')
last_name[0].send_keys("Danishek")
time.sleep(3)

mail_field=driver.find_element_by_id("billing_email")
mail_field.send_keys("Danishek@mail.ru")
time.sleep(3)

phone_field=driver.find_element_by_id("billing_phone")
phone_field.send_keys("+786435461")
time.sleep(3)

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)

country=driver.find_element_by_id("s2id_billing_country").click()
country_fld=driver.find_element_by_css_selector("#select2-drop>div>input")
country_fld.send_keys("Congo (Kinshasa)")
time.sleep(3)
country_opt=driver.find_element_by_css_selector("[class='select2-results-dept-0 select2-result select2-result-selectable select2-highlighted']").click()
time.sleep(3)

addres_fld=driver.find_element_by_id("billing_address_1")
addres_fld.send_keys("Avenue Kianza")
time.sleep(3)

town=driver.find_element_by_id("billing_city")
town.send_keys("Kinshasa")
time.sleep(3)

state=driver.find_element_by_id("billing_state")
state.send_keys ("Central")
time.sleep(3)

zip=driver.find_element_by_id("billing_postcode")
zip.send_keys("885656425")
time.sleep(3)

# 7. Выбираем способ оплаты "Check Payments":
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)

payments_checkbox=driver.find_element_by_id("payment_method_cheque").click()
time.sleep(2)

# 8. Нажимаем "PLACE ORDER":
place_order_btn=driver.find_element_by_id("place_order").click()
time.sleep(2)

# 9. Проверяем, что отображается надпись "Thank you. Your order has been received.":
inf_win = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'),"Thank you. Your order has been received."))

# 10. Проверяем, что в Payment Method отображается текст "Check Payments":
pay_meth_wind = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tfoot>tr:nth-child(3)'),"Check Payments"))

driver.quit()

















