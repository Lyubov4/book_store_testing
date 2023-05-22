# 1. Добавление комментария

# 1.Открываем practice.automationtesting.in:
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)


# 2. Проскроллим страницу на 600 пикселей вниз:
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

# 3. Нажмем на название книги "Selenium Ruby":
book=driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0>div>ul>li>a>img')
book.click()
time.sleep(3)

# 4. Нажмем на вкладку "REVIEWS":
reviews_btn=driver.find_element_by_css_selector(".reviews_tab>a")
reviews_btn.click()

# 5. Проскроллим страницу вниз, поставим 5 звёзд:
driver.execute_script("window.scrollBy(0, 500);")
star=driver.find_element_by_css_selector(".star-5")
star.click()

# 6. Заполним поле "Review" сообщением: "Nice book!":
review_txt=driver.find_element_by_id("comment")
review_txt.send_keys("Nice book!")
time.sleep(3)

#7. Заполним поле "Name":
name_fld=driver.find_element_by_id("author")
name_fld.send_keys("Lyubov")
time.sleep(3)

#8. Заполним поле "Email":
email_fld=driver.find_element_by_id("email")
email_fld.send_keys("Lyubov@mail.ru")
time.sleep(3)

# 9. Нажмем на кнопку "SUBMIT":
submit_btn=driver.find_element_by_css_selector(".form-submit>input")
submit_btn.click()
time.sleep(3)

driver.quit()


