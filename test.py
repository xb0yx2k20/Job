from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import re

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

url1 = 'https://galaxystore.ru/about/contacts/'
url2 = "https://repetitors.info"
driver.get(url1)

source = driver.page_source

# Regex search - not ideal pattern
phone_pattern = r'\b8\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}\b'
phone_match = re.findall(phone_pattern, source)
# print(phone_match)

# XPath search
phones = driver.find_elements("xpath", "//a [starts-with (@href, 'tel:')]")
for phone in phones:
    print(phone.text)

# Click search
