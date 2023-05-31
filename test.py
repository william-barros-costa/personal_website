from selenium import webdriver

cdriver=r"C:\Users\William\Desktop\repository\personal_website\chromedriver.exe"
vivaldi=r"C:\Users\William\AppData\Local\Vivaldi\Application\vivaldi.exe"

options = webdriver.ChromeOptions()
options.binary_location = vivaldi

driver = webdriver.Chrome(cdriver, options=options) 

driver.get("http://www.google.com")