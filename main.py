from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import re

all_phones = []
phone_regex = r'\b8\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}\b'



# Regex search - not ideal
def regex_search():
    global all_phones, phone_regex
    phone_match = re.findall(phone_regex, source)
    all_phones = phone_match.copy()
    # print(phone_match, 'mm')


 # XPath search
def xpath_search():
    global all_phones
    phones = driver.find_elements("xpath", "//a [starts-with (@href, 'tel:')]")
    for phone in phones:
        print(phone.href, 'xxx')

        all_phones.append(phone.text)


    # Click search
def click_search():
    global all_phones
    hidden_phones = driver.find_elements("xpath", "//* [contains (@class, 'phone') and contains (@class, 'link')]")
    for phone in hidden_phones:
        if phone.text not in all_phones:
            try:
                match = re.match(phone_regex, phone.text)
                if (match):
                    all_phones.append(phone.text)
                    print(phone.text, "click")
                else:
                    phone.click()
                    xpath_search()
            except:
                phone.click()
                xpath_search()
                        
if __name__ == '__main__':
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

        
        regex_search()
        xpath_search()
        click_search()
        print()
        all_phones = list(set(all_phones))

        for phone in all_phones:
            if phone != '':
                print(phone)