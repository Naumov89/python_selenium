
from selenium import webdriver
import time
import random
from fake_useragent import UserAgent # pip3 install fake_useragent

user_agents_list = [
        "hello-world",
        "python",
        "best_of_the_best"
        ]

useragent = UserAgent()

# options
my_options = webdriver.ChromeOptions()
# my_options.add_argument(f"user-agent={random.choice(user_agents_list)}")
my_options.add_argument(f"user-agent={useragent.random}")

link = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
driver = webdriver.Chrome(executable_path="/home/oleksandr/Desktop/python_work/chromedriver/chromedriver", options=my_options)

try:
    driver.get(url=link)
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
