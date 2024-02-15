from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import re

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

url1 = 'https://galaxystore.ru/about/contacts/'
url2 = "https://repetitors.info"
url3 = "https://hands.ru/company/about/"
urls = [url1, url2, url3]
for url in urls:
    driver.get(url)
    source = driver.page_source

    print("URL:", url)

    all_phones = []


    # Regex search - not ideal pattern
    phone_regex = r'\b8\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}\b'
    phone_match = re.findall(phone_regex, source)
    # print(phone_match)

    # XPath search
    phones = driver.find_elements("xpath", "//a [starts-with (@href, 'tel:')]")
    for phone in phones:
        print(phone.text)

    # Click search
    try:
        hidden_phones = driver.find_elements("xpath", "//* [contains (@class, 'phone') and contains (@class, 'link')]")
        for phone in hidden_phones:
            if phone not in phones and phone not in phone_match:
                match = re.match(phone_regex, phone)
                if (match):
                    all_phones.append(phone)
                    print(phone)
                else:
                    # click
        #print(hidden_phones.text)
    except:
        print("Hidden phones not found")