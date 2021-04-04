from selenium import webdriver
import time

my_url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="/home/oleksandr/Desktop/python_work/chromedriver/chromedriver")

try:
    driver.get(url=my_url)
    time.sleep(5)
    driver.get_screenshot_as_file('1.png')
    driver.get(url="https://www.rezka.ag")
    time.sleep(7)
    driver.save_screenshot('2.png')
    # driver.refresh()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

