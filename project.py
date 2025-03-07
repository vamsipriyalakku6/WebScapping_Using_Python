# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qo_jRf1egwESSOkVTq1ebwoK4lR40wlI
"""

#import libraries
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Identify the URL
URL="http://quotes.toscrape.com/"

#Loading the WebPage in Memory using request
page=requests.get(URL)

#Checking Status Code
page.status_code

#Extracting the HTML Code of the Webpage
htmlCode=page.text
soup=BeautifulSoup(htmlCode)
htmlCode

content=soup.find("div",attrs={"class":"container"})
text=content.text
#print(text)
r1=text.split("\n")
#print(r1)
r2=[]
for i in r1:
    if i!='' and i != '\r':
        r2.append(i)
#print(r2)
r3=[]
for i in r2:
    k=i.strip()
    r3.append(k)
#print(r3)
r4=[]
for i in r3:
    if i!='':
     r4.append(i)
#print(r4)
data=[]
for i in r4:
    if len(i)>10:
     data.append(i)
#print(data)



# Extracting quotes and authors
quotes = []
authors = []
for i in range(len(data)):
    if data[i].startswith("“") and (i + 1) < len(data) and data[i + 1].startswith("by"):
        quotes.append(data[i])
        authors.append(data[i + 1].replace("by ", ""))

print(quotes)
print(authors)

# Creating DataFrame
df = pd.DataFrame({"Quote": quotes, "Author": authors})

# Display DataFrame

# Display DataFrame
df

df.head()

df.shape

#Saving the DataFrame
df.to_csv("quotes.csv",header=True,index=False)

#Downloading
from google.colab import files
files.download("quotes.csv")