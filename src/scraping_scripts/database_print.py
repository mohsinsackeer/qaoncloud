import sqlite3
from static import database
def print_all(database):
    connect = sqlite3.connect('qaoncloud.db')
    crsr = connect.cursor()
    crsr.execute('''SELECT * FROM tag_info''')
    ans = crsr.fetchall()
    for i in ans:
        print(i)

    print('done')

if __name__=='__main__':
    print_all(database)