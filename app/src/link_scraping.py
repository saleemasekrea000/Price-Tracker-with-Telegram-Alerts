from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from celery.schedules import crontab

from src.celery_app import app



@app.task
def scrape_product_price(product_link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without opening the browser window

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    try:
        driver.get(product_link)

        price_element = driver.find_element(By.CLASS_NAME, "price--currentPriceText--V8_y_b5")
        price = price_element.text.strip()

        return price

    except Exception as e:
        return f"Error fetching price: {str(e)}"

    finally:
        driver.quit()

app.conf.beat_schedule = {
    'scrape-product-price-every-hour': {
        'task': 'scrape_product_price',
        'schedule': crontab(minute=0, hour='*'),  # Runs every hour at minute 0
        # TODO change this link .
        'args': ('https://www.aliexpress.com/item/1005005470194484.html',),
    },
}

# product_price = get_product_price("https://www.aliexpress.com/item/1005005470194484.html")
# print(f"Product Price: {product_price}")
