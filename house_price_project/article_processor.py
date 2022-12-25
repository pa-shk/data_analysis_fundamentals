from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import csv
import  time
from multiprocessing import Process


path = r"C:\Users\ss\OneDrive\Рабочий стол\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


with open('skipped.txt') as s_file:
        skipped = s_file.read()


with open('unique_links.txt') as file:
        for count, url in enumerate(file):
                if url not in skipped:
                        url = url.strip()
                        print(count, url)
                        try:
                                driver = webdriver.Chrome(options=options)
                                stealth(
                                        driver,
                                        languages=["en-US", "en"],
                                        vendor="Google Inc.",
                                        platform="Win32",
                                        webgl_vendor="Intel Inc.",
                                        renderer="Intel Iris OpenGL Engine",
                                        fix_hairline=True,
                                )
                                driver.get(url)

                                price = driver.find_element("xpath", "//div[@data-name='OfferCardAside']")
                                title = driver.find_element("xpath", "//div[@data-name='OfferTitle']")
                                location = driver.find_element("xpath", "//div[@data-name='Geo']")
                                summary = driver.find_element("xpath", "//div[@data-name='ObjectSummaryDescription']")
                                additional =  driver.find_element("xpath", "//section[@data-name='AdditionalFeatures']")
                                house = driver.find_element("xpath", "//div[@data-name='BtiHouseData']")

                                with open('output.tsv', 'a', encoding='utf-8') as out_file:
                                        tsv_writer = csv.writer(out_file, delimiter='\t')
                                        tsv_writer.writerow([url, price.text.strip(), title.text.strip(), location.text.strip(),
                                                             summary.text.strip(), additional.text.strip(), house.text.strip()])
                                time.sleep(10)
                                driver.quit()
                                with open('processed.txt', 'a') as file:
                                        file.write(url)
                                        file.write('\n')
                        except Exception:
                                time.sleep(10)
                                with open('skipped.txt', 'a') as file:
                                        file.write(f'{count} {url}')
                                        file.write('\n')
                        finally:
                                driver.quit()
