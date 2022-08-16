"""
We take the already exisitng ML Web Element Locator Identifying model,
and use it to predict the locators for the web elements in the new
version of the wbsite.
"""

import pickle
import pandas as pd
import mysql.connector


model_filename = 'web-locator-identifier-model.sav'
RAW_FILE = 'url_data.csv'
# DF_FILE = 'locator_label_data.csv'
element_identifiers = ['name', 'id', 'class', 'title', 'role', 'aria-label', 'accesskey', 'target']

#

model = pickle.load(open(model_filename, 'rb'))
clean_data = [] # Store data of all elements

def create_dataframe():
    # If data created from web scraping is stored in csv file, use the following command
    # df = pd.read_csv(RAW_FILE)

    # If data created from web scraping is stored in mysql, use the following block of commands
    cols = {}
    for col in element_identifiers:
        cols[col] = []
    df = pd.DataFrame(cols)
    db_config = {'host': '',
                 'user': '',
                 'password': '',
                 'database': ''}                      # Stores the database
    conn = mysql.connector.connect(**db_config)
    table_name = ''
    cursor = conn.cursor()
    query = f'select * from {table_name}'
    cursor.execute(query)
    res = cursor.fetchall()
    for i in range(len(res)):
        cols = {}
        for j in range(len(element_identifiers)):
            cols[element_identifiers[j]] = res[i][j]
        df.append(cols, ignore_index=True)

    return df


df = create_dataframe()

preds = model.predict(df[element_identifiers])
df['target'] = preds
pd.to_csv(preds, 'locator-predicted.csv', index=False)      # Store the element's attributes and the locator

"""
Now we have:
    - The element and their locators for the latest version of our webpage
"""
