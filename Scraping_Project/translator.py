from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# import translators as ts
import os
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from googletrans import Translator
import lxml
from selenium.webdriver.common.by import By
from deep_translator import GoogleTranslator as ts
import re
# prefs = {
#     "translate":{"enabled":"true"},
#     "translate_whitelists":{"en":"hi"}
  
# }
# options = Options()
# options.add_argument("--lang=hi")
# options.add_experimental_option("prefs", prefs)
# # options.add_argument("--headless")
# driver = webdriver.Chrome() 
# driver.get('https://translate.google.com/') 
# time.sleep(2)
# accept_button = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div")
# accept_button.click()
# time.sleep(3)
# button = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button")
# button.click()
# time.sleep(5)
# hindi_button = driver.find_element(By.XPATH, ("//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[3]/div/div[2]/div[54]/div[2]"))
# hindi_button.click()
# time.sleep(2)



# total_page_height = driver.execute_script("return document.body.scrollHeight")
# browser_window_height = driver.get_window_size(windowHandle='current')['height']
# current_position = driver.execute_script('return window.pageYOffset')

# while total_page_height - current_position > browser_window_height:
#     driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
#     current_position = driver.execute_script('return window.pageYOffset')
#     time.sleep(2)
# content = driver.page_source.encode()
# print(content)
# assert len(driver.window_handles) == 1
# driver.refresh()
# time.sleep(5)
# wait = WebDriverWait(driver, 10)
# driver = webdriver.Chrome() 
# web = driver.get('https://www.classcentral.com')
# translator = Translator()


translator = ts(source='auto', target='hi')

list_text = []

# base = os.path.dirname(os.path.abspath(__file__))
# html = open(os.path.join(base, 'site_clone_original.html'))
# soup = bs(html, 'html.parser')
# print(soup.prettify('utf-8'))
# text = soup.find_all('a')

# for i in soup:
#     translated = i.replace()
#     i.replace_with

# with open("example_modified.html", "wb") as f_output:
#     f_output.write(soup.prettify("utf-8"))  



with open('/home/veggiedev/Curso-Python/Scraping_Project/site_clone_original.html', 'r') as f:
    web = f.read()
    soup = bs(web, 'html.parser')
    # print(soup.prettify('utf-8'))
    # text = soup.find_all('a')
    for row in soup.find_all('a'):
        string = row.getText().strip()
        # text = row.text
        # text.replace_with(translator.translate(string))
        list_text.append(string)
    # print(list_text)

for string in list_text:
    try:
        html = open('/home/veggiedev/Curso-Python/Scraping_Project/site_clone_original.html')
        soup = bs(html, 'html.parser')
        the_string = soup.find(text =re.compile(string))
        print(the_string)
        translation = translator.translate(string)
        print(translation)
        new_text = the_string.replace(string, translation)
        the_string.replace_with(new_text)
    except AttributeError:
        pass
new_html = open('/home/veggiedev/Curso-Python/Scraping_Project/translated_site.html', 'wb')
new_html.write(soup.prettify('utf-8'))
    # print(list_text)
    # for string in list_text:
    #     old_string = soup.find(string)
    #     old_string.string.replace_with(translator.translate(string))




    # strong = soup.find('a', string)
    # print(strong)
        # i.replace_with(translator.translate(string))
# with open('trans_index.html', 'wb') as f_output:
#     f_output.write(soup.prettify('utf-8'))

# for i in list_text:
#     with open('/home/veggiedev/Curso-Python/Scraping_Project/site_clone_original.html') as f:
#         web = f.read()
#         soup = bs(web, 'html.parser')
#         text = soup.find_all('a')
#         print(text)
#     driver = webdriver.Chrome() 
#     translated_text = translator.translate(string)
#     row.replace_with(translated_text)
# f.write(soup.prettify('utf-8'))





    # driver.get('https://translate.google.com/?sl=auto&tl=hi&op=translate') 
    # time.sleep(2)
    # textarea = driver.find_element(By.XPATH, "//textarea[@role='combobox'")
    # textarea.click()
    # time.sleep(1)
    # button = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button")
    # button.click()
    # time.sleep(5)
    # hindi_button = driver.find_element(By.XPATH, "//div[@data-language-code='hi'")
    # hindi_button.click()
    # time.sleep(2)
#         stripped_string = string.strip()
#         current_text = stripped_string
#         print(current_text)
#         print(translator.detect(stripped_string))
        # print(translator.translate(text=stripped_string, dest='hi', src='en'))
        # time.sleep(1)

    # for i in text:
    #     # each_text = i.get_text()
    #     translation = translator.translate(i, dest='hi', src='en')


    #     print(translation.text)
    # text = soup.get_text()
    # print(text)




    # translator = Translator()
    # translator.translate(text, dest='hi')
    # print(text)
    # print(soup.prettify())
        # file_translate = Translator()
        # result = Translator.translate(line,  dest='hi')
        # print(result.text)
    # print(soup.prettify())


# soup = bs(web, 'html.parser')


# print(soup.prettify())














# with open('/home/veggiedev/Curso-Python/Scraping_Project/content/report.html') as file:
#     soup = bs()
#     print(soup)



# file = open('index_text.txt', 'r')
# site = file.read()
# print(site)
