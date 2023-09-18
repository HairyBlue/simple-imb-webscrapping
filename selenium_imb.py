import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeServices
from selenium.webdriver.common.by import By
from selenium import webdriver

headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
noUI = "--headless"
url = "https://www.imdb.com/chart/top/"

try:
    service = ChromeServices(executable_path=ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument(noUI)
    option.add_argument(f"user-agent={headers}")

    driver = webdriver.Chrome(service=service, options=option)
    driver.get(url)

    lists = driver.find_element(By.XPATH, "//*[@id='__next']/main/div/div[3]/section/div/div[2]/div/ul")
    chilstlists = lists.find_elements(By.CSS_SELECTOR, "[class=ipc-title__text]")

    print("top 250 movies in IMB webites\n")

    for list in chilstlists:
        print(list.text)

except Exception as e:
    print(e)