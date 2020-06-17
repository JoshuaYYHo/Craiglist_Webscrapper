from bs4 import BeautifulSoup
import requests

link = requests.get("https://sfbay.craigslist.org/d/cell-phones/search/moa").text
website = BeautifulSoup(link, 'lxml')

#prints out the whole website
#print(website.prettify())

#list_item = website.find_all('li', class_ = "result-row")
master_list = []


for item in website.find_all('li', "result-row"):
    item_list = []
    masterRoot = item.find('p', "result-info")

    title = masterRoot.a.text
    item_list.append(title)
    #print("Title: " + title)

    price = masterRoot.find('span', "result-meta").span.text
    item_list.append(price)
    #print("Price: " + price)

    date = masterRoot.find('time').text
    item_list.append(date)
    """
    item_list.append(price.find_next_sibling)
    
    """
    master_list.append(item_list)
    print(item_list)

print(master_list)

#class to reorganize the items in the list
class electronic:
    def __init__(self, title, price, date):
        self.title = title
        self.price = price
        self.date = date
    def print_data(self):
        print("Title: " + self.title + "\n" + "Price: " + self.price + "\n" + "Date: "+ self.date + "\n")


for j in master_list:
    item = electronic(j[0], j[1], j[2])
    j = item
    item.print_data()

def cheapest_item():
    cheapest_item = master_list[0]
    for i in master_list:
        if cheapest_item.price < i.price:
            cheapest_item = i.price
    return cheapest_item.print_data()

print(cheapest_item)