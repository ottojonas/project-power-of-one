from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Navigate to Dynamics NAV login page
driver.get("https://your-dynamics-nav-url")

# Log in
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("your-username")
password.send_keys("your-password")
driver.find_element(By.ID, "submitButton").click()

# Wait for navigation to complete
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nav-bar")))

# Navigate to Sales Quote section
driver.find_element(By.LINK_TEXT, "Sales Quotes").click()

# Wait for Sales Quotes page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "new-quote-button"))
)

# Click on New Sales Quote
driver.find_element(By.ID, "new-quote-button").click()

# Wait for the new quote form to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "quote-form")))

# Fill in the Sales Quote form
# ! placeholder information and form - need to do more research into
# TODO research NAV field names and labels etc
customer_name = driver.find_element(By.ID, "customer-name")
quote_date = driver.find_element(By.ID, "quote-date")
item = driver.find_element(By.ID, "item")
quantity = driver.find_element(By.ID, "quantity")

customer_name.send_keys("Customer Name")
quote_date.send_keys("2023-10-01")
item.send_keys("Item Name")
quantity.send_keys("10")

# Submit the form
driver.find_element(By.ID, "submit-quote-button").click()

# Close the browser
driver.quit()
