from for_sale_items import tab_list, link_list
from bs4 import BeautifulSoup
import requests

#limitations: this program only applies to the for-sale section on craigslist and the left side
#you can change the index number to go through whatever link you want
#options:
'''
0 - antiques
1 - appliances
2 - arts+crafts
3 - atv/utv/sno
4 - auto parts
5 - aviation
6 - baby+kid
7 - barter
8 - beauty+hlth
9 - bike parts
10 - bikes
11 - boat parts
12 - boats
13 - books
14 - business
15 - cars+trucks
16 - cds/dvd/vhs
17 - cell phones
18 - clothes+acc
19 - collectibles
20 - computer parts
21 - computers
22 - electronics
'''
index = 17
ending_link = link_list[index]
template_link = "https://sfbay.craigslist.org{}".format(ending_link)
link = requests.get(template_link).text
website = BeautifulSoup(link, 'lxml')

master_list = []

for item in website.find_all('li', "result-row"):
    item_list = []
    masterRoot = item.find('p', "result-info")

    title = masterRoot.a.text
    item_list.append(title)

    #The reason the variable name is result_meta_hierachy is because there are 2 span tags and not just price
    result_meta_hierachy = masterRoot.find('span', "result-meta")
    price = result_meta_hierachy.span.text
    item_list.append(price)

    date = masterRoot.find('time').text
    item_list.append(date)

    place = result_meta_hierachy.span.find_next_sibling('span').text
    item_list.append(place)

    master_list.append(item_list)

#class to reorganize the items in the list
class electronic:
    def __init__(self, title, price, date, place):
        self.title = title
        self.price = price
        self.date = date
        self.place = place
    def return_data(self):
        whole_thing = '''
        Title: {}
        Price: {}
        Date: {}
        Place: {}
        '''.format(self.title, self.price, self.date, self.place)
        return whole_thing

for j in master_list:
    item = electronic(j[0], j[1], j[2], j[3])
    print(item.return_data())
