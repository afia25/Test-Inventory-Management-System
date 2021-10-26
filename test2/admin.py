from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
dr=webdriver.Chrome(executable_path="D:\\software pycharm projects\\web driver\\chromedriver.exe")

dr.get("http://localhost:8000/")
dr.maximize_window()
time.sleep(10)

dr.find_element(By.LINK_TEXT,"Sign up").click()
time.sleep(1)

dr.find_element_by_name("username").send_keys("Aria22")
time.sleep(1)
dr.find_element_by_name("password1").send_keys("uap123456")
time.sleep(1)
dr.find_element_by_name("password2").send_keys("uap123456")
time.sleep(1)
dr.find_element_by_name("first_name").send_keys("Aria")
time.sleep(1)
dr.find_element_by_name("last_name").send_keys("Aurora")
time.sleep(1)
dr.find_element_by_name("email").send_keys("aria12@gmail.com")
time.sleep(15)
dr.find_element(By.ID,"usertype").click()
time.sleep(3)
dr.find_element_by_name("usertype2").click()
time.sleep(1)
dr.find_element_by_name("button").send_keys(Keys.ENTER)
time.sleep(1)




dr.find_element(By.LINK_TEXT,"Admin").click()
time.sleep(6)
dr.find_element(By.PARTIAL_LINK_TEXT,"Add").click()
time.sleep(1)


dr.find_element(By.XPATH, "//input[@id='id_product_name']").send_keys("Hoody")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_category_name']").send_keys("Clothes")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_description']").send_keys("Long Sleeve Hoodies")
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, "input[id='id_buying_price']").send_keys("500")
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, "input[id='id_selling_price']").send_keys("600")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_purchase']").send_keys("20")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_sale']").send_keys("10")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@id='id_stock']").send_keys("10")
time.sleep(1)
dr.find_element_by_name("addbutton").send_keys(Keys.ENTER)
time.sleep(3)



dr.find_element(By.PARTIAL_LINK_TEXT,"Stock").click()
time.sleep(5)




from PIL import Image  ## pip install Pillow


dr.save_screenshot("stock_report.png")
time.sleep(1)

dr.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(6)


dr.close()
print("completed")


