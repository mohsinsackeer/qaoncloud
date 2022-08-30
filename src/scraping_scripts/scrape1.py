from bs4 import BeautifulSoup
import pandas as pd
'''
from static import url
url=url
c=requests.get(url)
page=BeautifulSoup(c,'html.parser')
'''
def scrape_page(f,file_name):
    '''
    f is the file.
    As it is in development stage i have used file.We can also url in the place of file.
    It stores the all tag_info in the filename given.Be careful in giving the file name
    .end it with csv.
    We can use the below down code if we are working with url.
    from static import url
    url=url
    c=requests.get(url)
    page=BeautifulSoup(c,'html.parser')
    '''
    page = BeautifulSoup(f, 'html.parser')
    products = []
    footstrip = page.findAll()
    print('products*******************************************************************************************')
    for feet in footstrip:
        # tag_info=[feet.name].extend()
        tag_sibling = feet.next_sibling
        tag_name = feet.name  # return the tag name of an html element
        tag_info = feet.attrs  # tag_info is a dictionary
        tag_info['tag_name'] = tag_name
        products.append(tag_info)
    print('done_storing')
    df = pd.DataFrame(products)
    df.to_csv(file_name)
with open('registration1.html','r') as f:
    scrape_page(f,'tag_info.csv')