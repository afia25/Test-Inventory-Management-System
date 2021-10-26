from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
dr=webdriver.Chrome(executable_path="D:\\software pycharm projects\\web driver\\chromedriver.exe")

dr.get("http://localhost:8000/")
dr.maximize_window()
time.sleep(2)


dr.find_element(By.ID,"id_username").send_keys("Nova")
time.sleep(1)
dr.find_element(By.ID,"id_password").send_keys("uap123456")
time.sleep(1)
dr.find_element_by_name("loginbutton").send_keys(Keys.ENTER)
time.sleep(5)

dr.find_element(By.LINK_TEXT,"Customer").click()
time.sleep(15)
dr.find_element_by_name("cat").send_keys(Keys.ENTER)
time.sleep(4)

dr.find_element(By.XPATH,"//a[contains(text(),'Food')]").click()
time.sleep(7)


dr.find_element_by_name("product_id").send_keys("7")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@name='user_id']").send_keys("208")
time.sleep(1)
dr.find_element(By.XPATH, "//input[@name='quantity']").send_keys("3")
time.sleep(1)
dr.find_element_by_name("foodbutton").send_keys(Keys.ENTER)
time.sleep(2)
dr.find_element_by_name("cartbutton").send_keys(Keys.ENTER)
time.sleep(5)
dr.find_element_by_name("buybutton").send_keys(Keys.ENTER)
time.sleep(7)
#dr.find_element_by_name("user_details_button").send_keys(Keys.ENTER)
#time.sleep(2)
dr.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(8)


dr.close()
print("completed")
