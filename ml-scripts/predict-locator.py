"""
We take the already exisitng ML Web Element Locator Identifying model,
and use it to predict the locators for the web elements in the new
version of the wbsite.
"""

import csv
import pickle
import pandas as pd


model_filename = 'web-locator-identifier-model.sav'
RAW_FILE = 'url_data.csv'
# DF_FILE = 'locator_label_data.csv'
element_identifiers = ['name', 'id', 'class', 'title', 'role', 'aria-label', 'accesskey', 'target']

def label_data(model,d):
    pred_x = [d]
    pred_x = pd.DataFrame(pred_x)
    pred_y = model.predict(pred_x)      # Predicts the correct locator using the exisitng model
    d.update({'target': pred_y.to_numpy()[0]})

model = pickle.load(open(model_filename, 'rb'))
clean_data = [] # Store data of all elements

"""
with open(RAW_FILE, 'r', encoding='utf-8') as r: #, open(DF_FILE, 'w', encoding='utf-8', newline='') as dfFile:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        element_dict = {k: v.strip('""') for l, v in re.findall(r'(\S+)=(".*?"|\S+)', row[1])}
        d = {k: element_dict.get(k, None) for k in element_key}
        label_data(model, d)
        clean_data.append(d)
"""

df = pd.read_csv(RAW_FILE)
preds = model.predict(df[element_key])
df['target'] = preds
pd.to_csv(preds, 'locator-predicted.csv', index=False)      # Store the element's attributes and the locator

"""
Now we have:
    - The element and their locators for the latest version of our webpage
"""
