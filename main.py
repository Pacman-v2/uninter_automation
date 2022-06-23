from selenium import webdriver
from selenium.webdriver.common.by import By

from dados import user, senha

navegador = webdriver.Chrome()

while True:
    try:
        navegador.get("https://univirtus.uninter.com/ava/web/")

    except:
        continue

    else:
        break

navegador.find_element(By.NAME, "ru").send_keys(user)
navegador.find_element((By.XPATH, "//input[@id='senha']"))
