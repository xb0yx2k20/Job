from selenium import webdriver

# Создайте объект ChromeOptions
chrome_options = webdriver.ChromeOptions()

# Укажите путь к драйверу в ChromeOptions
chrome_options.add_argument('--chromedriver=/Users/xb0yx2k20/Downloads/chromedriver_mac_arm64/chromedriver')

# Добавьте любые другие необходимые опции
# Например, отключение отображения изображений
chrome_options.add_argument('--blink-settings=imagesEnabled=false')

# Используйте объект ChromeOptions при создании объекта WebDriver
driver = webdriver.Chrome(options=chrome_options)

