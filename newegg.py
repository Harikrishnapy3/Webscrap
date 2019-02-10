import csv
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})
filename="products.csv"
f=open(filename, "a")
headers="Product Name,shipping\n"
f.write(headers)
for container in containers:
    title_container=container.findAll("a", {"class":"item-title"})
    product_name=title_container[0].text
    shipping_container=container.findAll("li", {"class":"price-ship"})
    shipping=shipping_container[0].text.strip()
    print("product_name: "+ product_name)
    print("shipping: "+ shipping)

    f.write(product_name.replace(",", " ") + "," + shipping + "\n")
f.close()