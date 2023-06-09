from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests

driver = webdriver.Chrome()
driver.get("https://www.pap.pl/")

#Zadanie 1.
try:
    cookies_accept = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='ok closeButton']"))
    )
    cookies_accept.click()
    print("Cookies accepted")
except:
    print("Unable to accept cookies.")

#Zadanie 2.
driver.maximize_window()

#Zadanie 3.
try:
    language_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='http://www.pap.pl/en']"))
    )
    language_link.click()
    print("Language changed to English.")
except:
    print("Unable to change language.")

#Zadanie 4
try:
    business_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ('//a[@href="/en/business"]'))
    ))
    business_link.click()
    print("Navigated to the Business section")
except:
    print("Unable to navigate to the Business section")

#Zadanie 5.
news_titles = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='title']/a"))
)

titles = []
print("Titles:")
for title in news_titles:
    print(title.text)

#Zadanie 6
image_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".imageWrapper img"))
)

if not os.path.exists("Photos"):
    os.makedirs("Photos")

for i, img in enumerate(image_elements):
    img_url = img.get_attribute("src")
    img_file = f"Photos/photo{i}.jpg"
    response = requests.get(img_url, stream=True)
    if response.ok:
        with open(img_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


#Zadanie 7

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#Zadanie 8 nie działa przy użyciu tego powyżej, dlatego skorzystałem z:
driver.execute_script("window.scrollBy(0,1600)")

#Zadanie 8
try:
    last_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="?page=78"]'))
    )
    last_page.click()
    current_page = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[@title="Current page"]'))
    )
    page_number = current_page.text.strip()
    print(f"The last page number is {page_number}")

except:
    print("Unable to navigate to the last page")




