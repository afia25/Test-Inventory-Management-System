from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
dr=webdriver.Chrome(executable_path="D:\\software pycharm projects\\web driver\\chromedriver.exe")

dr.get("http://localhost:8000/")
dr.maximize_window()
########

time.sleep(3)


dr.find_element(By.ID,"id_username").send_keys("Tithi25")
time.sleep(1)
dr.find_element(By.ID,"id_password").send_keys("uap123456")
time.sleep(1)
dr.find_element_by_name("loginbutton").send_keys(Keys.ENTER)
time.sleep(2)



dr.find_element(By.LINK_TEXT,"Employee").click()
time.sleep(20)

dr.find_element(By.LINK_TEXT,"Orders").click()
time.sleep(7)
dr.back()
time.sleep(4)



dr.find_element(By.PARTIAL_LINK_TEXT,"Create").click()
time.sleep(1)


dr.find_element(By.XPATH, "//input[@name='name_of_customer']").send_keys("Nova Tasnuba")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@name='customer_id']").send_keys("208")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@name='name_of_product']").send_keys("Flour")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_prod_id']").send_keys("7")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_quantity']").send_keys("3")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_total_price']").send_keys("180")
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, "input[name='delivery_charge']").send_keys("20")
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, "input[name='discount']").send_keys("0")
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, "input[name='total']").send_keys("200")
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, "input[id='id_payment']").send_keys("200")
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, "input[id='id_due']").send_keys("0")
time.sleep(1)

dr.find_element_by_name("invoice_button").send_keys(Keys.ENTER)
time.sleep(2)


dr.find_element(By.LINK_TEXT,"Profile").click()
time.sleep(4)
dr.find_element(By.LINK_TEXT,"All Invoices").click()
time.sleep(4)
dr.back()
time.sleep(3)

dr.find_element(By.PARTIAL_LINK_TEXT,"Sales").click()
time.sleep(8)

dr.find_element_by_name("pid").send_keys("7")
time.sleep(2)
dr.find_element(By.ID,"quan").send_keys("3")
time.sleep(2)
dr.find_element_by_name("sales_button").send_keys(Keys.ENTER)
time.sleep(6)
dr.find_element(By.LINK_TEXT,"Profile").click()
time.sleep(3)
dr.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(3)



dr.close()
print("completed")