# Shop: отображение страницы товара
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# My_Account = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# My_Account.click()
# Email_address = driver.find_element_by_id("username")
# Email_address.send_keys("1234email@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("P9anbv3T!s5")
# Login = driver.find_element_by_css_selector("[name='login']")
# Login.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# HTML5_Forms = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
# HTML5_Forms.click()
# element = driver.find_element_by_css_selector(".product_title.entry-title")
# element_get_text = element.text
# assert element_get_text == "HTML5 Forms"



# Shop: количество товаров в категории
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# My_Account = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# My_Account.click()
# Email_address = driver.find_element_by_id("username")
# Email_address.send_keys("1234email@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("P9anbv3T!s5")
# Login = driver.find_element_by_css_selector("[name='login']")
# Login.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# HTML = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product-category/html/']")
# HTML.click()
# items_count = driver.find_elements_by_tag_name("h3")
# if len(items_count) == 3:
#     print("В корзине 3 товара")
# else:
#     print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))



# Shop: сортировка товаров
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# My_Account = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# My_Account.click()
# Email_address = driver.find_element_by_id("username")
# Email_address.send_keys("1234email@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("P9anbv3T!s5")
# Login = driver.find_element_by_css_selector("[name='login']")
# Login.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# selected = driver.find_element_by_css_selector("[value='menu_order']")
# selected_checked = selected.get_attribute("selected")
# print("value of selected: ", selected_checked)
# if selected_checked is not None:
#     print("Выбран вариант сортировки по умолчанию")
# else:
#     print("Не выбран вариант сортировки по умолчанию")
# selector_option = driver.find_element_by_class_name("orderby")
# select = Select(selector_option)
# select.select_by_value("price-desc")
# selected = driver.find_element_by_class_name("orderby")
# selected_check = selected.get_attribute("value")
# if selected_check == "price-desc":
#     print("Выбран вариант сортировки по цене от большей к меньшей")
# else:
#     print("Не выбран вариант сортировки по цене от большей к меньшей")



# Shop: отображение, скидка товара
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# My_Account = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# My_Account.click()
# Email_address = driver.find_element_by_id("username")
# Email_address.send_keys("1234email@mail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("P9anbv3T!s5")
# Login = driver.find_element_by_css_selector("[name='login']")
# Login.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# Android_Quick_Start_Guide = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
# Android_Quick_Start_Guide.click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()



# Shop: проверка цены в корзине
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# Add_to_basket = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
# Add_to_basket.click()
# item = driver.find_element_by_css_selector("a > .cartcontents")
# item_text = item.text
# price = driver.find_element_by_css_selector("a > .amount")
# price_text = price.text
# assert item_text == "1 item"
# assert price_text == "₹180.00"
# time.sleep(3)
# basket = driver.find_element_by_id("wpmenucartli")
# basket.click()
# Subtotal = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] > .woocommerce-Price-amount"), "180.00"))
# Total = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "183.60"))



# Shop: работа в корзине
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# HTML5_WebApp_Development = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
# HTML5_WebApp_Development.click()
# time.sleep(3)
# JS_Data_Structures_and_Algorithm = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']")
# JS_Data_Structures_and_Algorithm.click()
# basket = driver.find_element_by_id("wpmenucartli")
# basket.click()
# time.sleep(3)
# Delete_first_book = driver.find_element_by_css_selector("[data-product_id='182']")
# Delete_first_book.click()
# time.sleep(3)
# Undo = driver.find_element_by_css_selector(".woocommerce-message :nth-child(1)")
# Undo.click()
# Clear_field = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# Clear_field.clear()
# Quantity = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# Quantity.send_keys("3")
# Update_basket = driver.find_element_by_name("update_cart")
# Update_basket.click()
# element = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# element_check = element.get_attribute("value")
# assert element_check == "3"
# time.sleep(3)
# APPLY_COUPON = driver.find_element_by_css_selector("[name='apply_coupon']")
# APPLY_COUPON.click()
# time.sleep(3)
# Please_enter = driver.find_element_by_css_selector(".woocommerce-error :nth-child(1)")
# Please_enter_text = Please_enter.text
# assert Please_enter_text == "Please enter a coupon code."



# Shop: покупка товара
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# Add_to_basket = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
# Add_to_basket.click()
# time.sleep(3)
# basket = driver.find_element_by_id("wpmenucartli")
# basket.click()
# Proceed_to_checkout = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
# Proceed_to_checkout.click()
# First_Name = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.ID, "billing_first_name")))
# First_Name.send_keys("Virat")
# Last_Name = driver.find_element_by_id("billing_last_name")
# Last_Name.send_keys("Roshan")
# Email = driver.find_element_by_id("billing_email")
# Email.send_keys("1111@mail.ru")
# Phone = driver.find_element_by_id("billing_phone")
# Phone.send_keys("1234567890")
# Address = driver.find_element_by_css_selector("#billing_address_1.input-text")
# Address.send_keys("Nagapura")
# Town = driver.find_element_by_css_selector("#billing_city.input-text")
# Town.send_keys("Guntur")
# Postcode = driver.find_element_by_css_selector("#billing_postcode.input-text")
# Postcode.send_keys("12345")
# country = driver.find_element_by_id("s2id_billing_state")
# country.click()
# country_select = driver.find_element_by_id("s2id_autogen2_search")
# country_select.send_keys("Andhra Pradesh")
# country_select_Andhra_Pradesh = driver.find_element_by_id("select2-results-2")
# country_select_Andhra_Pradesh.click()
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# Check_Payments = driver.find_element_by_id("payment_method_cheque")
# Check_Payments.click()
# place_order = driver.find_element_by_id("place_order")
# place_order.click()
# time.sleep(3)
# Thank_you = driver.find_element_by_css_selector(".woocommerce-thankyou-order-received")
# Thank_you_text = Thank_you.text
# assert Thank_you_text == "Thank you. Your order has been received."
# time.sleep(3)
# Check_Payments_Here = driver.find_element_by_css_selector("tr:nth-child(3) td")
# Check_Payments_Here_text = Check_Payments_Here.text
# assert Check_Payments_Here_text == "Check Payments"


















