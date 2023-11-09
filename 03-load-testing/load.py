import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

service = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

header_locator = "body > nav > div > div > a"
locators = {
    "v1": "body > div.container-fluid > div:nth-child(2) > div:nth-child(2) > blockquote:nth-child(3) > small:last-child",
    "v2": "body > div.container-fluid > div:nth-child(2) > div:nth-child(2) > blockquote:nth-child(3) > font[color=black] > span:nth-child(1)",
    "v3": "body > div.container-fluid > div:nth-child(2) > div:nth-child(2) > blockquote:nth-child(3) > font[color=red] > span:nth-child(1)",
}
stats = {
    "v1": 0,
    "v2": 0,
    "v3": 0,
    "fails": 0,
}

driver.get("https://94f2-20-123-184-30.ngrok-free.app/productpage?u=test#")
for i in range(1000000):
    driver.refresh()
    try:
        el = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, header_locator))
        )
    except TimeoutException:
        print("Loading took too much time!")
        stats["fails"] += 1

    for version, locator in locators.items():
        try:
            el = driver.find_element(By.CSS_SELECTOR, locator)
            stats[version] += 1
        except NoSuchElementException:
            continue
    if i % 10 == 0:
        print(f"stats {stats}")
driver.quit()
