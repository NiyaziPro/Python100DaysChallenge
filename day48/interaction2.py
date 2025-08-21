from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(By.NAME, value="fName")
first_name_field.send_keys("Niko", Keys.TAB, "Dev", Keys.TAB, "nikodev@dev.io", Keys.TAB, Keys.ENTER)

success_text = driver.find_element(By.CLASS_NAME,value="lead")
print(success_text.text)
success_text.is_displayed()

driver.quit()