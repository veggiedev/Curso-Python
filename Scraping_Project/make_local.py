from html.parser import HTMLParser
# from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

import os

import re

options = uc.ChromeOptions()
options.add_argument()
  
driver = uc.Chrome(options=options) 
# driver.get("https://www.classcentral.com/") 


# total_page_height = driver.execute_script("return document.body.scrollHeight")
# browser_window_height = driver.get_window_size(windowHandle='current')['height']
# current_position = driver.execute_script('return window.pageYOffset')

# while total_page_height - current_position > browser_window_height:
#     driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
#     current_position = driver.execute_script('return window.pageYOffset')
#     time.sleep(2)
content = driver.page_source.encode()
# assert len(driver.window_handles) == 1
# driver.refresh()
# time.sleep(5)
# wait = WebDriverWait(driver, 10)


file = open('index.html', 'wb')
file.write(content)

# original_window = driver.current_window_handle


# links = driver.find_elements(By.XPATH, "//a[@href]")
# links_list = []
# for i in links:
#     links_list.append(i.get_attribute('href'))



# soup = bs('original_index.html')



#Create clone of every site under min pages links
with open('url_list.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:  
        print(line)
        if line != 'https://www.classcentral.com' or line != 'https://www.classcentral.com/':
            if 'https://www.classcentral.com' in line:
                driver.get(line)
                total_page_height = driver.execute_script("return document.body.scrollHeight")
                browser_window_height = driver.get_window_size(windowHandle='current')['height']
                current_position = driver.execute_script('return window.pageYOffset')

                while total_page_height - current_position > browser_window_height:
                    driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
                    current_position = driver.execute_script('return window.pageYOffset')
                    time.sleep(2)
                content = driver.page_source.encode()
                file_name_list = []
                directory = 'content'
                # if line[-1] == '/':
                #     print("Found '/' in file_name")
                #     line.slice[:-1]
                #     for c in reversed(line):
                #         if c != '/':
                #                 file_name_list.append(c)
                #         else:
                #             break
                    
                #     file_name = ''.join(reversed(file_name_list)).strip()
                #     full_file_name = f'content/{file_name}.html'
                #     print(full_file_name)
                #     for file in os.listdir(directory):
                #         # if file == full_file_name:
                #         #      print('File == full_file_name')
                #         #      pass
                #         # else:
                #         file = open(f'content/{full_file_name}', 'wb')
                #         file.write(content)

                # for c in reversed(line):
                #     if c != '/':
                #         file_name_list.append(c)
                #     else:
                #         break
                print(f'This is the second to last character: {line[-2]}')
                # print(f'{file_name} Thiis is before the if sttement')
                if line[-2] == '/':
                    pass
                    # new_line = line[:-2]
                    # for c in reversed(new_line):
                    #     if c != '/':
                    #         file_name_list.append(c)
                    #     else:
                    #         break
                    # file_name = ''.join(reversed(file_name_list))
                    # print(f'This is the file_name in line with /: {file_name}')
                    # # print(file_name_stripped)
                    # # full_file_name = f'content/{file_name}.html'
                    # # print(full_file_name)

                    # file = open(f'content/{file_name}.html', 'wb')
                    # file.write(content)
                # else:
                else:
                    for c in reversed(line):
                        if c != '/':
                            file_name_list.append(c)
                        else:
                            break
                    file_name = ''.join(reversed(file_name_list))

                    print(f'This is the file_name: {file_name.strip()}')
                    # print(file_name_stripped)
                    # full_file_name = f'content/{file_name}.html'
                    # print(full_file_name)

                    file = open(f'content/{file_name.strip()}.html', 'wb')
                    file.write(content)
                # else:
                #     for c in reversed(line):
                #         if c != '/':
                #             file_name_list.append(c)
                #         else:
                #             break
                #     full_file_name = f'content/{file_name}.html'
                #     print(f'This is the else statement {full_file_name}')
                #     file = open(full_file_name, 'wb')
                #     file.write(content)



                # html = open('/home/veggiedev/Curso-Python/Scraping_Project/original_index.html')
                # soup = bs(html, 'html.parser')

                # original_text = soup.find(line[1])
                # # if url != None:
                # #     print(url)
                # file_name_list = []
                # for c in reversed(line):
                #     if c != '/':
                #             file_name_list.append(c)
                #     else:
                #         break
                # # clean_url = url.split()
                # file_name = ''.join(reversed(file_name_list))
                # if original_text is not None:
                #     original_text.find(line).replace_with(file_name)
                #     new_index = open('new_index.html')
                #     new_index.write(soup.prefix('utf-8'))



            # try:
            #     to_be_replaced.replace_with = f'file:///home/veggiedev/Curso-Python/Scraping_Project/{file_name}'
            # except AttributeError:
            #         pass
            
            # for i in to_be_replaced:
            #      if i != None:
            #         print(to_be_replaced)
        # to_be_replaced.replace_with(f'file:///home/veggiedev/Curso-Python/Scraping_Project/{file_name}')
        # page.replace(url, f'file:///home/veggiedev/Curso-Python/Scraping_Project/{file_name}')

        # for line in page:
        #     if url in line:
        #          print(line)
                            


        
