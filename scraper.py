#loading the libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests


#trying for data request by url of the website
response=requests.get("https://www.flipkart.com/search?q=apple+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=apple+mobiles%7CMobiles&requestId=74513d15-9fcc-41ea-a7e0-16499e689ee3&as-backfill=on&otracker=nmenu_sub_Electronics_0_Apple")
#print("The Response From Site Url is ",response)

# if the response code is 200 then we can access the data from website
#here im using jiomart data

soup=BeautifulSoup(response.content,"html.parser")

#print(soup)

'''
-----------Fetching the Names ------------
'''
names=soup.find_all('div',class_="KzDlHZ")

name_list=[]
for name in names:
    d=name.text
    name_list.append(d)
    #print(d)

#print(name_list)    


'''
-----------Fetching the Prices ------------
'''

prices=soup.find_all("div",class_="Nx9bqj _4b5DiR")
price_list=[]

for price in prices:
    p=price.text
    price_list.append(p)

#print(price_list)

'''
-----------Fetching the Specifications ------------
'''

specifications=soup.find_all("ul",class_="G4BRas")#tag --> class name

specification_list=[]

for spec in specifications:
    s=spec.text
    specification_list.append(s)

#print(specification_list)

'''
-----------Fetching the Ratings------------
'''

ratings=soup.find_all("div",class_="XQDdHH")

ratings_list=[]

for rate in ratings:
    r=rate.text
    ratings_list.append(r)

#print(ratings_list)

'''
-----------Fetching the ratings and reviews ------------
'''
number_of_ratings=soup.find_all("span",class_="Wphh3N")

no_of_reviews_list=[]
for re in number_of_ratings:
    r=re.text
    
    no_of_reviews_list.append(r)

#print(no_of_reviews_list)

'''
-----------Fetching the images ------------
'''

images=soup.find_all("img",class_="DByuf4")
images_list=[]
for i in images:
    d=i['src']
    images_list.append(d)

#print(images_list)

'''
-----------Fetching the Links ------------
'''

links=soup.find_all("a",class_="CGtC98")

link_list=[]

for link in links:
    l="https://www.flipkart.com"+link['href']
    link_list.append(l)

#print(link_list)
'''
for i in [name_list,price_list,specification_list,ratings_list,no_of_reviews_list,images_list,link_list]:
    print(len(i))
'''



"""Converting to structured format
"""
import pandas as pd

# Ensure lists have at least 25 elements; truncate or extend as necessary
name_list = name_list[:25] + [None] * (25 - len(name_list))
price_list = price_list[:25] + [None] * (25 - len(price_list))
specification_list = specification_list[:25] + [None] * (25 - len(specification_list))
ratings_list = ratings_list[:25] + [None] * (25 - len(ratings_list))
no_of_reviews_list = no_of_reviews_list[:25] + [None] * (25 - len(no_of_reviews_list))
images_list = images_list[:25] + [None] * (25 - len(images_list))
link_list = link_list[:25] + [None] * (25 - len(link_list))

d = {
    "Names": pd.Series(name_list),
    "Prices": price_list,
    "Specifications": specification_list,
    "Ratings": ratings_list,
    "Number Of Reviews And Ratings": no_of_reviews_list,
    "Images": images_list,
    "Links": link_list
}

df = pd.DataFrame(d)
print(df.head(5))

df.to_csv("Scraped_Data.csv")
print(df.shape)