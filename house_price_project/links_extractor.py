from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

path = r"C:\Users\ss\OneDrive\Рабочий стол\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

page = 1
links_count = 0
while links_count < 2_000:
        driver = webdriver.Chrome( options=options)
        stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

        print(f'current page {page}, links extracted{links_count}')
        url = f'https://nn.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&p={page}&region=4885'
        driver.get(url)
        articles = driver.find_elements(By.TAG_NAME, "article")
        with open('links.txt', 'a') as file:
                for a in articles:
                        link = a.find_element(By.TAG_NAME, "a").get_attribute("href")
                        print(link)
                        file.write(link)
                        file.write('\n')
                        links_count += 1
        page += 1
        time.sleep(1)
        driver.quit()
