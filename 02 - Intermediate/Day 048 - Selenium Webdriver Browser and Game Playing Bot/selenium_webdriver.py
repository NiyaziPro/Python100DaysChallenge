from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# url = "https://www.amazon.de/Apple-MacBook-Laptop-12-Core-16-Core/dp/B0DLJFC4X3/ref=pd_ci_mcx_mh_mcx_views_1_image?pd_rd_w=upfcT&content-id=amzn1.sym.912f42bf-a738-49a7-a7e9-360c5ecbe036%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=912f42bf-a738-49a7-a7e9-360c5ecbe036&pf_rd_r=KGTTZWD6FXFNYZ2X7N55&pd_rd_wg=kFOaA&pd_rd_r=c5ea734c-0055-4937-b601-ccfb1067d150&pd_rd_i=B0DLJFC4X3&th=1"
url = "https://www.python.org"
driver.maximize_window()
driver.get(url)

# driver.implicitly_wait(30)
# driver.find_element(By.ID,value="sp-cc-rejectall-link").click()
#
# price_euro = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# currency = driver.find_element(By.CLASS_NAME,value="a-price-symbol")
#
# print(f"The price is {price_euro.text}.{price_cents.text}{currency.text}")

# search_box = driver.find_element(By.NAME,value="q")
# search_box.send_keys("selenium")
# driver.find_element(By.ID,value="submit").click()

event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

# driver.close()
driver.quit()
