import csv
import re
from pathlib import Path

from bs4 import BeautifulSoup
import pandas as pd
import requests
import html5lib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

myFile=open('Registration.html','r')
soup=BeautifulSoup(myFile,"html5lib")
print('soup*******************************************************************************************')
print(soup.prettify())

products = []
footstrip = soup.findAll()

print('products*******************************************************************************************')
for feet in footstrip:
    products.append(feet.attrs)
print(products)

df = pd.DataFrame(products)
df.to_csv('welcome.csv', index= False, encoding='UTF-8')

dataset = pd.read_csv("welcome.csv")
df2 = pd.DataFrame(dataset, columns=['name', 'id', 'class', 'title', 'role', 'aria-label', 'accesskey', 'target','type'])
df2.to_csv('welcome2.csv', index= False, encoding='UTF-8')

empty_keys = ['name', 'id', 'class', 'title', 'role', 'aria-label', 'accesskey', 'target']
df4 = df2[df2[empty_keys].isnull().all(axis=1)]
print('empty_keys*******************************************************************************************')
print(df4)



