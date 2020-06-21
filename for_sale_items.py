#This is to query the list items on criagslist because I am lazy to type them out
from bs4 import BeautifulSoup
import requests

link = requests.get("https://sfbay.craigslist.org/").text
website = BeautifulSoup(link, 'lxml')

tab_list = []
link_list = []

masterRoot = website.find('div', "housing").div
for_sale = masterRoot.find_next_sibling("div")
for_sale_left = for_sale.ul

for item in for_sale_left.find_all("li"):
    tab_list.append(item.text)

for link in for_sale_left.find_all('a'):
    link_list.append(link.get('href'))

'''
for_sale_right = for_sale.find_next_sibling("ul")

for item in for_sale_right.find_all("li"):
    tab_list.append(item.text)
'''
#leftSide = masterRoot.find_all('ul', 'left').text

#print(leftSide)