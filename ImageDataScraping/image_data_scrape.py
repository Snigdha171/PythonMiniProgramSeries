# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 00:02:25 2020

@author: Prachi Prakash
"""

# D:\Prachi - online-education\Python Mini Projects\Python Mini Program Series\imageDataScraping\ImageDataScraping

from selenium import webdriver
import time

search_string = input('Enter the string to be searched : ')

search_query = 'https://en.wikipedia.org/wiki/'+search_string

# Creating an instance of Google Chrome
driver = webdriver.Chrome(executable_path='C:/Users/Prachi Prakash/Downloads/chromedriver_win32/chromedriver.exe')

driver.get(search_query)

image_tag = driver.find_elements_by_xpath("//table[contains(@class,'infobox vcard')]/tbody/tr[1]/td")[0]
                                          
FILE_PATH_FOLDER = 'D:\Prachi - online-education\Python Mini Projects\Python Mini Program Series\imageDataScraping\ImageDataScraping'

time.sleep(10)

file_name_search_string = search_string.replace(" ", "_") 

final_filename = FILE_PATH_FOLDER + "/" + file_name_search_string + '.png'

print(final_filename)

image_tag.screenshot(final_filename)

driver.quit()
