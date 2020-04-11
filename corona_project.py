import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
print(r.text) #text is for HTML FILE
html=r.text
soup=BeautifulSoup(html,'html.parser') 
print(soup.title.text)
print()
print()
live_data=soup.find_all('div',id='maincounter-wrap')
print(live_data)
for i in live_data:
    print(i.text)
table_body=soup.find("tbody")     
table_rows=table_body.find_all('tr')
countries=[]
totalcases=[]
newcases=[]
totaldeaths=[]
todaysdeaths=[]
totalrecoveries=[]
for tr in table_rows:
    td=tr.find_all('td')
    countries.append(td[0].text)
    totalcases.append(td[1].text)
    newcases.append(td[2].text)
    totaldeaths.append(td[3].text)
    todaysdeaths.append(td[4].text)
    totalrecoveries.append(td[5].text)
headers=['Countries','Total Cases','New Cases', 'total Deaths','todays Deaths','total Recoveries']
df=pd.DataFrame(list(zip(countries,totalcases,newcases,totaldeaths,todaysdeaths,totalrecoveries)),columns=headers)
print(df)
df.to_csv("C:\\Users\\HP\\Desktop\\project\\data.csv")
