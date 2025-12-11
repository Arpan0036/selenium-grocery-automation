import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj=Service(r"C:\Users\arpan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,'search-keyword').send_keys("Ber")
time.sleep(2)
addtocarts=driver.find_elements(By.XPATH,'//div[@class="product-action"]')
for button in addtocarts:
    button.click()


driver.find_element(By.CSS_SELECTOR,"a[class='cart-icon']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,'promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CLASS_NAME,'promoBtn').click()
wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'promoInfo')))
assert driver.find_element(By.CLASS_NAME,'promoInfo').is_displayed()

print(driver.find_element(By.CLASS_NAME,'promoInfo').text)

prices=driver.find_elements(By.XPATH,"//td[5]/p")
sum=0
for price in prices:
    sum=sum+float(price.text)
print(f"Your Total order price is {sum}rs")

assert sum==float(driver.find_element(By.CLASS_NAME,'totAmt').text)
assert sum>float(driver.find_element(By.CLASS_NAME,'discountAmt').text)

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
driver.find_element(By.XPATH,"//option[text()='India']").click()
driver.find_element(By.CLASS_NAME,"chkAgree").click()
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()


time.sleep(7)
