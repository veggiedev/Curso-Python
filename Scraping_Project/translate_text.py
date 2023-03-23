from deep_translator import GoogleTranslator as ts
from bs4 import BeautifulSoup as bs
import os

import argostranslate.package, argostranslate.translate
import translatehtml

from_code = "en"
to_code = "hi"
# with open('/home/veggiedev/Curso-Python/Scraping_Project/original_index.html', 'r') as f:
#     # web = f.read()
#     soup = bs(f, 'html.parser')
#     new_soup = soup.prettify('utf-8')
# # f = 'original_index.html'
#     # web = file.read()web
#     print(new_soup)

directory = '/home/veggiedev/Curso-Python/Scraping_Project/original_content'

# print(f)
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    with open(file, 'r') as f:
    # web = f.read()
        soup = bs(f, 'html.parser')
        new_soup = soup.prettify('utf-8')
    print(filename)
    # Download and install Argos Translate package
    available_packages = argostranslate.package.get_available_packages()
    available_package = list(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )[0]

    download_path = available_package.download()
    argostranslate.package.install_from_path(download_path)

    # Translate
    installed_languages = argostranslate.translate.get_installed_languages()
    # print(installed_languages)
    from_lang = list(filter(lambda x: x.code == from_code, installed_languages))[0]
    # print(from_lang)
    to_lang = list(filter(lambda x: x.code == to_code, installed_languages))[0]
    # print(to_lang)
    translation = from_lang.get_translation(to_lang)

    translated_soup = translatehtml.translate_html(translation, new_soup)

    # print(translated_soup)

    new_directory = '/home/veggiedev/Curso-Python/Scraping_Project/content/'

    with open(f'{new_directory}{filename}', 'wb') as f:
        f.write(translated_soup.prettify('utf-8'))



    # translator = ts(source='auto', target='hi')

    # list_text = []


    # directory = '/home/veggiedev/Curso-Python/Scraping_Project/content'
    # for filename in os.listdir(directory):
    #     f = os.path.join(directory, filename)
    #     print(f)


        # with open(f, 'r') as document:
        #         web = document.read()
        #         soup = bs(web, 'html.parser')
        #         # print(soup.prettify('utf-8'))
        #         # text = soup.find_all('a')
        #         for row in soup.find_all('label'):
        #             string = row.getText()
        #             # text = row.text
        #             # text.replace_with(translator.translate(string))
        #             list_text.append(string)



        # with open(f, 'r') as document:
        #     web = document.read()
        #     soup = bs(web, 'html.parser')
        #     # print(soup.prettify('utf-8'))
        #     # text = soup.find_all('a')
        #     for row in soup.find_all('li'):
        #         string = row.getText()
        #         # text = row.text
        #         # text.replace_with(translator.translate(string))
        #         list_text.append(string)



        # with open(f, 'r') as document:
        #         web = document.read()
        #         soup = bs(web, 'html.parser')
        #         # print(soup.prettify('utf-8'))
        #         # text = soup.find_all('a')
        #         for row in soup.find_all('span'):
        #             string = row.getText()
        #             # text = row.text
        #             # text.replace_with(translator.translate(string))
        #             list_text.append(string)

    # for row in site_text:            
        # print(filedata)
            # print(filedata)


            # prettified_code = soup.prettify('utf-8')
            # pre

        # 
        # 
        #   # print(soup.prettify('utf-8'))
        #     # text = soup.find_all('a')
        #     for i in soup:
        #         filedata = soup.prettify('utf-8')
        #         # print(filedata)
        #         for i in soup.find_all(row.strip()):
        #             # if row.strip == i
        #             filedata = filedata.replace(i, translator.translate(i))

        #         newdoc = open('new_full_index.html', 'wb')
        #         newdoc.write(filedata)
                # string = row.getText()
                # # text = row.text
                # # text.replace_with(translator.translate(string))
                # list_text.append(string.strip())

    # with open(f, 'r') as document:
    #     web = document.read()
    #     soup = bs(web, 'lxml')
    #     # print(soup.prettify('utf-8'))
    #     # text = soup.find_all('a')
    #     for row in soup.find_all('p'):
    #         string = row.getText()
    #         # text = row.text
    #         # text.replace_with(translator.translate(string))
    #         list_text.append(string.strip())
    #         # print(string)


    # with open(f, 'r') as document:
    #     web = document.read()
    #     soup = bs(web, 'lxml')
    #     # print(soup.prettify('utf-8'))
    #     # text = soup.find_all('a')
    #     for row in soup.find_all('h1'):
    #         string = row.getText()
    #         # text = row.text
    #         # text.replace_with(translator.translate(string))
    #         list_text.append(string.strip())
    #         # print(string)

    # with open(f, 'r') as document:
    #     web = document.read()
    #     soup = bs(web, 'lxml')
    #     # print(soup.prettify('utf-8'))
    #     # text = soup.find_all('a')
    #     for row in soup.find_all('h2'):
    #         string = row.getText()
    #         # text = row.text
    #         # text.replace_with(translator.translate(string))
    #         list_text.append(string.strip())
    #         # print(string)

    # with open(f, 'r') as document:
    #     web = document.read()
    #     soup = bs(web, 'lxml')

    #     # print(soup.prettify('utf-8'))
    #     # text = soup.find_all('a')
    #     for row in soup.find_all('h3'):
    #         string = row.getText()
    #         # text = row.text
    #         # text.replace_with(translator.translate(string))
    #         list_text.append(string.strip())
    #         # print(string)











    # # old_name = f
    # # new_name = f'{f[:-4]}txt'

    # # os.rename(old_name, new_name)





    # # print(site_text)
    # document = open(f, 'rb')
    # print(document)


    # soup = bs(document, 'html.parser')

    # print(soup.prettify('utf-8'))
    # filedata_raw = soup.find_all('a')
    # for i in filedata_raw:
    #     filedata = i.getText()
    #     for string in site_text_open:
    #         filedata = filedata.replace(string, translator.translate(string))

    #     newdoc = open('new_full_index.html', 'w')
    #     newdoc.write(filedata)



    # # txt_name = new_name
    # # definitive_name = old_name

    # # os.rename(txt_name, definitive_name)
