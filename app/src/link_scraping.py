from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without opening the browser window

# Initialize the WebDriver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the desired product page
#TODO get the link  from the user
driver.get('https://www.aliexpress.com/item/1005005470194484.html')

# Find the price element and extract the price text
price_element = driver.find_element(By.CLASS_NAME, 'price--currentPriceText--V8_y_b5')
price = price_element.text.strip()

print(f"Product Price: {price}")

# Close the driver
driver.quit()
