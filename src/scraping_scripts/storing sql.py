import sqlite3
from static import database,df_path
import pandas as pd
#connecting to database
def create_connection(databasename):
    connection = sqlite3.connect(databasename)
    return connection

#create table
def create_table(connection):
    crsr = connection.cursor()
    sql_command = '''
    CREATE TABLE tag_info (
    lang VARCHAR(255),
    tag_name VARCHAR(255),
    charset VARCHAR(255),
    action VARCHAR(255),
    method VARCHAR(255),
    name VARCHAR(255),
    id VARCHAR(255),
    type VARCHAR(255),
    value VARCHAR(255),
    for VARCHAR(255));
    '''
    crsr.execute(sql_command)
    connection.close()
#inserting the table
def delete_table(database):

    # Connecting to sqlite
    conn = sqlite3.connect(database)

    # Creating a cursor object using
    # the cursor() method
    cursor = conn.cursor()

    # Updating
    cursor.execute('''DROP TABLE tag_info;''')

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()
def insert_into_table(database,df):
    '''
    df has tag_name ,charset,action.....
    '''
    connection=create_connection(database)
    crsr=connection.cursor()
    ldf = df.to_dict('list')
    cols = list(df.columns)

    ldf = df.to_dict('list')
    cols = list(df.columns)
    col1 = ldf[cols[0]]
    col2 = ldf[cols[1]]
    col3 = ldf[cols[2]]
    col4 = ldf[cols[3]]
    col5 = ldf[cols[4]]
    col6 = ldf[cols[5]]
    col7 = ldf[cols[6]]
    col8 = ldf[cols[7]]
    col9 = ldf[cols[8]]
    col10 = ldf[cols[9]]

    for i in range(len(df)):
        sql = '''INSERT INTO tag_info VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(col1[i],
                                                                                                            col2[i],
                                                                                                            col3[i],
                                                                                                            col4[i],
                                                                                                            col5[i],
                                                                                                            col6[i],
                                                                                                            col7[i],
                                                                                                            col8[i],
                                                                                                            col9[i],
                                                                                                            col10[i])
        crsr.execute(sql)
        # This is important to save in a table
        connection.commit()

    #closing the connection
    connection.close()



if __name__=='__main__':
    #creating the database or connecting to the database
    connection=create_connection(database)
    try:
        # drop table
        delete_table(database)
        print('deleted table')
    except:
        # creating the table
        create_table(connection)
        # importing the dataframe whihch came after scraping
        df = pd.read_csv(df_path)
        # inserting the dataframe into database
        insert_into_table(database, df)
        print('done inserting')
